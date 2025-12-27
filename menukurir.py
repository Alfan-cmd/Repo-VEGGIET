import pandas as pd

df_keranjang = pd.read_csv("keranjang.csv")
df_cart = pd.read_csv("cart.csv")
open_file_2 = pd.read_csv('akun_user.csv')
df_subs = pd.read_csv('daftar_subs.csv')
df_langganan = pd.read_csv('subs.csv',dtype={"status": "string"})


def load_lagi():
    return pd.read_csv("cart.csv")

def pesanan_satuan():
    df_cart = load_lagi()
    kolomTampil = ["nama_pengguna","nama","alamat","harga","status"]
    print("========Pesanan saat ini==========")
    pesanan = pd.merge(df_cart[["username","nama_pengguna","nama","jumlah","subtotal","status"]],
                       open_file_2[["username","alamat"]],
                       on= "username").drop(columns= "username")
    print(pesanan.to_markdown(index = False))

def update_status():
    username_input = input("Masukkan username pesanan yang ingin diupdate: ").lower()
    status_baru = input("Masukkan status baru (Menunggu kurir / Dikirim / Selesai): ")

    ditemukan = False
    for i in range(len(df_cart)):
        if df_cart.loc[i, "username"] == username_input:
            df_cart.loc[i, "status"] = status_baru
            ditemukan = True

    if ditemukan:
        df_cart.to_csv("cart.csv", index=False)
        print("Status pesanan berhasil diperbarui ")
        pesanan_satuan()
    else:
        print("Pesanan tidak ditemukan")

def pesanan_berlangganan():
    print("=== Pesanan saat ini ===")

    merge1 = pd.merge(
        df_langganan,
        df_subs[["kode", "nama", "harga",]],
        on="kode",
        how="left"
    )

    merge_final = pd.merge(
        merge1,
        open_file_2[["username", "alamat"]],
        on="username",
        how="left"
    )

    merge_final["status"] = merge_final["status"].astype(str)

    for i in range(len(merge_final)): 
        if merge_final.loc[i, "status"] == "<NA>": 
            merge_final.loc[i, "status"] = "Belum dikirim"
    hasil = merge_final[["username", "nama", "harga", "alamat", "status"]]
    print(hasil.to_markdown(index=False))


def update_status_langganan():

    df_langganan["status"] = df_langganan["status"].astype(str)

    username_input = input("Masukkan username pesanan yang ingin diupdate: ").lower()
    status_baru = input("Masukkan status baru (Menunggu kurir / Dikirim / Selesai): ")

    ditemukan = False
    for i in range(len(df_langganan)):
        if df_langganan.loc[i, "username"] == username_input:
            df_langganan.loc[i, "status"] = status_baru
            ditemukan = True

    if ditemukan:
        df_langganan.to_csv("subs.csv", index=False)
        print("Status pesanan berhasil diperbarui ")
        pesanan_berlangganan()
    else:
        print("Pesanan tidak ditemukan")



    
