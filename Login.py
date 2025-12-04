user = []
admin = [
    {
        'username' : 'adminveggiet',
        'password' : 'sehat321'
    }
]
homepage = True
adminmenu = True
def cekuser(x):
    for i in user:
        if i['username'].lower() != x:
                return True
    return False
                
def signup(x,y):
    user.append({
        'username' : x,
        'password' : y
        })
    return user
    
def login(x,y):
    for i in user:
        if i['username'].lower() == x.lower() and i['password'] == y:
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
                print("Selamat Anda Berhasil Login")
                menu()
            menuadmin()
            break
            
            menu()
            break
        else:
            print("Password Atau Username Salah!")

def menu(nameinput):
    while True:
        print(f"Halo {nameinput}")
        break
    

def menuadmin():
    while True:
        print("LOop")
        break

menulogin()

print("See You Next Time :)")