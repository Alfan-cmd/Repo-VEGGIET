#Import Library
import pandas as pd

#Import File
from profiluser import profil
from adminpage import tambah_barang
from mencari_produk import menambah_stok, mencariproduk, tampilkan_sayuran
from transaksi import beli_sayuran, pesan_sayuran, lihat_cart, checkout
from subs import menu_subs

#Variable
def load_user():
    return pd.read_csv("akun_user.csv")

def save_user(df):
    return df_user.to_csv("akun_user.csv", index=False)
    
df_user = load_user()
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
        print()

        if pilihan == "1":
            signup()

        elif pilihan == "2":
            username, role = login()

            if username:
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

def signup():
    global df_user
    
    print("=== Registrasi User Baru ===")
    
    while True:
        usernameInput = input("Masukkan Username: ")
        
        if usernameInput.lower() in df_user["username"].str.lower().values:
            print("Username sudah digunakan")
            print()
            continue
        break
        
    passwordInput = input("Masukkan Password:")
    alamatInput = input("Masukan Alamat:")
    notelpInput = input("Masukan Telp:")
    
    userBaru = {
        "username": usernameInput,
        "password": passwordInput,
        "role": 1,
        "alamat": alamatInput,
        "nama_pengguna": "Belum di isi",
        "no_telephone": notelpInput
    }
    
    df_user = pd.concat([df_user, pd.DataFrame([userBaru])], ignore_index=True)
    
    save_user(df_user)
    
    df_user = load_user()
    
    print()
    print("Registrasi berhasil, silahkan login.")
    print()

#Procedure Login
def login():
    while True:

        print("=== Silahkan Login ===")
        
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
    global df_user
    print(f"\nSelamat datang {current}!")
    
    while True:
        print("\n=== Homepage ===")
        print("1. Profil")
        print("2. Cari Produk")
        print("3. Daftar Produk")
        print("4. Pesan")
        print("5. Lihat Keranjang")
        print("6. Checkout")
        print("7. Subscription")
        print("8. Log Out")

        pilih = input("Pilih Opsi: ")
        print()

        if pilih == "1":
            profil(current,df_user)
        elif pilih == "2":
            mencariproduk()
        elif pilih == "3":
            tampilkan_sayuran()
        elif pilih == "4":
            pesan_sayuran(current)
        elif pilih == "5":
            lihat_cart(current)
        elif pilih == "6":
            checkout(current)
        elif pilih == "7":
            menu_subs(current)
        elif pilih == "8":
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
        print("3. Perbarui Stok")
        print("4. Search Produk")
        print("5. Subscription")
        print("6. Log Out")

        pilih = input("Pilih Opsi: ")

        if pilih == "1":
            tampilkan_sayuran()
        elif pilih == "2":
            tambah_barang()
        elif pilih == "3":
            menambah_stok()
        elif pilih == "4":
            mencariproduk()
        elif pilih == "5":
            menu_subs(current)
        elif pilih == "6":
            print("Logout admin...\n")
            return
        else:
            print("Opsi tidak tersedia")

'''
def append_kefile():
    for i in user:
        ember_ke_file = [i['username'],i['password'],i['alamat'],
                         i['nama_pengguna'],i['no_telephone']]
    with open("akun_user.csv","a") as file_akun:
        if len(user) != 0:
            hasil = ','.join(ember_ke_file)
            file_akun.write(f"\n{hasil}")
'''
while True:
    if not menulogin():
        break
