def tampilkan_menu():
    print("\n--- MENU KAFE MAHASISWA---")
    print("1. Kopi Susu Gula Aren  - Rp 18.000")
    print("2. Americano            - Rp 15.000")
    print("3. Roti Bakar Coklat    - Rp 12.000")
    print("4. Mie Instan Telur     - Rp 10.000")
    print("5. Es Teh Manis         - Rp  5.000")
    print("---------------------------------")

def main():
    # Database harga sederhana menggunakan Dictionary
    harga_barang = {
        1: 18000,
        2: 15000,
        3: 12000,
        4: 10000,
        5: 5000
    }
    
    nama_barang = {
        1: "Kopi Susu",
        2: "Americano",
        3: "Roti Bakar",
        4: "Mie Instan",
        5: "Es Teh"
    }

    total_belanja = 0
    keranjang = [] # Menyimpan riwayat belanja

    print("Selamat datang di Sistem Pembayaran Sederhana")
    
    # Loop untuk memilih barang
    while True:
        tampilkan_menu()
        pilihan = input("Pilih nomor menu (atau ketik 'q' untuk bayar): ").lower()

        if pilihan == 'q':
            break
        
        # Validasi input agar tidak error jika user salah ketik
        if not pilihan.isdigit() or int(pilihan) not in harga_barang:
            print("⚠ Pilihan tidak valid, silakan coba lagi.")
            continue
        
        kode = int(pilihan)
        qty = int(input(f"Berapa banyak {nama_barang[kode]}? "))
        
        subtotal = harga_barang[kode] * qty
        total_belanja += subtotal
        
        # Menambahkan detail ke keranjang
        keranjang.append(f"{nama_barang[kode]} (x{qty}) - Rp {subtotal:,}")
        print(f"✔ {nama_barang[kode]} berhasil ditambahkan!")

    # Jika tidak ada yang dibeli
    if total_belanja == 0:
        print("Anda tidak membeli apa-apa. Terima kasih!")
        return

    # Proses Pembayaran
    print("\n" + "="*30)
    print(f"TOTAL YANG HARUS DIBAYAR: Rp {total_belanja:,}")
    print("="*30)

    while True:
        try:
            uang_bayar = int(input("Masukkan jumlah uang tunai: Rp "))
            if uang_bayar < total_belanja:
                kurang = total_belanja - uang_bayar
                print(f"⚠ Uang tidak cukup. Kurang Rp {kurang:,}")
            else:
                kembalian = uang_bayar - total_belanja
                break
        except ValueError:
            print("⚠ Masukkan angka yang valid tanpa titik/koma.")

    # Cetak Struk / Receipt
    print("\n" + "="*30)
    print("       STRUK PEMBAYARAN       ")
    print("="*30)
    for item in keranjang:
        print(item)
    print("-" * 30)
    print(f"Total     : Rp {total_belanja:,}")
    print(f"Tunai     : Rp {uang_bayar:,}")
    print(f"Kembalian : Rp {kembalian:,}")
    print("="*30)
    print(" Terima kasih, selamat belajar! ")
    print("="*30)

if __name__ == "__main__":
    main()