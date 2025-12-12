
def print_profil(nameinput, user):
    for i in user:
        if i['username'] == nameinput:
            print(f"\n1.Nama : {i['nama_pengguna']}")
            print(f"2.Alamat :{i['alamat']} ")
            print(f"3.No Telephone :{i['no_telephone']}\n")

def profil(nameinput, user):
    print(f"\nSelamat datang di menu Profil User!")
    while True:
        print("\n== Profil anda saat ini ==")
        print_profil(nameinput,user)
        gantiortidak = input("1.Ganti\n2.Back\nPilih: ")
        if gantiortidak == "1":
            while True:
                inputan_user_menu_profil = input("Mau Ganti yang mana? (1-3)\nPilih: ")

                if inputan_user_menu_profil == "1":
                    nama(nameinput,user)
                    break

                elif inputan_user_menu_profil == "2":
                    alamat(nameinput,user)
                    break

                elif inputan_user_menu_profil == "3":
                    nohp(nameinput,user)
                    break
                else:
                    print("Masukkan angka valid")

        elif gantiortidak == "2":
            break
        
def alamat(nameinput,user):
    for i in user:
        if i['username'] == nameinput:
            i[f"alamat"] = input("===================\nMasukkan alamat anda:")
            print("=====================\nAlamat ditambahkan!\n===================")

def nama(nameinput,user):
    for i in user:
        if i['username'] == nameinput:
            i[f"nama_pengguna"] = input("===================\nMasukkan nama anda: ")
            print("=============\nNama ditambahkan!\n=============")

def nohp(nameinput,user):
    for i in user:
        if i['username'] == nameinput:
            i[f"no_telephone"] = input("===================\nMasukkan Nomor Telephone anda: ")
            print("============\nNo HP ditambahkan!\n============")