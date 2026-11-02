# Cara 1
# print("Pilih Jenis Operasi:")
# print("a. Pertambahan")
# print("b. Pengurangan")
# print("c. Perkalian")
# print("d. Pembagian")
# print("e. Modulus")
# print("f. Perpangkatan")
# print(float(input ("Masukkan Angka Pertama: ")))
# print(float(input ("Masukkan Angka Kedua: ")))

# Cara 2
# print("Pilih Jenis Operasi: ", "\n" 
#       "A. Pertambahan", "\n"
#       "B. Pengurangan", "\n"
#       "C. Perkalian", "\n"
#       "D. Pembagian", "\n"
#       "E. Modulus", "\n"
#       "F. Perpangkatan"
# )

# Cara 3
print("Pilih Jenis Operasi:\na. Pertambahan\nb. Pengurangan\nc. Perkalian\nd. Pembagian\ne. Modulus\nf. Perpangkatan")

operasi = input(">>").upper()

# lower buat ngecilin huruf
# upper buat ngecilin huruf

angka1 = float(input(f"Masukkan Angka Pertama: "))
angka2 = float(input(f"Masukkan Angka Kedua: "))

if operasi == "A" :
    hasil = angka1 + angka2
    print(f"Pertambahan: {hasil}")
elif operasi == "B" :
    hasil = angka1 - angka2
    print(f"Pengurangan: {hasil}")
elif operasi == "C" :
    hasil = angka1 * angka2
    print(f"Perkalian: {hasil}")
elif operasi == "D" :
    hasil = angka1 / angka2
    print(f"Pembagian: {hasil}")
elif operasi == "E" :
    hasil = angka1 % angka2
    print(f"Modulus: {hasil}")
elif operasi == "F" :
    hasil = angka1 ** angka2
    print(f"Perpangkatan: {hasil}")
else :
    print("Nilai Huruf Tidak Valid")

print("Program Selesai")

# -----------------------------------------------------------------------------------------------
# MATCH CASE
print("Pilih Jenis Operasi:\na. Pertambahan\nb. Pengurangan\nc. Perkalian\nd. Pembagian\ne. Modulus\nf. Perpangkatan")

operasi = input(">>").upper()

angka1 = float(input(f"Masukkan Angka Pertama: "))
angka2 = float(input(f"Masukkan Angka Kedua: "))

match  operasi : 
    case "A" :
        hasil = angka1 + angka2
        print(f"Pertambahan: {hasil}")
    case "B" :
        hasil = angka1 - angka2
        print(f"Pengurangan: {hasil}")
    case "C" :
        hasil = angka1 * angka2
        print(f"Perkalian: {hasil}")
    case "D" :
        hasil = angka1 / angka2
        print(f"Pembagian: {hasil}")
    case "E" :
        hasil = angka1 % angka2
        print(f"Modulus: {hasil}")
    case "F" :
        hasil = angka1 ** angka2
        print(f"Perpangkatan: {hasil}")
    case _ :
        print("Nilai Huruf Tidak Valid")