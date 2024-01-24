# Boolean
x = 5
y = 9

value = x != y

print(value)

a = "Hello world"
b = "Hello world"

value2 = a == b

print(value2)

value3 = x == a

print(value3)

# if else statement
# rumus
# if KONDISI:
# Kodenya disini

x = 5
y = 9

a = 10
b = 10

if x <= y:
    print("X kecil dari Y")

if y < x:
    print("y kurang dari x")
elif x > y:
    print("x lebih dari y")
elif y == x:
    print("y lebih dari x")
else:
    print("Semua if elif check kondisi gagal!!")

if x > y and x < y:
    print("operasi and bekerja")
elif x < y and a == b:
    print("Operasi and kedua berhasi;")

if x > y or a > y:
    print("operasi OR berhasil")

if (x > y and x < y) or b > a or a == b:
    print("This complex operator working")

if (b > a or a == b or x > y) and x > y:
    print("This second complex operator working")
else:
    print("This second complex OPERATOR IS NOT working")


"""
x = 5
y = 9

a = 10
b = 10
"""
# program ngecheck berhak buat sim
# User berhak membuat sim, jika umurnya lebih dari 18 tahun DAN statusnya sudah bekerja
# Jika tidak memenuhi keduanya, maka tidak berhak membuat sim
age = 16
working_status = False
if age >= 18 and working_status == True:
    print("User berhak membuat SIM")
else:
    print("User tidak berhak membuart SIM")

if age >= 18:
    if working_status == True:
        print("User berhak membuat sim")
    else:
        print("User tidak berhak membuat ssim, karena statusnya belum bekerja")
else:
    print("Usia user tidak memenuhi untuk membuat sim")

# program ngecek untuk mahasiswa berhak meminjam buku di perpus
# 1 jika user adalah mahasiswa, dan user semester minimal 3, dan memiliki kartu perpustakaan, maka dia berhak untuk meminjam buku
# 2 jika user adalah mahasiswa, dan memiliki kartu perpus, tapi user semester adalah kurang dari 3, maka dia tetap berhak meminjam, tapi
# ditambahi keterangan batas meminjam hanya 7 hari
# 3 jika user bukan mahasiswa, maka tidak berhak meminjam buku
# BONUS
# 1 jika user bukan mahasiswa, tapi dia punya kartu perpus, maka dia akan ditangkap polisi
# 2 struktur datanya coba pakai dictionary.

"""
contoh diktionary :
fr_name_update = {"budi" :
                  {"name" : "budi",
                  "age" : 26,
                  "hobby" : ["fishing", "running"]}}
"""

print("welcome to student library")
student_data = {
    "name": "bon",
    "student_card": False,
    "semester": 2,
    "library_card": True,
}
if student_data["library_card"] == True:
    if student_data["student_card"] == True:
        if student_data["semester"] >= 3:
            print("You can borrow book fo a month")
        else:
            print("You could only borrow max 7 day's only")
    elif student_data["student_card"] != True:
        print("You will got jailed!!!")

"""
1. Nilainya dijadikan input, harus input nama, student_card dst
2. Pakai while True, buatlah programnya untuk berulang2
3. buatlah frasa kata kunci untuk memberhentikan programnya
4. pakai exit()
5. print nama-nama atau data-data2 yg sudah diinput
"""
