user = []
admin = [
    {
        'username' : 'adminveggiet',
        'password' : 'sehat321',
        'alamat' : 'Belum di Isi'
    }
]
homepage = True
adminmenu = True
def cekuser(x):
    for i in user:
        if i['username'].lower() == x.lower():
            return True
    return False
                
def adminlogin(username,password):
    for i in admin:
        if i['username'].lower() == username and i['password'] == password:
            return True
    return False

def signup(username,password):
    user.append({
        'username' : username,
        'password' : password,
        'alamat' : 'Belum di Isi',
        'nama_pengguna' : 'Belum di isi',
        'no_telephone' : 'Belum di Isi'
        })
    return user
    
def login(username,password):
    for i in user:
        if i['username'].lower() == username.lower() and i['password'] == password:
            return True
    return False
            
def adminlogin(x,y):
    for i in admin:
        if i['username'].lower() == "adminveggiet" and i['password'] == 'sehat321':
             return menuadmin()
    return False
# masuk=True
def menulogin():
    while True:

        print("=== LOGIN/SIGN UP ==")
        print("1. Sign Up")
        print("2. Login")
        print("3. Quit")
        input1 = input("Pilih Opsi:")
        
        if input1 == "1":
            singup()
        elif input1 == "2":
            loginmenu()
        elif input1 == "3":
            break

def singup():
    print("\n=== SIGN UP ===")
    while True:
        SUname = input("Masukan Username:")
        SUpass = input("Masukan Password:")
        
        if cekuser(SUname):
            print("Username Telah Dipakai!")
        else:
            signup(SUname,SUpass)
            print("Selamat Akun Anda Berhasil Dibuat!")
            break      
                
            
def loginmenu():
    print("\n=== LOGIN ===")
    while True:
        nameinput = input("Username:")
        passinput = input("Password:")
        if adminlogin(nameinput,passinput) != False:
            if login(nameinput, passinput):
                print("=======Selamat Anda Berhasil Login=======")
                menu(nameinput,passinput)
            menuadmin(nameinput)
            break
            
            menu()
            break
        else:
            print("Password Atau Username Salah!")

def menu(nameinput,passinput):
    while True:
        print(f"Halo {nameinput}!")
        print("Selamat Datang Di Aplikasi Pemesanan Sayur Segar!")

        while True:

            print("1.Menu Profil\n2.Keluar")
            inputan_user_dimenu = input("Silahkan Dipilih Syng : ")

            if inputan_user_dimenu == "1":
                profil(nameinput)

            elif inputan_user_dimenu == "2":
                menulogin()

            
    
def alamat(nameinput):
    for i in user:
        if i['username'] == nameinput:
            i[f"alamat"] = input("===================\nMasukkan alamat anda:")
            print("=====================\nAlamat ditambahkan!\n===================")

def nama(nameinput):
    for i in user:
        if i['username'] == nameinput:
            i[f"nama_pengguna"] = input("===================\nMasukkan nama anda: ")
            print("=============\nNama ditambahkan!\n=============")

def nohp(nameinput):
    for i in user:
        if i['username'] == nameinput:
            i[f"no_telephone"] = input("===================\nMasukkan Nomor Telephone anda: ")
            print("============\nNo HP ditambahkan!\n============")




def menuadmin():
    while True:
        print("Selamat datang di Menu admin")
        break

def print_profil(nameinput):
    for i in user:
        if i['username'] == nameinput:
            print(f"1.Nama : {i['nama_pengguna']}")
            print(f"2.Alamat :{i['alamat']} ")
            print(f"3.No Telephone :{i['no_telephone']}\n")

def profil(nameinput):
    print(f"\nSelamat datang di menu Profil User!")
    while True:
        print("== Profil anda saat ini ==")
        print_profil(nameinput)
        gantiortidak = input("1.Ganti\n2.Back\nPilih: ")
        if gantiortidak == "1":
            while True:
                inputan_user_menu_profil = input("Mau Ganti yang mana? (1-3)\nPilih: ")

                if inputan_user_menu_profil == "1":
                    nama(nameinput)
                    break

                elif inputan_user_menu_profil == "2":
                    alamat(nameinput)
                    break

                elif inputan_user_menu_profil == "3":
                    nohp(nameinput)
                    break
                else:
                    print("Masukkan angka valid")

        elif gantiortidak == "2":
            break

            



menulogin()

print("See You Next Time :)")
