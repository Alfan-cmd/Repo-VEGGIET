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
    pesanan = pd.merge(df_cart[["username","nama","jumlah","subtotal"]],open_file_2[["username","alamat"]], on="username")
    print(pesanan.to_markdown(index = False))

def pesanan_berlangganan():
    pass
