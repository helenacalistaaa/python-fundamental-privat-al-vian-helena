while True:
    try:
        angka = int(input("Masukan Bilangan : "))
    except ValueError:
        print("Bilangan wajib menggunakan angka")
    else:
        print(f"Bilang yang anda masukkan adalah {angka}")
        break