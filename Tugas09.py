# TUGAS 1 (SAVE DATA) ----------
data = [
    ["01", "Sarapan Nasi Kuning", 5000],
    ["01", "Beli Galon", 20000],
    ["01", "Mie Ayam Tin Ton", 15000],
    ["02", "Cilor", 2000],
    ["03", "Paket Data", 50000]
]

with open("File09.csv","w",encoding="utf-8") as ffile :
    for i in range(len(data)) :
        print(data[i][0] , data[i][1], data[i][2] , sep="," , file=ffile)

# TUGAS 2 (LOAD DATA) ---------
data = []
print(data)

with open("File09.csv","r",encoding="utf-8") as ffile :
    for baris in ffile :
        # 1
        baris = baris.strip()
        
        # 2 
        tanggal, menu, harga = baris.split(",")
        
        # 3
        harga = int(harga)
        
        data.append([tanggal, menu, harga])

print(data)

