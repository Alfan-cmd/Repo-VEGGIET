import pandas as pd

#Membaca data CSV
df = pd.read_csv("daftar_veggiet.csv")
dfUser = pd.read_csv("akun_user.csv")
df_keranjang = pd.read_csv("keranjang.csv")


#Function beli
def beli_sayuran(username):
    global df
    global df_keranjang

    print("=== Beli Sayuran ===")

    # Input nama barang
    namaBarang = input("Masukkan nama Sayuran yang ingin dibeli: ").lower()
    print()
    
    # Cek barang
    if namaBarang not in df['nama'].values:
        print("Sayuran tidak ditemukan")
        return

    item = df[df["nama"] == namaBarang].iloc[0]

    # Input jumlah
    jumlahInput = input("Masukkan jumlah yang ingin dibeli: ")

    # Validasi harus angka
    if not jumlahInput.isdigit():
        print("Jumlah harus berupa angka")
        return

    jumlahBeli = int(jumlahInput)

    # Validasi tidak boleh nol / negatif
    if jumlahBeli <= 0:
        print("Jumlah harus lebih dari 0")
        return

    # Cek stok
    if jumlahBeli > item['stok']:
        print("Stok tidak cukup")
        return

    subtotal = jumlahBeli * item['harga']

    # Cek apakah barang sudah ada di keranjang user
    barangPembelian = (
        (df_keranjang["username"] == username) &
        (df_keranjang["kode"] == item["kode"])
    )

    if barangPembelian.any():
        # Update jumlah & subtotal
        df_keranjang.loc[barangPembelian, "jumlah"] += jumlahBeli
        df_keranjang.loc[barangPembelian, "subtotal"] += subtotal
    else:
        # Tambah baris baru
        data_baru = {
            "username": username,
            "kode": item["kode"],
            "nama": item["nama"],
            "harga": item["harga"],
            "jumlah": jumlahBeli,
            "subtotal": subtotal
        }
        df_keranjang = pd.concat(
            [df_keranjang, pd.DataFrame([data_baru])],
            ignore_index=True
        )

    # Simpan ke CSV
    df_keranjang.to_csv("keranjang.csv", index=False)

    print(f"\n {jumlahBeli} {item['nama'].upper()} berhasil ditambahkan ke keranjang")
    print(f"Subtotal: Rp{subtotal:,}".replace(",", "."))
    
#Procedure pesan sayur
def pesan_sayuran(username):
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
        
        #Setting tampilan
        kolomTampil = ["nama","stok","harga"]
        
        #Print data
        print()
        print("=== Daftar Sayuran yang dijual ===")
        print(page[kolomTampil].to_markdown(index=False))
        print()
        
        #Input User
        userInput = input("Ketik 'lanjut' untuk melihat data berikutnya\nKetik 'beli' untuk membeli sayuran\nKetik 'keluar' atau apa saja untuk keluar: ").lower()
        
        #Pengecekan input user
        if userInput == "lanjut":
            #Geser ke page selanjutnya
            startPage += perPage
        elif userInput == "beli":
            beli_sayuran(username)
        else:
            print("Terima Kasih")
            break


#Procedure Keranjang
def lihat_cart(username):
    keranjangUser = df_keranjang[df_keranjang["username"] == username]
    kolomTampil = ["nama","harga","jumlah","subtotal"]
    

    if keranjangUser.empty:
        print("Keranjang kosong")
    else:
        print("================ Keranjang =================")
        print(keranjangUser[kolomTampil].to_markdown(index=False))
        print(f"Total: {keranjangUser['subtotal'].sum()}")



#Checkout
def checkout(username):
    global df_keranjang, df

    cart_user = df_keranjang[df_keranjang["username"] == username]

    if cart_user.empty:
        print("Keranjang kosong")
        return

    for _, row in cart_user.iterrows():
        df.loc[df["kode"] == row["kode"], "stok"] -= row["jumlah"]

    df.to_csv("daftar_veggiet.csv", index=False)

    df_keranjang = df_keranjang[df_keranjang["username"] != username]
    df_keranjang.to_csv("cart.csv", index=False)

    print("Checkout berhasil!")

