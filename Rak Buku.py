class buku : 
    def __init__(self, nama, penulis, penerbit, kategori) :
        self.nama = nama
        self.penulis = penulis
        self.penerbit = penerbit
        self.kategori = kategori

data = [
]

def tabel() :
    global data
    print("="*94)
    print(f"| {"No.":3} | {"Nama Buku":^30} | {"Penulis":^20} | {"Penerbit":^15} | {"Kategori":^10} |")
    print("="*94)
    for i in range(len(data)):
        print(f"| {i+1:>3} | {data[i].nama:<30} | {data[i].penulis:<20} | {data[i].penerbit:<15} | {data[i].kategori:<10} |")
    print("="*94)    

def tambah_buku():
    global data
    tabel()
    nama = input("Masukkan Nama Buku\t: ")
    if len(nama) > 30 :
        nama = nama[:30:]
    penulis = input("Masukkan Nama Penulis\t: ")
    if len(penulis) > 20 :
        penulis = penulis[:20:]
    penerbit = input("Masukkan Nama Penerbit\t: ")
    if len(penerbit) > 15 :
        penerbit = penerbit[:15:]
    kategori = input("Masukkan Kategori Buku\t: ")
    if len(kategori) > 10 :
        kategori = kategori[:10:]
    data.append(buku(nama, penulis, penerbit, kategori))

def edit_buku():
    global data
    tabel()
    baris = int(input("Masukkan nomor baris yang akan diedit : "))
    nama = input("Masukkan Nama Buku\t: ")
    if len(nama) > 30 :
        nama = nama[:30:]
    penulis = input("Masukkan Nama Penulis\t: ")
    if len(penulis) > 20 :
        penulis = penulis[:20:]
    penerbit = input("Masukkan Nama Penerbit\t: ")
    if len(penerbit) > 15 :
        penerbit = penerbit[:15:]
    kategori = input("Masukkan Kategori Buku\t: ")
    if len(kategori) > 10 :
        kategori = kategori[:10:]
    data[baris-1] = buku(nama, penulis, penerbit, kategori)

def hapus_buku():
    global data
    tabel()
    baris = int(input("Masukkan nomor baris yang akan dihapus : "))
    data.pop(baris-1)

def save_data():
    global data
    with open("FileProjek09.csv", "w", encoding = "utf-8") as f:
        for i in range(len(data)):
            print(data[i].nama, data[i].penulis, data[i].penerbit, data[i].kategori, sep = ",", file = f)
        
def load_data():
    global data
    with open("FileProjek09.csv", "a", encoding = "utf-8") as f :
        pass
    with open("FileProjek09.csv", "r", encoding = "utf-8") as f :
        for i in f :
            i = i.strip()
            nama, penulis, penerbit, kategori = i.split(",")
            data.append(buku(nama, penulis, penerbit, kategori))



load_data()
while True:
    tabel()
    print("Mau ngapain nih")
    print("A. Tambah Buku")
    print("B. Edit Buku")
    print("C. Hapus Buku")
    print("D. Keluar")
    pilihan = input(">> ").lower()

    match pilihan:
        case "a":
            tambah_buku()
        case "b":
            edit_buku()
        case "c":
            hapus_buku()
        case "d":
            save_data()
            exit()
        case _:
            print("Input tidak valid")
            input("Tekan enter untuk lanjut") # menghentikan layar