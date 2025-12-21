import pandas as mp
from transaksi import beli_sayuran


dfProduk = mp.read_csv("daftar_veggiet.csv")
open_file = mp.read_csv('daftar_veggiet.csv')
open_file_2 = mp.read_csv('akun_user.csv')

def mencariproduk(): #PAKE YANG INI BIAR LANGSUNG NYARI DI DATABASE
    pilihanuser = input("\nMasukkan Nama Sayur/Buah/Biji/Olahan : ").lower()
    cari_produk = open_file[(open_file['nama'] == pilihanuser)]
    if cari_produk.empty:
        print("\nItem tidak ditemukan :<")
    elif cari_produk.empty == False:
        print("\n", cari_produk.to_string(index= False)) #PAKE YANG INI BIAR LANGSUNG NYARI DI DATABASE

def menambah_stok():
    nama_barang = input("Masukkan nama barang : ").lower()
    jumlah_ditambah = int(input("Masukkan mau menambah berapa stok : "))
    open_file.loc[open_file['nama'] == nama_barang, 'stok'] += jumlah_ditambah
    open_file.to_csv("daftar_veggiet.csv", index=False)


"""
def binarySearch(sorted_list, target_barang):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        barang = sorted_list[mid]["nama"].lower()

        if barang == target_barang:
            return mid
        elif barang < target_barang:
            left = mid + 1
        else:
            right = mid - 1
    return -1
"""

def tampilkan_sayuran():
    #Banyaknya data per halaman
    perPage = 5
    startPage = 0
    
    while True:
        
        #Penutup Page
        endPage = startPage + perPage
        page = dfProduk.iloc[startPage:endPage]
        if page.empty:
            print("Tidak ada sayuran lagi untuk ditampilkan")
            break
        
        #Setting tampilan
        kolomTampil = ["nama","stok","harga"]
        
        #Print data
        print()
        print("=== Daftar Sayuran yang dijual ===")
        print(page[kolomTampil].to_markdown(index=False))
        print()
        
        #Input User
        userInput = input("Ketik 'lanjut' untuk melihat data berikutnya\nKetik 'keluar' atau apa saja untuk keluar: ").lower()
        
        #Pengecekan input user
        if userInput == "lanjut":
            #Geser ke page selanjutnya
            startPage += perPage
        else:
            print("Terima Kasih")
            break
