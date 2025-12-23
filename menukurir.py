import pandas as pd
from profiluser import profil
from adminpage import tambah_barang
from mencari_produk import menambah_stok, mencariproduk, tampilkan_sayuran,printlah
from transaksi import beli_sayuran, pesan_sayuran, lihat_cart, checkout
from subs import menu_subs

df_keranjang = pd.read_csv("keranjang.csv")
df_cart = pd.read_csv("cart.csv")
open_file_2 = pd.read_csv('akun_user.csv')

def pesanan_satuan():
    print("========Pesanan saat ini==========")
    pesanan = pd.merge(df_keranjang[["username","nama","jumlah","subtotal","status"]],open_file_2[["username","alamat"]], on="username")
    print(pesanan.to_markdown(index = False))


def update_status():
    username_input = input("Masukkan username pesanan yang ingin diupdate: ")
    status_baru = input("Masukkan status baru (Menunggu kurir / Dikirim / Selesai): ")

    ditemukan = False
    for i in range(len(df_keranjang)):
        if df_keranjang.loc[i, "username"] == username_input:
            df_keranjang.loc[i, "status"] = status_baru
            ditemukan = True

    if ditemukan:
        df_keranjang.to_csv("keranjang.csv", index=False)
        print("Status pesanan berhasil diperbarui ")
    else:
        print("Pesanan tidak ditemukan")

def pesanan_berlangganan():
    print("=== Pesanan saat ini ===")
    

