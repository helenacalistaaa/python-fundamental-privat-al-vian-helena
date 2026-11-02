# TUGAS 1 : Cek kelulusan
nilai = int(input("Masukkan Nilai\t: "))

if nilai >= 75:
    print("Lulus")
else:
    print("Remidi")

#Tugas 2 : Struk Kasir 
nama_barang = input("Masukkan nama barang\t\t: ")
harga_barang = int(input("Masukkan harga barang\t\t: "))
jumlah_barang = int(input("Masukkan jumlah barang\t\t: "))

print(f"{"":=^50}")

total_harga = harga_barang*jumlah_barang

print(f"{nama_barang}\t\t: Rp {total_harga:>10,}")

if total_harga > 150000:
    diskon = total_harga*0.1
    print(f"Diskon (10%)\t: Rp {diskon:>10,.0f}")
    total = total_harga - diskon
    print(f"{"":=^50}")
    print(f"Total\t\t: Rp {total:>10,.0f}")
else:
    diskon = 0
    print(f"Diskon (0%)\t: Rp {diskon:>10,}.0f")
    total = total_harga - diskon
    print(f"{"":=^50}")
    print(f"Total\t\t: Rp {total:>10,.0f}")

# Tugas 3 : Klasifikasi Kategori Usia
umur = int(input("Masukkan Usia : "))

if 0 < umur < 5:
    print(f"Balita")
if 5 < umur < 13:
    print(f"Anak anak")
if 13 < umur < 18:
    print(f"Remaja")
if 18 < umur < 60:
    print(f"Dewasa")
if umur > 60:
    print(f"Lansia")
if umur < 0:
    print(f"Tidak Valid")

# TUGAS 4 : Kalkulator sederhana

jenis_operasi = input(f"Pilihan Jenis Operasi: \nA. Pertambahan\nB. Pengurangan\nC. Perkalian\nD. Pembagian\n>>")

angka1 = int(input("Masukkan Angka Pertama\t: "))
angka2 = int(input("Masukkan Angak Kedua\t: "))

if jenis_operasi == "a":
    pertambahan = angka1 + angka2
    print(f"Hasil = {pertambahan}")
if jenis_operasi == "b":
    pengurangan = angka1 - angka2
    print(f"Hasil = {pengurangan}")
if jenis_operasi == "c":
    perkalian = angka1 * angka2
    print(f"Hasil = {perkalian}")
if jenis_operasi == "d":
    pembagian = angka1 + angka2
    print(f"Hasil = {pembagian}")
