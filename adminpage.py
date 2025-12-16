import pandas as pd
df= pd.read_csv("daftar_veggiet.csv")

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
