# CARA 1
print("Pilih Satuan Suhu Akhir:\na. Celcius\nb. Reamur\nc. Fahrenheit\nd. Kelvin")

operasi1 = input(">>")

suhu1 = float(input(f"Masukkan Nominal Suhu Awal: "))

print("Pilih Satuan Suhu Akhir:\na. Celcius\nb. Reamur\nc. Fahrenheit\nd. Kelvin")

operasi2 = input(">>")

match [operasi1,operasi2] : 
    case [op1,op2] if op1 == "a" and op2 == "a" :
        celcius_ke_celcius = suhu1
        print(f"Nominal Suhu Akhir: {celcius_ke_celcius}")
    case [op1,op2] if op1 == "a" and op2 == "b" :
        celcius_ke_reamur = suhu1/5*4
        print(f"Nominal Suhu Akhir: {celcius_ke_reamur}")
    case [op1,op2] if op1 == "a" and op2 == "c" :
        celcius_ke_fahrenheit = suhu1/5*9+32
        print(f"Nominal Suhu Akhir: {celcius_ke_fahrenheit}")
    case [op1,op2] if op1 == "a" and op2 == "d" :
        celcius_ke_kelvin = suhu1+273
        print(f"Nominal Suhu Akhir: {celcius_ke_kelvin}")
    case [op1,op2] if op1 == "b" and op2 == "a" :
        reamur_ke_celcius = suhu1/4*5
        print(f"Nominal Suhu Akhir: {reamur_ke_celcius}")
    case [op1,op2] if op1 == "b" and op2 == "b" :
        reamur_ke_reamur = suhu1
        print(f"Nominal Suhu Akhir: {reamur_ke_reamur}")
    case [op1,op2] if op1 == "b" and op2 == "c" :
        reamur_ke_fahrenheit = suhu1/4*9+32
        print(f"Nominal Suhu Akhir: {reamur_ke_fahrenheit}")
    case [op1,op2] if op1 == "b" and op2 == "d" :
        reamur_ke_kelvin = suhu1/4*5 + 273
        print(f"Nominal Suhu Akhir: {reamur_ke_kelvin}")
    case [op1,op2] if op1 == "c" and op2 == "a" :
        fahrenheit_ke_celcius = (suhu1-32)/9*5
        print(f"Nominal Suhu Akhir: {fahrenheit_ke_celcius}")
    case [op1,op2] if op1 == "c" and op2 == "b" :
        fahrenheit_ke_reamur = (suhu1-32)/9*4
        print(f"Nominal Suhu Akhir: {fahrenheit_ke_reamur}")
    case [op1,op2] if op1 == "c" and op2 == "c" :
        fahrenheit_ke_fahrenhit = (suhu1-32)/9*9+32
        print(f"Nominal Suhu Akhir: {fahrenheit_ke_fahrenhit}")
    case [op1,op2] if op1 == "c" and op2 == "d" :
        fahrenheit_ke_kelvin = (suhu1-32)/9*5+273
        print(f"Nominal Suhu Akhir: {fahrenheit_ke_kelvin}")
    case [op1,op2] if op1 == "d" and op2 == "a" :
        kelvin_ke_celcius = suhu1-273
        print(f"Nominal Suhu Akhir: {kelvin_ke_celcius}")
    case [op1,op2] if op1 == "d" and op2 == "b" :
        kelvin_ke_reamur = (suhu1-273)/5*4
        print(f"Nominal Suhu Akhir: {kelvin_ke_reamur}")
    case [op1,op2] if op1 == "d" and op2 == "c" :
        kelvin_ke_fahrenhit = (suhu1-273)/5*9+32
        print(f"Nominal Suhu Akhir: {kelvin_ke_fahrenhit}")
    case [op1,op2] if op1 == "d" and op2 == "d" :
        kelvin_ke_kelvin = suhu1
        print(f"Nominal Suhu Akhir: {kelvin_ke_kelvin}")

