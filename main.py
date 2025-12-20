#Import Library
import pandas as pd

#Import File
from profiluser import profil
from adminpage import tambah_barang
from mencari_produk import menambah_stok, mencariproduk, melihatbarang
from transaksi import beli_sayuran, tampilkan_sayuran

#Variable
df_user = pd.read_csv("akun_user.csv")
user = []
admin = [{'username' : 'adminsehat', 'password' : 'veggiet123'}]

homepage = True
quit = False
admintoggle = True
current = None
currentUser = None
currentRole = None
loop = True

def menulogin():
    while True:
        print("\n=== LOGIN / SIGN UP ===")
        print("1. Sign Up")
        print("2. Login")
        print("3. Quit")

        pilihan = input("Pilih Opsi: ")

        if pilihan == "1":
            signup()

        elif pilihan == "2":
            username, role = login()

            if username:
                print(f"\nSelamat datang {username}!\n")
                if role == 2:
                    adminmenu(username)
                else:
                    main_page(username)
            else:
                print("Username atau Password salah!")

        elif pilihan == "3":
            print("See You Next Time!")
            return False

        else:
            print("Opsi tidak tersedia")

 
# def cekuser(x):
#     for i in user:
#         if i['username'].lower() == x.lower():
#             return True
#     return False
                
# def adminlogin(x,y):
#     for i in admin:
#         if i['username'].lower() == x.lower() and i['password'] == y:
#             return True
#     return False

def signup():
    global df_user
    
    print("=== Registrasi User Baru ===")
    print()
    
    while True:
        usernameInput = input("Masukkan Username: ")
        
        if usernameInput in df_user["username"].values:
            print("Username sudah digunakan")
            print()
            continue
        break
        
    passwordInput = input("Masukkan Password: ")
    
    userBaru = {
        "username": usernameInput,
        "password": passwordInput,
        "role": 1,
        "alamat": "Belum di Isi",
        "nama_pengguna": "Belum di isi",
        "no_telephone": "Belum di Isi"
    }
    
    df_user = pd.concat([df_user, pd.DataFrame([userBaru])], ignore_index=True)
    
    df_user.to_csv("akun_user.csv", index=False)
    
    print()
    print("Registrasi berhasil, silahkan login.")
    print()

#Procedure Login
def login():
    while True:

        print("=== Silahkan Login ===")
        print()
        
        #User menginput username dan password
        usernameInput = input("Masukkan Username: ")
        passwordInput = input("Masukkan Password: ")

        #Pengecekan apakah ada username dan password di dalam CSV seperti yang diinput oleh user
        user = df_user[
            (df_user["username"] == usernameInput) &
            (df_user["password"] == passwordInput)
        ]
        #Jika isi variable user itu tidak kosong maka akan mengecek role
        if not user.empty:
            role = int(user.iloc[0]["role"])
            return usernameInput, role
        else:
            return None, None
       

    
def main_page(current):
    print(f"Selamat Datang {current}!")

    while True:
        print("\n=== Homepage ===")
        print("1. Profile")
        print("2. Search")
        print("3. Catalog")
        print("4. Pesan")
        print("5. Log Out")

        pilih = input("Pilih Opsi: ")

        if pilih == "1":
            profil(current)
        elif pilih == "2":
            mencariproduk()
        elif pilih == "3":
            melihatbarang()
        elif pilih == "4":
            beli_sayuran()
        elif pilih == "5":
            print("Logout...\n")
            return
        else:
            print("Opsi tidak tersedia")

                
def adminmenu(current):
    print(f"Admin: {current}")

    while True:
        print("\n=== Menu Admin ===")
        print("1. Cek Barang")
        print("2. Tambah Barang")
        print("3. Tambah Stok")
        print("4. Search Produk")
        print("5. Log Out")

        pilih = input("Pilih Opsi: ")

        if pilih == "1":
            melihatbarang()
        elif pilih == "2":
            tambah_barang()
        elif pilih == "3":
            menambah_stok()
        elif pilih == "4":
            mencariproduk()
        elif pilih == "5":
            print("Logout admin...\n")
            return
        else:
            print("Opsi tidak tersedia")
        
while True:
    if menulogin() == False:
        break