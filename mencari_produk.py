import pandas as mp
from transaksi import beli_sayuran, load_lagi
from transaksi import beli_sayuran

dfProduk = mp.read_csv("daftar_veggiet.csv")
open_file = mp.read_csv('daftar_veggiet.csv')
open_file_2 = mp.read_csv('akun_user.csv')


def mencariproduk(role_pengakses): #PAKE YANG INI BIAR LANGSUNG NYARI DI DATABASE
    role = str(role_pengakses)
    pilihanuser = input("Masukkan Nama Sayur/Buah/Biji/Olahan : ").lower()
    if role == "1":
        kolomTampil = ["nama","harga","kategori"]
    elif role == "2":
        kolomTampil = ["nama","stok","harga","kategori"]
    printlah(pilihanuser,kolomTampil,"nama") #PAKE YANG INI BIAR LANGSUNG NYARI DI DATABASE



def printlah(nama,listberisiapaaja,tampilin_apah):
    open_file = load_lagi()
    cari_produk = open_file[(open_file[f'{tampilin_apah}'] == nama)]
def mencariproduk(): #PAKE YANG INI BIAR LANGSUNG NYARI DI DATABASE
    pilihanuser = input("\nMasukkan Nama Sayur/Buah/Biji/Olahan : ").lower()
    kolomTampil = ["nama","stok","harga"]
    printlah(pilihanuser,kolomTampil) #PAKE YANG INI BIAR LANGSUNG NYARI DI DATABASE

def printlah(nama,listberisiapaaja):
    cari_produk = open_file[(open_file['nama'] == nama)]
    if cari_produk.empty:
        print("\nTidak dapat ditemukan :<")
    elif cari_produk.empty == False:
        print("\n", cari_produk.to_string(index= False)) #PAKE YANG INI BIAR LANGSUNG NYARI DI DATABASE
def cariKategori():
    print("=== Kategori Produk ===")
    print("Sayur")
    print("Buah")
    print("Kacang")
    print("Biji-Bijian")
    print("Olahan")
    print("Jamur")
    kategoriuser = input("Masukkan Kategori yang ingin dicari: ").lower()
    kategori_produk = open_file[(open_file['kategori'] == kategoriuser )]
    if kategori_produk.empty:
        print("\n Kategori yang dicari tidak ditemukan")
    elif kategori_produk.empty == False:
        print("\n",kategori_produk.to_string(index = False))
        print("\n", cari_produk[listberisiapaaja].to_markdown(index=False))

def menambah_stok():
    open_file = load_lagi()
    while True:
        kolomtampil = ["nama","stok"]
        nama_barang = input("Masukkan nama barang : ").lower()
        if open_file.loc[open_file["nama"]==nama_barang].empty == True:
            print("Barang ini tidak tersedia")
        elif open_file.loc[open_file["nama"]==nama_barang].empty == False:
            printlah(nama_barang,kolomtampil,'nama')
            inputubahstok = input("(Menambah/Mengurangi):").lower()
            if inputubahstok == "menambah":
                while True:
                    jumlah_ditambah = input("Masukkan mau menambah berapa stok : ")
                    if jumlah_ditambah.isdigit():
                        jumlah_ditambah = int(jumlah_ditambah)
                        if jumlah_ditambah >= 0:
                            open_file.loc[open_file['nama'] == nama_barang, 'stok'] += jumlah_ditambah
                            open_file.to_csv("daftar_veggiet.csv", index=False)
                            break
                        else:
                            print("Mohon masukkan angka positif :>")
                    else:
                        print("Mohon masukkan angka numerik :>")
                print("Sudah ditambah nih :>")
                printlah(nama_barang,kolomtampil,'nama')
                break

def menambah_stok():
    while True:
        kolomtampil = ["nama","stok"]
        nama_barang = input("Masukkan nama barang : ").lower()
        if open_file.loc[open_file["nama"]==nama_barang].empty == True:
            print("Barang ini tidak tersedia")
        elif open_file.loc[open_file["nama"]==nama_barang].empty == False:
            printlah(nama_barang,kolomtampil)
            inputubahstok = input("(Menambah/Mengurangi):").lower()
            if inputubahstok == "menambah":
                while True:
                    jumlah_ditambah = input("Masukkan mau menambah berapa stok : ")
                    if jumlah_ditambah.isdigit():
                        jumlah_ditambah = int(jumlah_ditambah)
                        if jumlah_ditambah >= 0:
                            open_file.loc[open_file['nama'] == nama_barang, 'stok'] += jumlah_ditambah
                            open_file.to_csv("daftar_veggiet.csv", index=False)
                            break
                        else:
                            print("Mohon masukkan angka positif :>")
                    else:
                        print("Mohon masukkan angka numerik :>")
                print("Sudah ditambah nih :>")
                printlah(nama_barang,kolomtampil)
                break
            
            elif inputubahstok == "mengurangi":
                jumlah_dikurang = input("Masukan mau mengurangi berapa stok:")
                if jumlah_dikurang.isdigit():
                    jumlah_dikurang = int(jumlah_dikurang)
                    if jumlah_dikurang >= 0:
                        open_file.loc[open_file["nama"] == nama_barang, 'stok'] -= jumlah_dikurang
                        open_file.to_csv("daftar_veggiet.csv", index=False)
                    else:
                        print("Mohon masukkan angka positif :>")
                else:
                    print("Mohon masukkan angka numerik :>")
                printlah(nama_barang,kolomtampil)
                break

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
    dfProduk = load_lagi()
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

def cariKategori():
    open_file = load_lagi()
    kolomtampil = ["nama","stok","harga","kategori"]
    while True:
        print("=== Kategori Produk ===")
        print("Sayur")
        print("Buah")
        print("Kacang")
        print("Biji-Bijian")
        print("Jamur")
        kategoriuser = input("Masukkan Kategori yang ingin dicari: ").lower()
        kategori_produk = open_file[(open_file['kategori'] == kategoriuser )]
        if kategori_produk.empty:
            print("\n Kategori yang dicari tidak ditemukan")
        elif kategori_produk.empty == False:
            printlah(kategoriuser,kolomtampil,"kategori")
            break
