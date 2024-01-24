"""
f(x,y) = x * Y

f(10,5) = 10*5 = 50
"""


def helloworld():
    print("Hello world")


def penjumlahan(x, y):
    hasil = x + y
    return hasil


helloworld()
hasil = penjumlahan(92, 7)
print(hasil)


def pemangkatan(i, j):
    hasil = i**j
    print(hasil)


pemangkatan(6, 2)


def info_dict():
    info_dict = {"name": "Rahman", "age": 19, "location": "Indonesia"}
    print(info_dict)


info_dict()


def kenalan(name):
    hasil = f"nama saya adalah {name}"
    return hasil  # nama saya adalah


def asal(lokasi):
    hasil = f"berasal dari {lokasi}"
    return hasil


nama = kenalan("Budi")
lokasi = asal("Banyumas")

print(f"{nama}, {lokasi}")


"""def kenalan_test()
    name = "budi"
    age = 19
    hasil = f"Nama saya adalah" (name), "umur saya" (age) "tahun"
    return hasil
    #nama saya budi, umur 19 tahun"""


def kenalan_name(name):
    hasil = f"Nama saya adalah {name}"
    return hasil


def kenalan_umur(age):
    hasil = f"saya berumur {age} tahun"
    return hasil


nama = kenalan_name("Budi")
umur = kenalan_umur(19)

print(f"{nama}, {umur}")


def kenalan_test2(nama, umur):
    hasil = f"nama saya {nama}, saya berumur {umur} tahun"
    return hasil


kenalan_yuk = kenalan_test2("Budi", 19)
print(kenalan_yuk)


# Buatlah fungsi dimana kita bisa konversi suhu. misal dari celcius -> kelvin -> fahrenheit ->reamur
# cara pakai baris 83
# 1. celcius ke kelvin or fahrenheit or reamur -> WAJIB
# 2. kelvin ke celcius or fahrenheit or reamur
# 3. fahrenheit ke celcius, kelvin, reamur
# 4. reamur ke celcius,kelvin, fahrenheit
