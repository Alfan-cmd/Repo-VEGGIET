import pandas as pd

#Membaca data CSV
df = pd.read_csv("daftar_veggiet.csv")


#Function beli
def beli_sayuran():
    print()
    print("=== Beli Sayuran ===")
    #Input Nama item
    namaBarang = input("Masukkan nama Sayuran yang ingin dibeli: ").lower()
    
    #Pengecekan nama item
    if namaBarang not in df['nama'].values:
        print("Sayuran tidak ditemukan")
        return
    
    #Input jumlah beli user
    jumlahBeli = int(input("Masukkan jumlah yang ingin dibeli: "))
    item =  df[df["nama"] == namaBarang].iloc[0]
    
    #Pengecekan apakah jumlah beli melebihi stok
    if jumlahBeli > item['stok']:
        print("Stok tidak cukup")
        return
    
    #Menghitung harga yang dibeli
    total = jumlahBeli * item['harga']
    print()
    print(f"Total harga: RP{total:,}".replace(",","."))
    
    #Pengurangan stok dengan jumlah yang dibeli
    df.loc[df['nama'] == namaBarang,'stok'] -= jumlahBeli
    print("Pembelian berhasil")
        

#Procedure Show Menu
def tampilkan_sayuran():
    #Banyaknya data per halaman
    perPage = 5
    startPage = 0
    
    while True:
        
        #Penutup Page
        endPage = startPage + perPage
        page = df.iloc[startPage:endPage]
        if page.empty:
            print("Tidak ada sayuran lagi untuk ditampilkan")
            break
        
        #Print data
        print("=== Daftar Sayuran yang dijual ===")
        print(page.to_markdown(index=False))
        print()
        
        #Input User
        userInput = input("Ketik 'lanjut' untuk melihat data berikutnya\nKetik 'beli' untuk membeli sayuran\nKetik 'keluar' atau apa saja untuk keluar: ").lower()
        
        #Pengecekan input user
        if userInput == "lanjut":
            #Geser ke page selanjutnya
            startPage += perPage
        elif userInput == "beli":
            #Memanggil fungsi beli
            beli_sayuran()
            break
        else:
            print("Terima Kasih")
            break
       


# tampilkan_sayuran()
