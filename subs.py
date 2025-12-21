import pandas as pd

from adminpage import tambah_subs
import time

def load():
    user = pd.read_csv('akun_user.csv')
    subs = pd.read_csv('subs.csv')
    daftar_subs = pd.read_csv('daftar_subs.csv')
    return user, subs, daftar_subs

def menu_subs(current):
    user, _, _ = load()
    user_role = user[user['username'] == current]['role'].values[0]
    if user_role == 1:
        while True:
            print("\n=== Menu Subscription ===")
            print("1. Pesan Subscription")
            print("2. Subscription yang lagi aktif")
            print("3. Kembali")
            pilihan = input("Pilih Opsi: ")
            print()

            if int(pilihan) == 1:
                pesan_subs(current)
            elif int(pilihan) == 2:
                cek_subs(current)
            elif int(pilihan) == 3:
                return
            else:
                print("Opsi tidak tersedia\n")

    elif user_role == 2:
        while True:
            print("\n=== Menu Subscription ===")
            print("1. List Subscription")
            print("2. Tambah Subscription")
            print("3. Kembali")
            pilihan = input("Pilih Opsi: ")
            print()

            if int(pilihan) == 1:
                list_subs()
            elif int(pilihan) == 2:
                tambah_subs()
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
        
        #Setting tampilan
        kolomTampil = ["nama","harga"]
        print("\n=== Daftar Subscription yang ada ===")
        print(f"{page[kolomTampil].to_markdown(index=False)}\n")
        
        userInput = input("Ketik 'lanjut' untuk melihat data berikutnya\nKetik 'keluar' atau apa saja untuk keluar: ").lower()
        
        if userInput == "lanjut":
            startPage += perPage
        else:
            print()
            break

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
        
        #Setting tampilan
        kolomTampil = ["nama", "harga"]
        print("\n=== Daftar Subscription yang ada ===")
        page[kolomTampil].reset_index(drop=True, inplace=True)
        page_display = page[kolomTampil].copy()
        page_display.index += 1
        print(f"{page_display.to_markdown(index=True)}\n")
        
        userInput = input("Ketik 'lanjut' untuk melihat data berikutnya\nKetik nomor untuk membeli\nKetik 'keluar' atau apa saja untuk keluar: ").lower()
        
        if userInput == "lanjut":
            startPage += perPage
        elif userInput.isdigit():
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
                    subs_updated = pd.concat([subs, new_subs], ignore_index=True)
                    subs_updated.to_csv('subs.csv', index=False)
                    
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