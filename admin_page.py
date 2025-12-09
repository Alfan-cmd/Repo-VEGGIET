import pandas as pd
df= pd.read_csv("daftar_veggiet.csv")

def tambah_barang():
    jumlah = int(input("Masukkan Jumlah Jenis Barang: "))
    for i in range(1, jumlah + 1):
        print(f"--- data barang ke {i} ---")
        produk = input("Nama: ")
        kode = input("Kode makanan : ")
        stok = int(input("Jumlah Stok: "))
        
        df.loc[len(df)] = [kode, produk, stok]
    print(f"Hasil: \n {df}")
tambah_barang()
#halooo