# Fungsi tabel 
buku = [
    ["Artificial Intelligence for Dumies", 5],
    ["The Power of Kepepet", 8],
    ["Hujan Kemarin", 6],
    ["Data Structure and Algoritma 2nd Edition", 10],
    ["Hundred Pages of Machine Learning", 2],
]

def tabel (buku) :
    print(f"{"":=^60} \n| {"No":^4} | {"Buku":^40} | {"Stok":^7} | \n{"":=^60}")
    for i in range (len(buku)) :
        print(f"| {i+1:^4} | {buku[i][0]:<40} | {buku[i][1]:^7} |")
    print(f"{"":=>60}")

tabel(buku)
tabel(buku)
tabel(buku)

# Fungsi ganjil genap 
def ganjilgenap (angka1) :

    if angka1%2 == 0 :
        return 'Genap'
    return 'Ganjil'
#CARA 1
for i in [3, 7, 100, -5, -42]:
    print(ganjilgenap(i))
#CARA 2 
print(ganjilgenap(angka=3))
print(ganjilgenap(angka=7))
print(ganjilgenap(angka=100))
print(ganjilgenap(angka=-5))
print(ganjilgenap(angka=-42))

# Fungsi Perpangkatan
def perpangkatan(angka1,angka2) :
    hasil = 1
    for i in range (angka2):
        hasil *= angka1
    return hasil
#CARA 1
angka = perpangkatan(2,2)
print(angka) 
angka = perpangkatan(2,3)
print(angka)
angka = perpangkatan(5,2)
print(angka)
angka = perpangkatan(2,5)
print(angka)
angka = perpangkatan(3,4)
print(angka)
#CARA 2
for i, j in [(2,2), (2,3), (5,2), (2,5), (3,4)]:
    print(perpangkatan(i,j))