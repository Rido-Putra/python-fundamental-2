
#global and local variable
#1. local variable
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is" + " " +x) #-------> local variable
myfunc()
print("Python is" + " " + x) #-------->global variable

# satu nilai untuk beberapa variabel
x = y = z = "orange"
print(x)
print(y)
print(z)

# penugasan (assigment operator)

#1. = 
a = 10
print('hasil :' , a)
b = 15
print('hasil :' ,b)

#2. +=
a, b = 10, 8
a +=b
print('hasil :', a)

#3. -+
a, b = 10, 8
a -= b
print('hasil :', a)

#4.  
a, b = 10, 8
a *= b
print('hasil :', a)

#5. /=
a, b = 10, 5
a /= b
print('hasil :',  a)

#6. %=
a, b = 10, 4
a %= b
print('hasil :', a)

#7. **=
a, b = 10, 2
a **= b
print('hasil :', a)

#8. //=
a, b = 10, 4
a //= b
print('hasil :', a)


print('___________________"')
#Metode string
#1. metode upper() dan lower()
kalimat = "Hallo, ini adalah string"
besar = kalimat.upper()
print(besar)
#2. metode lower
kalimat = "Hallo, ini adalah string"
besar = kalimat.lower()
print(besar)

#3. metode capitalize() dan tittle()
kalimat = 'ini adalah judul'
# Mengubah huruf pertama menjadi huruf kapital
kalimat_awal = kalimat.capitalize()
print(kalimat_awal)
# Output: Ini adalah judul
# Mengubah huruf pertama setiap kata menjadi huruf kapital
judul = kalimat.title()
print(judul)
# Output: Ini Adalah Judul

#4. metode count()
kalimat = 'berapa kali jumlah ini muncul dalam kalimat ini?'
print(kalimat)
jumlah_ini = kalimat.count('ini')
print(f'jumlah kata "ini" : {jumlah_ini} buah ditemukan dalam kalimat' )

#5. metode replace()
kalimat = 'ganti kata "ini" dengan kata "itu" dalam kalimt berikut'
print(kalimat)
ganti_kata = kalimat.replace("ini", "itu")
print(ganti_kata)
print(f'Berikut adalah hasil pergantian kata, hasilnya : {ganti_kata}')

#6. metode split()
kalimat = 'pisang jeruk mangga apel pepaya'
buah_list = kalimat.split()
print(buah_list)
kalimat = 'pisang,jeruk,mangga,apel,pepaya'
buah_list2 = kalimat.split(",")
print(buah_list2)

#7. metode strip() -->menghapus spasi di awal dan diakhir kalimat
kalimat ='    Ini kalimat dengan spasi diawal dan diakhir kalimat!       '
hasil_strip = kalimat.strip()
print(hasil_strip)

#8. metode startswith() dan endswith()
kalimat = 'ini adalah kalimat diawali dengan kata "ini" dan diakhiri kata "itu"'
starts_with_ini = kalimat.startswith('ini')
print(f'ini adalah kalimat diawali dengan kata "ini" : {starts_with_ini} ')
ends_with_itu = kalimat.endswith('"itu"')
print(f'diakhiri dengan kata "itu" : {ends_with_itu}')

#9. metode find()  --> mencari indeks awal kata "kata" dalam kalimat
kalimat = 'cari kata dalam kalimat ini'

