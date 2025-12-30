import pandas as pd
from adminpage import tambah_subs
from transaksi import id_pembayarann,id_pesanann
import time


def load():  # Mengambil dan mangubah csv menjadi dic
    user = pd.read_csv('akun_user.csv')
    subs = pd.read_csv('subs.csv')
    daftar_subs = pd.read_csv('daftar_subs.csv')
    return user, subs, daftar_subs

def load_detail():
    return pd.read_csv('detail_subs.csv')

def menu_subs(current):
    user, _, _ = load()  # hanya mengambil data dibawah kolom 'user', subs dan daftar subs diabaikan.
    user_role = user[user['username'] == current]['role'].values[0]  # mengambil data role

    if user_role == 1:  # Menu subs untuk user
        while True:
            print("\n=== Menu Subscription ===")
            print("1. Pesan Subscription")
            print("2. Subscription yang lagi aktif")
            print("3. Kembali")

            pilihan = input("Pilih Opsi: ")
            print()

            if int(pilihan) == 1:
                pesan_subs(current)  # Lompat ke line 76
            elif int(pilihan) == 2:
                cek_subs(current)  # Lompat ke line 130
            elif int(pilihan) == 3:
                return
            else:
                print("Opsi tidak tersedia\n")

    elif user_role == 2:  # Menu subs untuk admins
        while True:
            print("\n=== Menu Subscription ===")
            print("1. List Subscription")
            print("2. Tambah Subscription")
            print("3. Kembali")

            pilihan = input("Pilih Opsi: ")
            print()

            if int(pilihan) == 1:
                list_subs()  # Line 51
            elif int(pilihan) == 2:
                tambah_subs()  # Admin Page Line 23
            elif int(pilihan) == 3:
                return
            else:
                print("Opsi tidak tersedia\n")

def list_subs():
    perPage = 5
    startPage = 0
    _, _, daftar_subs = load()

    while True:
        endPage = startPage + perPage
        page = daftar_subs.iloc[startPage:endPage]

        if page.empty:
            print("Tidak ada subscription lagi untuk ditampilkan")
            break

        kolomTampil = ["nama", "harga"]
        print("\n=== Daftar Subscription yang ada ===")
        print(f"{page[kolomTampil].to_markdown(index=False)}\n")

        userInput = input(
            "Ketik 'lanjut' untuk melihat data berikutnya\n"
            "Ketik 'keluar' atau apa saja untuk keluar: "
        ).lower()

        if userInput == "lanjut":
            startPage += perPage
        else:
            print()
            break

def detail_subs(kode):
    detail_paket = load_detail()
    detail = detail_paket[detail_paket['kode'] == kode]
    
    if detail.empty:
        print("Detail Paket Tidak")
        return
    
    kolomtampil = [
        'deskripsi',
        'isi_sayur',
        'berat_total',
        'frekuensi',
        'durasi'
    ]
    
    print("\n=== Detail Paket Sayur ===")
    print(f"{detail[kolomtampil].to_markdown(index= False)}\n")
        
def pesan_subs(username):
    perPage = 5
    startPage = 0
    _, subs, daftar_subs = load()

    while True:
        endPage = startPage + perPage
        page = daftar_subs.iloc[startPage:endPage]

        if page.empty:
            print("Tidak ada subscription lagi untuk ditampilkan")
            break

        kolomTampil = ["nama", "harga"]

        page_display = page[kolomTampil].copy()
        page_display.index += 1

        print("\n=== Daftar Paket ===")
        print(page_display.to_markdown(index=True))
        print()

        userInput = input(
            "Ketik 'lanjut' untuk melihat data berikutnya\n"
            "Ketik 'detail' untuk melihat detail paket\n"
            "Ketik nomor untuk membeli\n"
            "Ketik 'keluar' untuk keluar: "
        ).lower()

        if userInput == "lanjut":
            startPage += perPage

        elif userInput == "detail":
            try:
                nomor = int(input("Masukkan nomor paket: ")) - 1
                if 0 <= nomor < len(page):
                    kode = page.iloc[nomor]['kode']
                    detail_subs(kode)
                else:
                    print("Nomor tidak valid")
            except ValueError:
                print("Input harus berupa angka")

        elif userInput.isdigit():
            nomor = int(userInput) - 1

            if 0 <= nomor < len(page):
                nama = page.iloc[nomor]['nama']
                kode = page.iloc[nomor]['kode']

                check = input(
                    f"Apakah kamu ingin membeli '{nama}'? (ya/tidak): "
                ).lower()

                if check == "ya":
                    valid_timestamp = int(time.time()) + (30 * 24 * 60 * 60)
                    while True:
                            metode_pembayaran = input("Pilih Metode Pembayaran:\n1. QRIS\n2. Apple Pay\n3. Master Card\nPilih : ")
                            if metode_pembayaran == "1":
                                metode = "QRIS"
                                break
                            elif metode_pembayaran == "2":
                                metode = "Apple Pay"
                                break
                            elif metode_pembayaran == "3":
                                metode = "Master Card"
                                break
                            else:
                                print("Masukkan Pilihan Yang Tepat :>")
                        
                    id_pesanan = id_pesanann(subs)
                    id_pembayaran = id_pembayarann(subs)

                    new_subs = pd.DataFrame({
                        'username': [username],
                        'kode': [kode],
                        'valid': [valid_timestamp],
                        'metode_pembayaran' : [metode],
                        'id_pesanan' : [id_pesanan],
                        'id_pembayaran' :[id_pembayaran]
                    })

                    subs = pd.concat([subs, new_subs], ignore_index=True)
                    subs.to_csv('subs.csv', index=False)

                    print(f"Berhasil membeli subscription '{nama}'")
                    break
                else:
                    print("Pembelian dibatalkan")
            else:
                print("Nomor tidak valid")

        elif userInput == "keluar":
            break

        else:
            print("Input tidak dikenali")



def cek_subs(username):
    perPage = 5
    startPage = 0
    _, subs, daftar_subs = load()

    user_subs = subs[subs['username'] == username]

    while True:
        endPage = startPage + perPage
        page = user_subs.iloc[startPage:endPage]

        if page.empty:
            print("Kamu tidak memiliki subscription")
            break

        page_merged = page.merge(
            daftar_subs,
            left_on='kode',
            right_on='kode'
        )

        page_merged['valid'] = (
            pd.to_datetime(page_merged['valid'], unit='s')
            .dt.strftime('%d/%m/%Y')
        )

        kolomTampil = ["nama", "harga", "valid"]
        print("\n=== Subscription Aktif ===")
        print(f"{page_merged[kolomTampil].to_markdown(index=False)}\n")

        userInput = input(
            "Ketik 'lanjut' untuk melihat data berikutnya\n"
            "Ketik 'keluar' atau apa saja untuk keluar: "
        ).lower()

        if userInput == "lanjut":
            startPage += perPage
        else:
            print()
            break

