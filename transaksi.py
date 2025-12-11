import pandas as pd

#Membaca data CSV
df = pd.read_csv("daftar_veggiet.csv")


def tampilkan_menu():
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
        userInput = input("Ketik 'lanjut' untuk melihat data berikutnya (atau apa saja untuk berhenti): ").lower()
        
        #Pengecekan input user
        if userInput != "lanjut":
            print("\nTerima kasih!")
            break
       
        #Geser ke page selanjutnya
        startPage += perPage
        
tampilkan_menu()
