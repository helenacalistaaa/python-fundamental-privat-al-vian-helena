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