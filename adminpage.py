import pandas as pd
from transaksi import load_lagi
dfawal= pd.read_csv("daftar_veggiet.csv")
subs = pd.read_csv("daftar_subs.csv")
df = load_lagi()


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
    
def hapus_barang():
    inputuser = input("Yakin ingin menghapus barang? (yakin/tidak): ").lower()
    
    if inputuser != "yakin":
        return

    print("\n=== Hapus Barang ===")
    print("1. Hapus berdasarkan KODE")
    print("2. Hapus berdasarkan NAMA")

    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        kode = input("Masukkan kode barang: ").upper()

        if kode not in df["kode"].values:
            print("Kode barang tidak ditemukan")
            return

        df.drop(df[df["kode"] == kode].index, inplace=True)
        df.to_csv("daftar_veggiet.csv", index=False)

        print(f"Barang dengan kode {kode} berhasil dihapus")

    elif pilihan == "2":
        nama = input("Masukkan nama barang: ").lower()

        if nama not in df["nama"].values:
            print("Nama barang tidak ditemukan")
            return

        df.drop(df[df["nama"] == nama].index, inplace=True)
        df.to_csv("daftar_veggiet.csv", index=False)

        print(f"Barang {nama.upper()} berhasil dihapus")

    else:
        print("Opsi tidak tersedia")
    
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
