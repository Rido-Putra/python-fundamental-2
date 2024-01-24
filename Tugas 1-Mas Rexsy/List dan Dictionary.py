#Tugas List dan Dictionary

'''
1. Buatlah sebuah list dengan nama daftar_nama yang berisi nama-nama teman Anda.
2. Buatlah sebuah dictionary dengan nama data_temans yang berisi informasi tentang teman-teman Anda. Setiap teman memiliki informasi berupa nama, usia, dan hobi.
3. Tampilkan nama-nama teman Anda dari list daftar_nama.
4. Tampilkan informasi lengkap teman pertama dari dictionary data_temans.
5. Tampilkan hanya usia teman kedua dari dictionary 
6. Itj me todata_temans.
7. Tambahkan teman baru ke dalam list daftar_nama dan dictionary data_temans.
8. Hapus teman pertama dari list daftar_nama dan dictionary data_temans.
9. Tampilkan nama-nama teman Anda setelah perubahan.
INSERT INTO `msuser` (`userid`, `sender`, `emailuser`, `fullname`, `password`, `lastlogin`, `regdate`) 
VALUES (1, 'admin@admin.com', 'admin@admin.com', 'admin@admin.com', SHA1('passwordnya'), '2023-11-09 04:07:24', NULL);'''

#jawab
#no. 1
'''fr_name = ["reno", "diki", "hamid"]
#no. 2
fr_name1 = {"name" : "reno", "age" : 23, "hobby" : ["mountain claimbing", "fishing"]}
fr_name2 = {"name" : "diki", "age" : 22, "hobby" : "hiking"}
fr_name3 = {"name" : "hamid", "age" : 24, "hobby" : ["surfing", "diving"]}
#no. 3
print (fr_name)
#no. 4
print (fr_name1)
#no. 5
print (fr_name2)
age = fr_name2["age"]
print(age)
#no. 6

#no. 7
fr_name.append("budi")
print(fr_name)'''
print("-------------------")
#no. 1
fr_name = ["reno", "diki", "hamid"]
print(fr_name)
#no. 2
fr_name_info = {"reno" :
                    {"name" : "reno", 
                    "age" : 23, 
                    "hobby" : ["mountain claimbing", "fishing"]},
                "diki" :
                    {"name" : "diki",
                    "age" : 22, 
                    "hobby" : "hiking"},
                "hamid" :
                    {"name" : "hamid", 
                    "age" : 24, 
                    "hobby" : ["surfing", "diving"]}}
#no. 3
print(fr_name_info)
#no. 4


#no. 5
diki_age = fr_name_info["diki"]["age"]
print(diki_age)

#no. 6
fr_name.append("budi")
print(fr_name)

#no. 7
fr_name_update = {"budi" :
                  {"name" : "budi",
                  "age" : 26,
                  "hobby" : ["fishing", "running"]}}

update = {"Nama" : "Wahyu"}

fr_name_info[update["Nama"]] = update

datas = {"Trima" : {"Name" : "Trima", "Hobby" : "Swimming"}}
fr_name_info[datas["Trima"]["Name"]] = datas["Trima"]
print(fr_name_info)


fr_name_info[fr_name_update["budi"]["name"]] = fr_name_update["budi"]
print(fr_name_info)
#no. 8
del fr_name_info["reno"]
print(fr_name_info)

fr_name.pop(0)
print(fr_name)

