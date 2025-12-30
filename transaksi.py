import pandas as pd
import random
#Membaca data CSV
dfawal = pd.read_csv("daftar_veggiet.csv")
dfUser = pd.read_csv("akun_user.csv")
df_keranjang = pd.read_csv("keranjang.csv")
dfcart = pd.read_csv("cart.csv")

def load_lagi():
    return pd.read_csv("daftar_veggiet.csv")

def load_cart():
    return pd.read_csv("cart.csv")

#Function beli
def beli_sayuran(username):
    global df
    global df_keranjang
    global dfawal
    df = load_lagi()
    print("=== Beli Sayuran ===")

    # Input nama barang
    namaBarang = input("Masukkan nama Sayuran yang ingin dimasukkan: ").lower()
    print()
    
    # Cek barang
    if namaBarang not in df['nama'].values:
        print("Sayuran tidak ditemukan")
        return

    item = df[df["nama"] == namaBarang].iloc[0]
    namapengguna = dfUser[dfUser["username"] == username].iloc[0]

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
            "subtotal": subtotal,
            "status" : "Belum dikirim",
            "nama_pengguna": namapengguna["nama_pengguna"]
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
    df = load_lagi()
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
        userInput = input("Ketik 'lanjut' untuk melihat data berikutnya\nKetik 'keranjang' untuk memasukkan item ke keranjang\nKetik 'keluar' atau apa saja untuk keluar: ").lower()
        
        #Pengecekan input user
        if userInput == "lanjut":
            #Geser ke page selanjutnya
            startPage += perPage
        elif userInput == "keranjang":
            beli_sayuran(username)
        elif userInput == "keluar":
            print("Terima Kasih")
            break
        else:
            print("Opsi tidak tersedia")
            


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
    dfcart = load_cart()
    cart_user = df_keranjang[df_keranjang["username"] == username]
    kolomtampil = ["nama","harga","jumlah","subtotal"]

    if cart_user.empty:
        print("Keranjang kosong")
        return
    
    elif cart_user.empty == False:
        while True:

            print("==========Mau checkout yang mana?==========")
            page_display = cart_user[kolomtampil].reset_index(drop = True)
            page_display.index +=1
            print(page_display[["nama","harga","jumlah","subtotal"]].to_markdown(index = True))

            inputancheckout = input("Ketik angka barang yang ingin di checkout\nketik enter untuk keluar...\n Pilih :")
            
            if inputancheckout.isdigit():
                nomor = int(inputancheckout) - 1

                if 0 <= nomor < len(cart_user): #username,kode,nama,harga,jumlah,subtotal,status,nama_pengguna
                    username,kode,nama,harga,jumlah,subtotal,nama_pengguna = cart_user.iloc[nomor]['username'], cart_user.iloc[nomor]['kode'],cart_user.iloc[nomor]['nama'], cart_user.iloc[nomor]['harga'], cart_user.iloc[nomor]['jumlah'], cart_user.iloc[nomor]['subtotal'], cart_user.iloc[nomor]['nama_pengguna']
                    check = input(f"Apakah kamu ingin membeli '{nama}'? (Ya/Tidak) : ").lower()

                    if check == "ya":
                        # Masukkin ke database
                        while True:
                            metode_pembayaran = input("Pilih Metode Pembayaran:\n1. QRIS\n2. Apple Pay\n3. Master Card\nPilih : ")
                            if metode_pembayaran == "1":
                                metode = "QRIS"
                                break
                            elif metode_pembayaran == "2":
                                metode = "Apple Pay"
                                break
                            elif metode_pembayaran == "3":
                                metode = "Master Card"
                                break
                            else:
                                print("Masukkan Pilihan Yang Tepat :>")
                        
                        id_pesanan = id_pesanann(dfcart)
                        id_pembayaran = id_pembayarann(dfcart)

                        new_subs = pd.DataFrame({
                            'username': [username],
                            'kode': [kode],
                            'nama': [nama],
                            'harga' : [harga],
                            'jumlah': [jumlah],
                            'subtotal': [subtotal],
                            'status': "Belum dikirim",
                            'nama_pengguna' : [nama_pengguna],
                            'metode_pembayaran' : [metode],
                            'id_pembayaran': [id_pembayaran],
                            'id_pesanan' : [id_pesanan]

                        })

                        dfcart = pd.concat([dfcart, new_subs], ignore_index=True) #concat, itu untuk menambah baris.
                                                                                        #anggap aja subs yang merupakan data lama, ditambah newsubs yang merupakan databaru.
                        dfcart.to_csv('cart.csv',index=False) #Setelah itu append deh ke csv pake to_csv(kayak nge stemple ulang datanya)

                        for _,row in cart_user.iterrows():
                            dfawal.loc[dfawal["kode"] == row["kode"], "stok"] -= row["jumlah"]
                        dfawal.to_csv("daftar_veggiet.csv", index=False)

                        df_keranjang = df_keranjang[df_keranjang['nama'] != nama] #Update keranjang dengan index barang yang dipilih hilang
                        df_keranjang.to_csv("keranjang.csv", index = False) #Update/dikembalikan ke csv

                        print(f"Berhasil melakukan checkout '{nama}'")
                        break
                    else:
                        continue
                else:
                    print("Nomor tidak valid")
            elif inputancheckout == "keluar":
                print()
                break

def invoice(username):
    invoice_cart = load_cart()
    invoice = invoice_cart[(invoice_cart[f'username'] == username)]
    print(f"{invoice[["username","nama_pengguna","metode_pembayaran","subtotal","id_pembayaran"]].to_markdown(index = False)}")

def id_pesanann(csv):
    while True:
        angka = random.randint(100000,999999)
        id = (f"#{angka}")
        if csv[csv['id_pesanan'] == id].empty:
            return id
        else:
            print()

def id_pembayarann(csv):
    while True:
        angka = random.randint(100000,999999)
        id = (f"${angka}")
        if csv[csv['id_pembayaran'] == id].empty:
            return id
        else:
            print()
            continue