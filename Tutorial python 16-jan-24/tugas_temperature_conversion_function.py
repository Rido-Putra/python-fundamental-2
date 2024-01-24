# Buatlah fungsi dimana kita bisa konversi suhu. misal dari celcius -> kelvin -> fahrenheit ->reamur
# cara pakai baris 83
# 1. celcius ke kelvin or fahrenheit or reamur -> WAJIB
# 2. kelvin ke celcius or fahrenheit or reamur
# 3. fahrenheit ke celcius, kelvin, reamur
# 4. reamur ke celcius,kelvin, fahrenheit
import json


def celsius_to_reamur(celsius):
    """
    Convert temperature from Celsius to Reamur.
    Formula: Celsius * 4/5
    """
    reamur = celsius * 4 / 5
    return reamur


def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    Formula: (Celsius * 9/5) + 32
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def celsius_to_kelvin(celsius):
    """
    Convert temperature from Celsius to Kelvin.
    Formula: Kelvin + 273.15
    """
    kelvin = celsius + 273
    return kelvin


def reamur_to_celsius(reamur):
    """
    Convert temperature from Reamur to Celsius.
    Formula: Reamur 5/4 Celsius
    """
    celsius = reamur * 5 / 4
    return celsius


def reamur_to_fahrenheit(reamur):
    """
    Convert temperature from Reamur to Fahrenheit.
    Formula: Reamur 9/4 + 32
    """
    fahrenheit = (reamur * 4 / 9) + 32
    return fahrenheit


def reamur_to_kelvin(reamur):
    """
    Convert temperature from Reamur to Kelvin.
    Formula: Reamur 5/4 + 273
    """
    kelvin = (reamur * 5 / 4) + 273
    return kelvin


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    Formula: (Fahrenheit - 32) * 5/9
    """
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def fahrenheit_to_reamur(fahrenheit):
    """
    Convert temperature from Fahrenheit to Kelvin.
    Formula: (Fahrenheit 4/9 - 32
    """
    reamur = 4 / 9 * (fahrenheit - 32)
    return reamur


def fahrenheit_to_kelvin(fahrenheit):
    """
    Convert temperature from Fahrenheit to Kelvin.
    Formula: 5 / 9 * (fahrenheit - 32) + 273
    """
    kelvin = 5 / 9 * (fahrenheit - 32) + 273
    return kelvin


def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    Formula: (Celsius - 273
    """
    celsius = kelvin - 273
    return celsius


def kelvin_to_reamur(kelvin):
    """
    Convert temperature from Kelvin to  Reamur.
    Formula: Kelvin 4/5 - 273
    """
    reamur = 4 / 5 * (kelvin - 273)
    return reamur


def kelvin_to_fahrenheit(kelvin):
    """
    Convert temperature from Kelvin to  Fahrenheit.
    Formula: Kelvin 9/5 - 273 + 32
    """
    fahrenheit = 9 / 5 * (kelvin - 237) + 32
    return fahrenheit


""" aplikasi konversi suhu
1. masukin input dari celsius konversi reamur, fahrenheit, kelvin
2. masujinn input dari reamur to celsius, fahrenheit, kelvin
3. masukin input dari fahrenheit to celsius, reamur, kelvin
4. masukin input dari kelvin to celsius, reammur, fahrenheit
5. exit
note :
1. suhu input satu aja, translate/konversi ke 3 suhu sekaligus
ex = celcius -> reamur, fahren, kelv

ide ku =
aku maunya manual satu persatu dulu, misal celcius to fahrenheit, celcius to kelv
challenge,bug, to improve:
1. User pasti akan kecapean dalam memasukan input 

solusi mas (pythonic way): 
1.  bikin fungsi, input celsius--> R,F,K


ideku = 
1. program harus bisa ambil input user, input suhu
1a. karena input di python itu string -> harus konversi ke int
2. program harus bisa ambil input user, ttg jenis suhu (c,r,k,f)
3. jika jenis input suhu == c -> eksekusi fungsi c_to_f,k,r | r_to_c,k,f dst
ex = celcius -> reamur, fahren, kelv
4. print outputnya
5. selesai
"""


# 1. konversi c--> r, 2. komversi c-->f


# int(input("masukan suhu dalam celsius"))

# start aplikasi kode lebih jelas
# .json = data diictionary
"""
    with open("output.json", "r") as file: #-> baca data json
        data: dict = json.load(file)
    print(f"data json adalah {data}")
    print(data.get("output"))
    print(data.get("output")[0])
    print(type(data.get("output")[0]))
    with open("output.txt", "r") as file: 
        data2 = file.readlines()
    print(data2[0])
    print(type(data2[0]))
    print(data2[0][1:5])
    exit()
"""

if __name__ == "__main__":
    while True:
        try:
            suhu_conversi = int(input("Masukan suhu yang akan di konversi!\n"))
            break
        except ValueError:  # gmn kalau tipe error 2, tapi handlling kode nya
            print("Please check your input!!!")

    while True:
        pilihan_input = input("Silahkan masukan konversi suhu dari C, R, F, K \n")
        pilihan_input = pilihan_input.upper()
        pilihan_input_key = ("C", "R", "F", "K")
        if pilihan_input not in pilihan_input_key:  # "C" != tuple (c,r,f,k)
            print("Please check your temperature conversion input!!!")
        elif pilihan_input in pilihan_input_key:
            break
    # pilihan_hasil = input(
    #    "SIlahkan masukan  konversi suhu yang diinginkan C, R, F, K \n"
    # )
    # pilihan_input_key = ("C", "R", "F", "K")
    # 123 celcius
    if pilihan_input == "C":
        print("Suhu celsius akan di konversi")
        c_to_f = celsius_to_fahrenheit(suhu_conversi)
        c_to_r = celsius_to_reamur(suhu_conversi)
        c_to_k = celsius_to_kelvin(suhu_conversi)
        print(
            f"suhu awal {suhu_conversi} celcius, suhu konversi adalah {c_to_f} fahrenheit"
        )
        print(
            f"suhu awal {suhu_conversi} celcius, suhu konversi adalah {c_to_r} reamur"
        )
        print(
            f"suhu awal {suhu_conversi} celcius, suhu konversi adalah {c_to_k} kelvin"
        )
        output = {"output": [c_to_f, c_to_r, c_to_k]}
        with open("output.json", "w") as file:
            json.dump(output, file)

        with open("output.json", "r") as file:
            data = json.load(file)
        print(data)
        # data2 = json.load(file)
        # print(data2)

        # with open("output.txt", "w") as file:
        #    file.writelines(f"{c_to_f, c_to_r, c_to_k}")

    if pilihan_input == "F":
        print("Suhu fahrenheit akan di konversi")
        f_to_c = fahrenheit_to_celsius(suhu_conversi)
        f_to_r = fahrenheit_to_reamur(suhu_conversi)
        f_to_k = fahrenheit_to_kelvin(suhu_conversi)
        print(
            f"suhu awal {suhu_conversi} fahrenheit, suhu konversi adalah {f_to_c} celcius"
        )
        print(
            f"suhu awal {suhu_conversi} fahrenheit, suhu konversi adalah {f_to_r} reamur"
        )
        print(
            f"suhu awal {suhu_conversi} fahrenheit, suhu konversi adalah {f_to_k} kelvin"
        )

    if pilihan_input == "R":
        print("Suhu reamur akan di konversi")
        r_to_c = reamur_to_celsius(suhu_conversi)
        r_to_f = reamur_to_fahrenheit(suhu_conversi)
        r_to_k = reamur_to_kelvin(suhu_conversi)
        print(
            f"suhu awal {suhu_conversi} reamur, suhu konversi adalah {r_to_c} celcius"
        )
        print(
            f"suhu awal {suhu_conversi} reamur, suhu konversi adalah {r_to_f} fahrenheit"
        )
        print(f"suhu awal {suhu_conversi} reamur, suhu konversi adalah {r_to_k} kelvin")

    if pilihan_input == "K":
        print("Suhu kelvin akan di konversi")
        k_to_c = kelvin_to_celsius(suhu_conversi)
        k_to_f = kelvin_to_fahrenheit(suhu_conversi)
        k_to_r = kelvin_to_reamur(suhu_conversi)
        print(
            f"suhu awal {suhu_conversi} kelvin, suhu konversi adalah {k_to_c} celcius"
        )
        print(
            f"suhu awal {suhu_conversi} kelvin, suhu konversi adalah {k_to_f} fahrenheit"
        )
        print(f"suhu awal {suhu_conversi} kelvin, suhu konversi adalah {k_to_r} reamur")
    exit()

    kelvin_conv = kelvin_to_celsius(3)
    print(kelvin_conv)

    celsius_conv = celsius_to_fahrenheit(30)
    print(celsius_conv)

    k_to_f = kelvin_to_fahrenheit(87)
    print(k_to_f)
