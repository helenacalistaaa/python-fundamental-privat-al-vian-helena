# TUGAS 1 : Ganjil genap berulang
while True :
    angka = int(input("Masukkan Angka : "))

    if angka %2 == 0:
        print("Genap")
    else:
        print("Ganjil")

    menambah_lagi = input("Ingin menggunakan program lagi?\nA. Ya\nB. Tidak\n>>")

    if menambah_lagi == "a" or menambah_lagi == "A":
        continue
    else :
        break

# TUGAS 2 : Penjumlahan tak hingga
hasil = 0
while True:

    angka = int(input("Masukkan Angka : "))
    
    if angka != 0:
        hasil += angka
        continue
    else:
        break
print(f"Hasil : {hasil}")

# TUGAS 3 : Garis bintang
masukkan_panjang = int(input("Masukkan Panjang : "))

for i in range (masukkan_panjang): 
    print("* ", end="")