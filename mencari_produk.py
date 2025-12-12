import pandas as mp
makanan_nabati = [
    # SAYURAN
    {"kode": "SAY001", "nama": "bayam", "stok": 25},
    {"kode": "SAY002", "nama": "kangkung", "stok": 30},
    {"kode": "SAY003", "nama": "sawi hijau", "stok": 20},
    {"kode": "SAY004", "nama": "brokoli", "stok": 15},
    {"kode": "SAY005", "nama": "kembang kol", "stok": 12},
    {"kode": "SAY006", "nama": "wortel", "stok": 40},
    {"kode": "SAY007", "nama": "buncis", "stok": 18},
    {"kode": "SAY008", "nama": "kol", "stok": 22},
    {"kode": "SAY009", "nama": "selada", "stok": 14},
    {"kode": "SAY010", "nama": "timun", "stok": 35},
    {"kode": "SAY011", "nama": "terong", "stok": 16},
    {"kode": "SAY012", "nama": "labu siam", "stok": 10},
    {"kode": "SAY013", "nama": "tomat", "stok": 50},
    {"kode": "SAY014", "nama": "paprika", "stok": 8},
    {"kode": "SAY015", "nama": "kentang", "stok": 60},

    # BUAH
    {"kode": "BUA001", "nama": "apel", "stok": 40},
    {"kode": "BUA002", "nama": "pisang", "stok": 55},
    {"kode": "BUA003", "nama": "jeruk", "stok": 30},
    {"kode": "BUA004", "nama": "mangga", "stok": 20},
    {"kode": "BUA005", "nama": "pepaya", "stok": 12},
    {"kode": "BUA006", "nama": "semangka", "stok": 7},
    {"kode": "BUA007", "nama": "melon", "stok": 9},
    {"kode": "BUA008", "nama": "alpukat", "stok": 18},
    {"kode": "BUA009", "nama": "anggur", "stok": 25},
    {"kode": "BUA010", "nama": "stroberi", "stok": 10},

    # BIJI-BIJIAN
    {"kode": "BIJ001", "nama": "beras", "stok": 100},
    {"kode": "BIJ002", "nama": "gandum", "stok": 60},
    {"kode": "BIJ003", "nama": "jagung", "stok": 45},
    {"kode": "BIJ004", "nama": "oat", "stok": 35},
    {"kode": "BIJ005", "nama": "quinoa", "stok": 20},
    {"kode": "BIJ006", "nama": "barley", "stok": 15},

    # KACANG-KACANGAN
    {"kode": "KAC001", "nama": "kacang merah", "stok": 25},
    {"kode": "KAC002", "nama": "kacang tanah", "stok": 40},
    {"kode": "KAC003", "nama": "kacang kedelai", "stok": 50},
    {"kode": "KAC004", "nama": "kacang polong", "stok": 22},
    {"kode": "KAC005", "nama": "almond", "stok": 15},
    {"kode": "KAC006", "nama": "mete", "stok": 12},
    {"kode": "KAC007", "nama": "pistachio", "stok": 10},

    # OLAHAN NABATI
    {"kode": "OLA001", "nama": "tahu", "stok": 50},
    {"kode": "OLA002", "nama": "tempe", "stok": 45},
    {"kode": "OLA003", "nama": "susu kedelai", "stok": 30},
    {"kode": "OLA004", "nama": "edamame", "stok": 20},
    {"kode": "OLA005", "nama": "tepung tapioka", "stok": 18},
    {"kode": "OLA006", "nama": "tepung terigu", "stok": 40},
    {"kode": "OLA007", "nama": "miso", "stok": 8},
    {"kode": "OLA008", "nama": "oncom", "stok": 12},

    # JAMUR
    {"kode": "JAM001", "nama": "jamur tiram", "stok": 25},
    {"kode": "JAM002", "nama": "jamur kancing", "stok": 30},
    {"kode": "JAM003", "nama": "jamur shitake", "stok": 12},
    {"kode": "JAM004", "nama": "jamur enoki", "stok": 20}
]
open_file = mp.read_csv('daftar_veggiet.csv')
open_file_2 = mp.read_csv('akun_user.csv')

def mencariproduk(): #PAKE YANG INI BIAR LANGSUNG NYARI DI DATABASE
    pilihanuser = input("Masukkan Nama Sayur/Buah/Biji/Olahan : ").lower()
    cari_produk = open_file[(open_file['username'] == pilihanuser)]
    print(cari_produk) #PAKE YANG INI BIAR LANGSUNG NYARI DI DATABASE


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

def binary_search_menu():
    nama = input("Masukkan barang yang ingin dicari: ").lower()

    temp = makanan_nabati.copy()
    temp.sort(key=lambda x: x["nama"].lower())  

    index = binarySearch(temp, nama)

    if index == -1:
        print("Barang tidak ditemukan!")
    else:
        b = temp[index]
        print(f"Kode: {b['kode']} , Nama: {b['nama']}, Stok: {b['stok']}")

    input("Tekan enter...")

def melihat_barang():
    print("=== Daftar Barang ===")
    if len(makanan_nabati) == 0:
        print("Belum ada data barang.")
    else:
        for i in range(len(makanan_nabati)):
            b = makanan_nabati[i]
            print(f"[{i+1}] Nama Produk: {b['nama']} , Stok: {b['stok']} , Kode: {b['kode']}")


def main():
    while True:
        print("Pilih Menu")
        print("1. Mencari Produk")
        print("2. Melihat Produk")
        print("3. Mencari Produk (CSV)")
        pilihan = input("Masukkan Pilihan Anda: ")
        if pilihan == "1":
            binary_search_menu()
        elif pilihan == "2":
            melihat_barang()
        elif pilihan == "3":
            mencariproduk()
main()



