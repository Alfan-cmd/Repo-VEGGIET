import pandas as pd
df= pd.read_csv("daftar_veggiet.csv")

def tambah_barang():
    jumlah = int(input("Masukkan Jumlah data yang ingin dimasukkan: "))
    for i in range(1, jumlah + 1):
        print(f"--- daata Veggiet ke {i} ---")
        produk = input("Nama: ")
        kode = input("Kode makanan : ")
        stok = int(input("Jumlah Stok: "))
        harga = int(input("Harga : "))
        kategori = input("Kategori : ")

        
        df.loc[len(df)] = [kode, produk, stok, harga, kategori] #untuk memasukkan data
        df.to_csv("daftar_veggiet.csv", index=False)
    print(f"Hasil: \n {df}")
tambah_barang()