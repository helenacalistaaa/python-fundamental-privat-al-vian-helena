# TUGAS 1 - Split String
string1 = "Artificial Neural Network Multi Layer Perceptron"
string2 = "Saltcheese, 2000, 1.345, Rating saya kasih satu karena udah bosan"
string3 = "RTX 5090\t100000000\t10.00\tBonus CPU Intel Celeron untuk paket Gaming Turbo"
# CARA 1
kalimat1 = string1.split(" ")
print(kalimat1)
kalimat2 = string2.split(",")
print(kalimat2)
kalimat3 = string3.split("\t")
print(kalimat3)
#CARA 2
for i in [[string1," "],[string2,","],[string3,"\t"]] :
    print(i[0].split(i[1]))
#CARA 3
for i, j in [[string1," "],[string2,","],[string3,"\t"]] :
    print(i.split(j))

# TUGAS 2 - Print Data List
data = [
    ["01", "Sarapan Nasi Kuning", 5000],
    ["01", "Beli Galon", 20000],
    ["01", "Mie Ayam Tin Ton", 15000],
    ["02", "Cilor", 2000],
    ["03", "Paket Data", 50000]
]
#CARA1
for i, j, k in data:
    print(i,j,k, sep = "," )
#CARA2
for i in data:
    print(f"{i[0]},{i[1]},{i[2]}")
#CARA3
for i in range (len(data)):
    print(f"{data[i][0]},{data[i][1]},{data[i][2]}")

# TUGAS 3 - Print Data Dict
data = {
    "A-001" : {"Nama" : "Majalah Bobo", "Stok": 38},
    "A-002" : {"Nama" : "Jendela", "Stok" : 23},
    "A-003" : {"Nama" : "Musyagz Muslimah", "Stok" : 5},
    "B-001" : {"Nama" : "Sejarah Dunia Lengkap", "Stok" : 5},
    "B-002" : {"Nama" : "Hikayat Majapahit", "Stok": 9}
}
#CARA1
for i in data:
    print(i,data[i]["Nama"],data[i]["Stok"],sep=",")
#CARA2
for i,j in data.items():
    print(i,j["Nama"],j["Stok"],sep =",")