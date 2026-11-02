# TUGAS 1 : Ganjil genap negatif positif

angka = int(input("Masukkan Angka: "))

if angka < 0 and angka %2 == 0:
    print(f"Bilangan Negatif Genap")
if angka < 0 and angka %2 == 1:
    print(f"Bilangan Negatif Ganjil")
if angka > 0 and angka %2 == 0: 
    print(f"Bilangan Positif Genap")
if angka > 0 and angka %2 == 1: 
    print(f"Bilangan Positif Ganjil")
if angka == 0:
    print(f"Bilangan Netral") 

# TUGAS 2 : Seganjil Segenap
angka1 = int(input("Masukkan Angka Pertama\t: "))
angka2 = int(input("Masukkan Angka Kedua\t: "))

if (angka1 %2 == 0 and angka2 %2 == 0) or (angka2 %2 == 1 and angka1 %2 == 1):
    print("Sama")
else:
    print("Beda")

# TUGAS 3 : Struk Kasir 2
nama_barang1 = input("Masukkan nama barang Pertama\t: ")
harga_barang1 = int(input("Masukkan harga barang\t\t: "))
jumlah_barang1 = int(input("Masukkan jumlah barang\t\t: "))
print("\n\n")

nama_barang2 = input("Masukkan nama barang kedua\t: ")
harga_barang2 = int(input("Masukkan harga barang\t\t: "))
jumlah_barang2 = int(input("Masukkan jumlah barang\t\t: "))
print("\n\n")

kupon = input("Punya kupon hemat? (Y/N)\t: ")
membership = input("Punya membership? (Y/N)\t\t: ")

kata = "Struk Belanja"
print(f"{"":=^30} \n{kata:^30} \n{"":=^30}")

total_harga1 = harga_barang1*jumlah_barang1
total_harga2 = harga_barang2*jumlah_barang2

print(f"{nama_barang1}\t\t: Rp {total_harga1:>10,}")
print(f"{nama_barang2}\t\t: Rp {total_harga2:>10,}")

total_belanja = total_harga1 + total_harga2

diskon = 0
if total_belanja > 500000:
    diskon += 0.1
if kupon == "Y" or kupan == "y":
    diskon += 0.05
if membership == "Y" or membership == "Y":
    diskon += 0.1
    if kupon == "Y" or kupon == "y":
        diskon += 0.05

total_diskon = total_belanja*diskon
print(f"Diskon\t\t: Rp {total_diskon:>10,.0f}")
print(f"{"":-^30}")
harga = total_belanja - total_diskon
print(f"Total\t\t: Rp {harga:>10,.0f}")