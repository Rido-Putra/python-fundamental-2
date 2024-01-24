# dictionary -> pakainya key-value pair
# misal ada variabell perorangan, isinya ada nama, umur, hobi

asep = {"nama" : "Asep", 
        "umur" : 21,
        "hobi" : "memancing",
        } 

name_asep = asep["nama"]
#shortcut command+shift+p
#command
umur_asep = asep["umur"]
hobi_asep = asep["hobi"]
print(name_asep)
print(umur_asep)
print(hobi_asep)

get_name = asep.get("nama")
print(get_name)
get_place = asep.get("location")
print(get_place)
#get_place = asep["location"] -> keyerror , location gk ada di dalam data asep
#print(get_place)
#
asep = {"nama" : "Asep", 
        "umur" : 21,
        "hobi" : ["memancing", "membaca"],
        "isWorking" : True,
        "TempatTinggal" : {"RT/RW" : [4,9],
                           "Kelurahan" : "Purwokerto Selatan",
                           "Kecamatan" : "Purwokerto",
                           "Kabupaten" : "Banyumas",
                           "Negara" : ["ID", "INDONESIA"]}
        } 

#mendapatkan value dalam dictionary
hobi = asep["hobi"] 
ttl = asep["TempatTinggal"]
print(hobi) #asep
print(ttl) # dictionary TempatTinggal

#mengupdate data
asep["nama"] = "Rido"
asep["umur"] = 24
new_hobi = "menanam"
new_hobi_2 = "bertani"
new_hobi_3 = "berdagang"
list_hobi = ["coding", "olahraga"]
hobi = asep["hobi"]
hobi.append(new_hobi) #['memancing', 'membaca', 'menanam' ]
asep["hobi"].append(new_hobi_2) # ['memancing', 'membaca', 'menanam', 'bertani']
asep["hobi"].append(new_hobi_3)
asep["hobi"].extend(list_hobi)

print(asep)

print("---------------------------------------------------------")
asep = {"nama" : "Asep", 
        "umur" : 21,
        "hobi" : ["memancing", "membaca"],
        "isWorking" : True,
        "TempatTinggal" : {"RT/RW" : [4,9],
                           "Kelurahan" : "Purwokerto Selatan",
                           "Kecamatan" : "Purwokerto",
                           "Kabupaten" : "Banyumas",
                           "Negara" : ["ID", "INDONESIA"]}
        } 

ttl = asep["TempatTinggal"]
print(ttl)
rt_rw = ttl["RT/RW"]
print(rt_rw)
country = ttl["Negara"]
INDONESIA = country[1]

print(country)
#[asd][32][zxa]
INDONESIA = asep["TempatTinggal"]["Negara"][1]
COUNTRY = asep.get("TempatTinggal").get("Negara")
print(INDONESIA)
print(COUNTRY)
#update info salary
salary = 12000
asep["salary"] = salary

asep["TempatTinggal"]["Benua"] = "Asia Tenggara"
print(asep)
#example
car = {"brand" : "Hyundai", "series" : "TDR3000", "year" : 2011, "location" : "Japan"}

year = car.pop("year")
print(car)
print(year)

del car["location"]
print(car)

food = {"title" : "Nasi Goreng", "price" : 12000, "ingredients" : ["Rice", "Egg", "Soy sauce"]}

food["title"] = "Mie Goreng" #-> update value title jadi mie goreng
food["isHalal"] = True #-> menambahkan key-value baru isHalal : True
ingredients = food["ingredients"] #-> deklarasi variabel baru bersiikan list ingredients
print(food["price"]) #-> akses value price 12000
ingredients.append("Garlic") #-> mengupdate list ingredients dengan value baru garlic
new_ingredients = ["pepper", "MSG"]
ingredients.extend(new_ingredients) #-> menambahkan value dalam list ingredients dengan value new_ingredients
food["discount"] = 0.10
food["price_after_discount"] = int(food["price"] - (food["discount"] * food["price"]))
new_info_food = food.pop("isHalal") #-> menghapus key-value isHalal
isHalal = {"isHalal" : new_info_food}
print(food)
#print(new_info_food)
print(isHalal)