# ---------------- Persegi panjang utuh ----------------
panjang = int(input(f"Masukkan panjang: "))
lebar = int(input(f"Masukkan lebar: "))

counter2 = 0
while counter2 < lebar : # seberapa banyak bintang
    counter = 0 # digunakan untuk menghitung bintang pertama yang akan dikeluarkan
    while counter < panjang :
        print("* ", end="")
        counter += 1 # mengeprint banyak kolom
    print("\n", end="")
    counter2 += 1 # mengeprint banyak baris 

# ---------------- Persegi panjang bolong ---------------
panjang = int(input(f"Masukkan panjang: "))
lebar = int(input(f"Masukkan lebar: "))

counter2 = 0
while counter2 < lebar : # seberapa banyak bintang
    counter = 0 # digunakan untuk menghitung bintang pertama yang akan dikeluarkan
    while counter < panjang :
        if counter == 0 or counter == panjang - 1 or counter2 == 0 or counter2 == lebar - 1 : 
            # pakai or karena kalau salah satu bener ya di print aja
            print("* ", end="")
        else :
            print("  ", end="")
        counter += 1 # mengeprint banyak kolom
    print("\n", end="")
    counter2 += 1 # mengeprint banyak baris 

panjang = int(input(f"Masukkan panjang: "))
lebar = int(input(f"Masukkan lebar: "))

# pakai and
panjang = int(input(f"Masukkan panjang: "))
lebar = int(input(f"Masukkan lebar: "))

counter2 = 0
while counter2 < lebar : # seberapa banyak bintang
    counter = 0 # digunakan untuk menghitung bintang pertama yang akan dikeluarkan
    while counter < panjang :
        if 0 < counter < panjang -1 and 0 < counter2 < lebar -1 : 
            # pakai or karena kalau salah satu bener ya di print aja
            print(" ", end="")
        else :
            print("*", end="")
        counter += 1 # mengeprint banyak kolom
    print("\n", end="")
    counter2 += 1 # mengeprint banyak baris 