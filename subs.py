import pandas as pd

from adminpage import tambah_subs
import time

def load(): #Mengambil dan mangubah csv menjadi dic
    user = pd.read_csv('akun_user.csv')
    subs = pd.read_csv('subs.csv')
    daftar_subs = pd.read_csv('daftar_subs.csv')
    return user, subs, daftar_subs

def menu_subs(current):
    user, _, _ = load() #hanya mengambil data dibawah kolom 'user', subs dan daftar subs diabaikan.
    user_role = user[user['username'] == current]['role'].values[0] #mengambil data role dari variable user line 13. values 0 berarti mengambil satu data dari kolom target
    if user_role == 1: #Menu subs untuk user
        while True:
            print("\n=== Menu Subscription ===")
            print("1. Pesan Subscription")
            print("2. Subscription yang lagi aktif")
            print("3. Kembali")
            pilihan = input("Pilih Opsi: ")
            print()

            if int(pilihan) == 1:
                pesan_subs(current) #Lompat ke line 76
            elif int(pilihan) == 2:
                cek_subs(current) #Lompat ke line 130
            elif int(pilihan) == 3:
                return
            else:
                print("Opsi tidak tersedia\n")

    elif user_role == 2: #Menu subs untuk admins
        while True:
            print("\n=== Menu Subscription ===")
            print("1. List Subscription")
            print("2. Tambah Subscription")
            print("3. Kembali")
            pilihan = input("Pilih Opsi: ")
            print()

            if int(pilihan) == 1:
                list_subs() #Line 51
            elif int(pilihan) == 2:
                tambah_subs() #Admin Page Line 23
            elif int(pilihan) == 3:
                return
            else:
                print("Opsi tidak tersedia\n")

def list_subs():
    perPage = 5 #index untuk kali pencet itu keluarnya 5 item sayur
    startPage = 0 #mulai dari 0 ya kak (index pertama dari subs.csv)
    _, _, daftar_subs = load() #mengambil daftar_subs dari load, mengabaikan user dan subs
    
    while True:
        endPage = startPage + perPage #Ini untuk mengatur halaman, cth Startpage = 0, perpage = 5. berarti di print dari 0-5. dst.
        page = daftar_subs.iloc[startPage:endPage]
        if page.empty: #kalau kosong ini mahh.
            print("Tidak ada subscription lagi untuk ditampilkan")
            break
        
        #Setting tampilan
        kolomTampil = ["nama","harga"] #ini untuk mengatur bagian atas table, nanti data dibawahnya bakal ngikutin. keren dan rapih :>
        print("\n=== Daftar Subscription yang ada ===") #halah nyocot
        print(f"{page[kolomTampil].to_markdown(index=False)}\n")#Page = line 58, kolom tampil = line 64,
                                                                #to_markdown itu rahasia dari kenapa data bisa di print sesuai kolomtampil, 
                                                                #index nya harus dihapus dengan = False.
        
        userInput = input("Ketik 'lanjut' untuk melihat data berikutnya\nKetik 'keluar' atau apa saja untuk keluar: ").lower()
        
        if userInput == "lanjut":
            startPage += perPage #Quiz dadakan, ini berarti nanti di print dari halaman berapa ke berapa coba :>
        else:
            print() #jujur, ini itu sebenernya print kosong biar yaudah, KOSONG aja gitu
            break

def pesan_subs(username):
    perPage = 5
    startPage = 0
    _, subs, daftar_subs = load()

    while True:
        endPage = startPage + perPage
        page = daftar_subs.iloc[startPage:endPage] #lagi-lagi ketemu si kurungan buat index [darisini:kesini] darisini saat ini = 0 dan kesini = 5
        if page.empty:
            print("Tidak ada subscription lagi untuk ditampilkan")
            break
        
        #Setting tampilan
        kolomTampil = ["nama", "harga"]
        print("\n=== Daftar Subscription yang ada ===")
        page[kolomTampil].reset_index(drop=True, inplace=True)  #reset_index adalah kata kerja untuk mereset index dengan ketentuan
                                                                #(drop atau "hapus", dan inplace atau "Buat baru bang dari 0")
        page_display = page[kolomTampil].copy() #copy() untuk mengcopy si page[kolomtampils] biar tidak terjadi hal yang tidak-tidak
                                                #ibarat bikin dia jadi badut buat jadi pelampiasan :<
        page_display.index += 1 #setelah di jadiin 0 indexnya, kodingan ini akan membuat si index dimulai dari 1. kayak pdkt gitu deh 
        print(f"{page_display.to_markdown(index=True)}\n") #kalau masih gapaham si keterlaluan ya, balik lagi gih ke line 66
        
        userInput = input("Ketik 'lanjut' untuk melihat data berikutnya\nKetik nomor untuk membeli\nKetik 'keluar' atau apa saja untuk keluar: ").lower()
        if userInput.isdigit():
            nomor = int(userInput) - 1
            if 0 <= nomor < len(page):
                nama = page.iloc[nomor]['nama']
                kode = page.iloc[nomor]['kode']
                check = input(f"Apakah kamu ingin membeli '{nama}'? (Ya/Tidak) : ").lower()
                if check == "ya":
                    
                    # Hitung timestamp sebulan kedepan (Total hari * total jam * total menit * total detik)
                    valid_timestamp = int(time.time()) + (30 * 24 * 60 * 60)
                    
                    # Masukkin ke database
                    new_subs = pd.DataFrame({
                        'username': [username],
                        'kode': [kode],
                        'valid': [valid_timestamp]
                    })
                    subs_updated = pd.concat([subs, new_subs], ignore_index=True) #concat, itu untuk menambah baris.
                                                                        # anggap aja subs yang merupakan data lama, ditambah newsubs yang merupakan databaru.
                    subs_updated.to_csv('subs.csv', index=False) #Setelah itu append deh ke csv pake to_csv(kayak nge stemple ulang datanya)
                    
                    print(f"Berhasil membeli subscription '{nama}'")
                    break
                else:
                    continue
            else:
                print("Nomor tidak valid")
        elif userInput == "keluar":
            print()
            break

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
        
        page_merged = page.merge(daftar_subs, left_on='kode', right_on='kode')
        
        page_merged['valid'] = pd.to_datetime(page_merged['valid'], unit='s').dt.strftime('%d/%m/%Y')
        
        kolomTampil = ["nama", "harga", "valid"]
        print("\n=== Subscription Aktif ===")
        print(f"{page_merged[kolomTampil].to_markdown(index=False)}\n")
        
        userInput = input("Ketik 'lanjut' untuk melihat data berikutnya\nKetik 'keluar' atau apa saja untuk keluar: ").lower()
        
        if userInput == "lanjut":
            startPage += perPage
        else:
            print()
            break