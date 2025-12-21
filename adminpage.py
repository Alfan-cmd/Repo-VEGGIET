import pandas as pd
df= pd.read_csv("daftar_veggiet.csv")
subs = pd.read_csv("daftar_subs.csv")

def tambah_barang():
    inputuser = input("Yakin/Tidak:").lower()
    if inputuser == "yakin":
        jumlah = int(input("Masukkan Jumlah data yang ingin dimasukkan: "))
        for i in range(1, jumlah + 1):
            print(f"--- data Veggiet ke {i} ---")
            produk = input("Nama: ").lower()
            kode = input("Kode makanan : ").upper()
            stok = int(input("Jumlah Stok: "))
            harga = int(input("Harga : "))
            kategori = input("Kategori : ")
            
            df.loc[len(df)] = [kode, produk, stok, harga, kategori] #untuk memasukkan data
            df.to_csv("daftar_veggiet.csv", index=False)
        print(f"Hasil: \n {df}")
    else:
        return
    
def tambah_subs():
    inputuser = input("Yakin/Tidak: ").lower()
    if inputuser == "yakin":
        jumlah = int(input("Masukkan Jumlah data yang ingin dimasukkan: "))
        for i in range(1, jumlah + 1):
            print(f"--- data Subs ke {i} ---")
            while True:
                produk = input("Nama: ").lower()
                if produk in subs['nama'].str.lower().values:
                    print("Produk sudah ada di daftar. Silakan masukkan nama produk yang lain.")
                else:
                    break
            kode = f"SUB{i:03d}"
            if len(subs) == 0:
                kode = "SUB001"
            else:
                last_code = subs.iloc[-1]['kode']
                last_number = int(last_code[3:]) + 1
                kode = f"SUB{last_number:03d}"
            harga = int(input("Harga : "))
            kategori = input("Kategori : ")

            produk = " ".join(word.capitalize() for word in produk.split())

            subs.loc[len(subs)] = [kode, produk, harga, kategori]
            subs.to_csv("daftar_subs.csv", index=False)
        print(f"Hasil: \n {subs}")
    else:
        return
