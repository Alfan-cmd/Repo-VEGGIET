import pandas as pd

df_user = pd.read_csv("akun_user.csv")

def print_profil(username):
    user = df_user[df_user["username"] == username].iloc[0]

    print()
    print(f"1. Nama        : {user['nama_pengguna']}")
    print(f"2. Alamat        : {user['alamat']}")
    print(f"3. No Telephone  : {user['no_telephone']}\n")


def profil(username):
    global df_user

    print("\nSelamat datang di menu Profil User!")

    while True:
        print("\n== Profil anda saat ini ==")
        print_profil(username)

        ganti = input("1. Ganti\n2. Back\nPilih: ")

        if ganti == "1":
            pilih = input("Mau ganti yang mana? (1-3)\nPilih: ")

            if pilih == "1":
                df_user.loc[df_user["username"] == username, "nama_pengguna"] = input("Masukkan nama: ")

            elif pilih == "2":
                df_user.loc[df_user["username"] == username, "alamat"] = input("Masukkan alamat: ")

            elif pilih == "3":
                df_user.loc[df_user["username"] == username, "no_telephone"] = input("Masukkan no HP: ")

            else:
                print("Pilihan tidak valid")
                continue

            df_user.to_csv("akun_user.csv", index=False)
            print("Data berhasil diperbarui!\n")

        elif ganti == "2":
            return
