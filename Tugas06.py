# TUGAS 1 : Manipulasi Dictionary Dasar ------------------------- 
nilai_siswa = {"Andre" : 78, "Hena" : 90, "Tono" : 67}
print(nilai_siswa)
print()

# Tambahkan siswa "Doni" dengan nilai 88
nilai_siswa["Doni"] = 88
print(f"Nilai siswa sesudah : {nilai_siswa}")
print()

# Hapus data siswa Hena
hapusdata = nilai_siswa.pop("Hena")
print(f"Dictionary Sesusdah Pop : {nilai_siswa}")
print()

# Edit nilai siswa "Tono" menjadi 76
nilai_siswa ["Tono"] = 76
print(f"Nilai sesudah : {nilai_siswa}")
print()

# Tambahkan siswa "Joni", "Lala", "Winda" dengan nilai berturut turut 88, 95, 100
nilai_tambahan = {
    "Joni" : 88,
    "Lala" : 95,
    "Winda" : 100
}
gabungan = nilai_siswa | nilai_tambahan
print(f"Gabungan : {gabungan}")
print()

# TUGAS 2 : Tabel siswa ------------------------- 
nilai_siswa = {"Andre" : 78, "Hena" : 90, "Tono" : 67}

print(f"{"":=^25} \n| {"Nama":<10} | {"Nilai":<9} | \n{"":=^25}")
for i in nilai_siswa :
    print(f"| {i:<9} | {nilai_siswa[i]:<9} |")
print(f"{"":=>25}")

# TUGAS 3 : Tambah data siswa
nilai_siswa = {"Andre" : 78, "Hena" : 90, "Tono" : 67}

print(f"{"":=^25} \n| {"Nama":<10} | {"Nilai":<9} | \n{"":=^25}")
for i in nilai_siswa :
    print(f"| {i:<9} | {nilai_siswa[i]:<9} |")
print(f"{"":=>25}")

nama = input("Masukkan Nama Siswa\t\t: ")
nilai = input("Masukkan Nilai Siswa\t: ")

if nama in nilai :
    print(f"Siswa dengan nama "{nama}" sudah di Tabel")
else: