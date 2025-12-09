import pandas as pd

# Nama file CSV
df = 'daftar_veggiet.csv'

def tampilkan_tabel_produk(df):
    pass

def main():
    # 1. Load Data

    keranjang = [] # List untuk menyimpan item belanja
    total_bayar = 0 

    print("Pembayaran Veggiet")

    while True:
        #Tampilkan Menu dari Dataframe
        tampilkan_tabel_produk(df)
        
        # 3. Form Input User
        input_user = input("Masukkan ID Produk (atau ketik 'b' untuk bayar): ").lower()

        if input_user == 'b':
            break
        
        # Validasi Input (Pastikan ID berupa angka)
        if not input_user.isdigit():
            print("Harap masukkan ID berupa angka!")
            continue
        
        id_dipilih = int(input_user)


main()