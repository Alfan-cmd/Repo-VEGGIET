user = []
admin = [{'username' : 'adminsehat', 'password' : 'veggiet123'}]

homepage = True
quit = False
admintoggle = True

def cekuser(x):
    for i in user:
        if i['username'].lower() == x.lower():
            return True
    return False
                
def adminlogin(x,y):
    for i in admin:
        if i['username'].lower() == x and i['password'] == y:
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
       
def logging():
    global homepage, quit, admintoggle
    while True:

        print("\n=== LOGIN/SIGN UP ==")
        print("1. Sign Up")
        print("2. Login")
        print("3. Quit")
        input1 = input("Pilih Opsi:")
        
        if input1 == "1":
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
                
        elif input1 == "2":
            print("\n=== LOGIN ===")
        
            nameinput = input("Username:")
            passinput = input("Password:")
            if login(nameinput, passinput):
                print("\nSelamat Anda Berhasil Login!")
                homepage = False
                return
            elif adminlogin(nameinput,passinput):
                print("\nSelamat Datang di Menu Admin!")
                admintoggle = False
            
            else:
                print("Password Atau Username Salah!")
            break
        
        elif input1 == "3":
            quit = True
            return         
        else:
            print("\nOpsi Tidak Tersedia")
    
def main_page():
    global homepage
    if not homepage:
        while True:
            print("\n=== Homepage ===")
            print("1.Subscription")
            print("2.Status")
            print("3.Log Out")
            input2 = input("Pilih Opsi:")
            
            if input2 == "1":
                break
            
            elif input2 == "2":
                break
            
            elif input2 == "3":
                homepage = True
                return

            else:
                print("Opsi Tidak Tersedia")
                
def adminmenu():
    while True:
        print("\n=== Menu Admin ===")
        print("1.Cek Barang")
        print("2.Menambah Barang")
        print("3.Log Out")
        
        inputadmin1 = input("Pilih Opsi:")
        
        if inputadmin1 == "1":
            pass
        
        else:
            admintoggle = True
            return
        
while True:
    
    if not homepage:
        main_page()
    elif quit == True:
        print("See You Next Time!")
        break   
    elif not admintoggle:
        adminmenu()
    
    logging()    