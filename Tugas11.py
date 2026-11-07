# TUGAS 1 - Exception Dasar

try :
    with open("File0.csv","r") as filebaru :
        pass
except FileNotFoundError:
    print("File Tidak Ada")
else:
    print("File Benar")
finally:
    print("Selesai")

# TUGAS 2 - Pemaksaan Input

while True:
    try:
        angka = int(input("Masukan Bilangan : "))
    except ValueError:
        print("Bilangan wajib menggunakan angka")
    else:
        print(f"Bilang yang anda masukkan adalah {angka}")
        break