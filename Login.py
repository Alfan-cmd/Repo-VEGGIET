user = []
homepage = True

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
            
    
# masuk=True
while True:

    print("=== LOGIN/SIGN UP ==")
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
        while True:
            nameinput = input("Username:")
            passinput = input("Password:")
            if login(nameinput, passinput):
                print("Selamat Anda Berhasil Login")
                homepage = False
                break
            else:
                print("Password Atau Username Salah!")
    
    elif input1 == "3":
        break
    
if not homepage:
    while True:
        pass
    
else:
    print("See You Next Time :)")