# TUGAS 1 Penulisan tanggal : Menggunakan 2 sintaks print dengan setting parameter end dan sep
tanggal = 6
bulan = "Oktober"
tahun = 2026

print("Tanggal:", end=" ")
print(tanggal, bulan, tahun, sep="-")

# TUGAS 2 Kartu nama : input dan gunakan character control untuk menyamakan letak titik 2 ":" di setiap baris
nama = input("Masukkan Nama\t: ")
prodi = input("Masukkan Prodi\t: ")

print("="*30)

print("Nama\t\t: ", nama,"\n","Program Studi\t: ", prodi, sep="")
print("="*30)

# TUGAS 3 Produk Online Shop : 
nama_barang = input("Masukkan Nama Barang\t: ")
jumlah_stok = int(input("Masukkan Jumlah Stok\t: "))
harga_barang = int(input("Masukkan Harga Barang\t: "))
rating = float(input("Masukkan Rating\t\t: "))

kata = "Sapu Jagad"
print(f"{"":=^30} \n{kata:^30} \n{"":=^30}")

print(f"Stok\t\t: {jumlah_stok} \nHarga\t\t: Rp {harga_barang:>5,} \nRating\t\t: {rating}")
print(f"{"":=^30}")