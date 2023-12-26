print("hello world")

number1 = 3.14
number2 = 3.232

number_of_integer = 92
result = number1 + number2 + number_of_integer
name = "Rido"
print(result)

#to check type of a value 0> type(variable or value)

programming_languages = ["Python", "Java", "GO"]
list_of_numbers = [1,3,4,2,5, 3.14, -231, -3.1532]
random_value = ["python", 302, "Java", 3.12312]

language = programming_languages[0]

print(language)


# latihan  indexing
#latihan 1
langguage_go = programming_languages[2]
print(langguage_go)

#latihan 2
number_test = list_of_numbers[6]
print(number_test)
#latihan 3
random_value_test = random_value[3]
print(random_value_test)

print(type(random_value))

#akses dalam list support indexing negatif
result = list_of_numbers[-1]
print(list_of_numbers[-1])

#list bersifat mutable -> bisa berubah ubah
#tuple
tuple_of_numbers = (12 , 34, 45)
number = tuple_of_numbers[0]
print(number)
#tuple is not mutable/tidak bisa berubah

list_of_numbers = [1,3,4,2,5, 3.14, -231, -3.1532]
new_number = 23

list_of_numbers.append(new_number)
print(list_of_numbers)

programming_languages = ["Python", "Java", "GO"]
print(f"this is the list : {programming_languages}")
new_langguage = "C++"
print(f"New value is : {new_langguage}")
programming_languages.append(new_langguage)
print(programming_languages)
print(f"this is after .append = {programming_languages}")



list_new_languages = ["Rails", "Assembly"]
programming_languages.extend(list_new_languages)
print(programming_languages)

programming_languages.remove("Assembly")
print(programming_languages)

removed_value = programming_languages.pop(-1)
print(programming_languages)
print(removed_value)

list_of_numbers = [1,3,4,2,5, 3.14, -231, -3.1532]
list_of_numbers.remove(3.14)

print(list_of_numbers)
programming_languages.reverse()
print(programming_languages)

#SLICING
fruits = ["Banana", "Apple", "Watermelon", "Rambutan", "Dragonfruit"]

slicing = fruits[1:3]

slicing.append(fruits[4])
print(slicing)

hobbies = ["Swimming", "Hiking", "Reading", "Tiktok", "Making Content"]
hobbies[2] = "Watching Youtube"
hobbies[1] = "Claimbing"
print(hobbies)

#INSERT
hobby = "Playing Chess"
hobbies.insert(1, hobby)
print(hobbies)

hobby_1 = "Photography"
hobbies.insert(4,hobby_1)
print(hobbies)

