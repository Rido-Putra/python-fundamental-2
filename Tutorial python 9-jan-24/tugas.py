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

"""print("welcome to student library")
student_data = {
    "name": "bon",
    "student_card": False,
    "semester": 2,
    "library_card": True,
}
if student_data["library_card"] == True:
    if student_data["student_card"] == True:
        if student_data["semester"] >= 3:
            print("You can borrow book for a month")
        else:
            print("You could only borrow max 7 day's only")
    elif student_data["student_card"] != True:
        print("You will got jailed!!!")"""

"""
1. Nilainya dijadikan input, harus input nama, student_card dst
2. Pakai while True, buatlah programnya untuk berulang2
3. buatlah frasa kata kunci untuk memberhentikan programnya
4. pakai exit()
5. print nama-nama atau data-data2 yg sudah diinput
"""
"""
while True:
    input_name = input("Pls input name = ")
    if input_name == "EXIT":
        print("exiting program")
        exit()
"""


while True:
    student_name = input("Please enter your name!!! \n")
    if student_name == "EXIT":
        break
    student_name = student_name.upper()
    library_card = input("Do you have library card!!!\n")
    library_card = library_card.upper()  # -> unlock -> Unlock
    library_card_key = ["Y"]
    student_card = input("DO you have student card!!! \n")
    student_card = student_card.upper()
    student_card_key = ["Y"]
    semester = int(input("Please input your semester!!!\n"))

    if student_name == "EXIT":
        break

    if library_card in library_card_key:
        library_card = True
    else:
        library_card = False

    if student_card in student_card_key:
        student_card = True
    else:
        student_card = False

    if semester >= 3:
        semester = True
    else:
        semester = False

    if library_card == True and student_card == True and semester == True:
        print("You can borrow a book for a month")
    elif library_card == True and student_card == True and semester == False:
        print("You could only borrow max 7 day's only")
    elif library_card == True and student_card == False:
        print("You got jailed")
    print(student_name, library_card, student_card, semester)
    #data = {"nama" : siapa, library card, student card, semester brp, status = }
    #listkosong.append(data)
    # if library_card in library_card_key:
    #    library_card == True
    #    if student_card in student_card_key:
    #        if semester >= 3:
    #            print("You can borrow book fo a month")
    #        else:
    #            print("You could only borrow max 7 day's only")
    #    elif student_card != True:
    #        print("You will got jailed!!!")
    # else:
    #    print("Sorry, You are Not Allowed to borrow book from library")

    continue_ = input("Do you want to continue? Y/N : ")
    continue_ = continue_.upper()
    if continue_ == "N":
        #print(listkosong)
        break

    try:
        with open("values.txt", "w") as values:
            values.write(student_name)
    except Exception as e:
        print("There is a Problem", str(e))
