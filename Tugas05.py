# TUGAS 1 : Manipulasi list dasar ------------------------
buah = ["Pisang", "Nanas", "Jambu", "Pepaya", "Mangga", "Kelapa"]
print(buah)
print()

# Tambahkan buah "Melon" pada indeks terakhir
buah.append("Melon")
print(f"Setelah append : {buah}")
print()

# Hapus buah urutan ke 2
buah.pop(1)
print(f"Setelah pop : {buah}")
print()

# Edit buah indeks pertama menjadi "Leci"
buah[0] = "Leci"
print(f"Setelah edit : {buah}")
print()

# Tambahkan buah "Semangka" pada urutan ke 3
buah.insert(2,"Semangka")
print(f"Setelah insert : {buah}")
print()

# Tambahkan buah "Apel", "Ceri", "Alpukat" berturut turut pada indeks terakhir
list_baru = ["Apel", "Ceri", "Alpukat"]
buah.extend(list_baru)
print(f"Setelah extend : {buah}")
print()

# Tampilkan buah indeks 2 hingga 6
print(f"Buah indeks 2 - 6 : {buah[2:7:]}")
print()

# TUGAS 2 : List buku ------------------------
buku = ["Artificial Intelligence for Dummies",
        "The Power of Kepepet",
        "Hujan Keamrin",
        "Data Structure and Alogoritma 2nd Edition",
        "Hundred Pages of Machine Learning"]

print(f"{"":=^55} \n|{"No":^4} | {"Nama Buku":<45} | \n{"":=^55}")

for i in range(len(buku)):
    print(f"| {i+1:^3} | {buku[i]:<45} |")
print(f"{"":=>55}")

# TUGAS 3 : Tambahkan Buku ------------------------
import os # lanjutan ada di os.system
buku = ["Artificial Intelligence for Dummies",
            "The Power of Kepepet",
            "Hujan Keamrin",
            "Data Structure and Alogoritma 2nd Edition",
            "Hundred Pages of Machine Learning"]
while True:

    print(f"{"":=^55} \n|{"No":^4} | {"Nama Buku":<45} | \n{"":=^55}")

    for i in range(len(buku)):
        print(f"| {i+1:^3} | {buku[i]:<45} |")
    print(f"{"":=>55}")

    masukkan_buku = input("Masukkan nama buku : ")
    buku.append(f"{masukkan_buku}")

    os.system("cls") # untuk menghilangkan kode di terminal sebelumnya

    print(f"{"":=^55} \n|{"No":^4} | {"Nama Buku":<45} | \n{"":=^55}")

    for i in range(len(buku)):
        print(f"| {i+1:^3} | {buku[i]:<45} |")
    print(f"{"":=>55}")

    ingin_menambah = input(f"Apakah ingin menambah buku lagi? \nA. Ya\nB. Tidak\n>>")

    if ingin_menambah == "a" or ingin_menambah == "A":
        continue
    else:
        break

# TUGAS 4 : Hapus Buku ------------------------
buku = ["Artificial Intelligence for Dummies",
            "The Power of Kepepet",
            "Hujan Keamrin",
            "Data Structure and Alogoritma 2nd Edition",
            "Hundred Pages of Machine Learning"]
while True:

    print(f"{"":=^55} \n|{"No":^4} | {"Nama Buku":<45} | \n{"":=^55}")

    for i in range(len(buku)):
        print(f"| {i+1:^3} | {buku[i]:<45} |")
    print(f"{"":=>55}")

    masukkannomorbuku = int(input("Masukkan nomor buku : "))
    buku_diambil = buku.pop(masukkannomorbuku-1)

    print(f"{"":=^55} \n|{"No":^4} | {"Nama Buku":<45} | \n{"":=^55}")

    for i in range(len(buku)):
        print(f"| {i+1:^3} | {buku[i]:<45} |")
    print(f"{"":=>55}")

    ingin_menambah = input(f"Apakah ingin menambah buku lagi? \nA. Ya\nB. Tidak\n>>")

    if ingin_menambah == "a" or ingin_menambah == "A":
        continue
    else:
        break

# TUGAS 5 : Edit buku ------------------------
buku = ["Artificial Intelligence for Dummies",
            "The Power of Kepepet",
            "Hujan Keamrin",
            "Data Structure and Alogoritma 2nd Edition",
            "Hundred Pages of Machine Learning"]
while True:

    print(f"{"":=^55} \n|{"No":^4} | {"Nama Buku":<45} | \n{"":=^55}")

    for i in range(len(buku)):
        print(f"| {i+1:^3} | {buku[i]:<45} |")
    print(f"{"":=>55}")

    masukkannomorbuku = int(input("Masukkan nomor buku : "))
    masukkannamabuku = input("Masukkan nama buku baru : ")

    buku[masukkannomorbuku - 1] = masukkannamabuku
    print()

    print(f"{"":=^55} \n|{"No":^4} | {"Nama Buku":<45} | \n{"":=^55}")

    for i in range(len(buku)):
        print(f"| {i+1:^3} | {buku[i]:<45} |")
    print(f"{"":=>55}")

    ingin_menambah = input(f"Apakah ingin menambah buku lagi? \nA. Ya\nB. Tidak\n>>")

    if ingin_menambah == "a" or ingin_menambah == "A":
        continue
    else:
        break