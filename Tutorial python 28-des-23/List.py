numbers = [4,7,6,4,3]
strings = ["adi", "asep", "bagas"]
boolean = [True, False]
list_of_lists = [[1,2,3], [4,5,6]]

mixs = [[1,2,3], True, False, ["adi", "asep"], [4,5,6,7]]
list_name = [None]
list_name[0] #-> return a value

numbers[0]
numbers[2]
numbers[4] 

strings[-1]
strings[-3]

numbers = [4,7,6,4,3]

print(numbers[0:2])
# cara muter dari akhir sampai awal
print(numbers[::-1])

# method = cara python manipulasi sebuah data
# rumus = variabel."akan ada banyak method"
# .append -> untuk nambahkan sebuah value

strings = ["adi", "asep", "bagas"]
strings.app("doni")
# .extend -> mirip kaya append, tapi dia gabungin list original dan list baru jadi satu
# ie. original = [1,2,3] | values = [4,5,6] -> original.extend(values) -> [1,2,3,4,5,6]
new_names = ["Karla", "Joni", 'Supri']
strings.extend(new_names)
print(strings)
strings = ["adi", "asep", "bagas"]
numbers = [8,9,10]
strings.extend(numbers)
print(strings)

print("--------------.remove----------")
# menghapus/delete
# .remove | .pop -> intinya menghapus value didalam list
# .remove
strings = ["adi", "asep", "bagas"]
strings.remove("adi")
print(strings) #['asep', 'bagas']
print("--------------.pop-------------")
# .pop
strings = ["adi", "asep", "bagas"]
value = strings.pop(0)
print(strings) #['asep', 'bagas']
print(value)

values1 = [1, "hennny", 2, "asep"]
values1_test = values1.pop(2)
print(values1_test)
print(values1)

# tipe data tuple -> mirip 99% sepeerti list. tapi yg membedakan itu tuple immutable -> value didalamnya itu nggk bisa diganti2
# list mutable -> bisa diganti-ganti

tuple_values = (4,3,"asep", "asep")
name = tuple_values[-1]
print(tuple_values[-1]) # "asep"
print(name) # "asep"
name_count = tuple_values.count("asep")
print(name_count) # 2
name_index = tuple_values.index("asep")
print(f"index asep ada di nilai = {name_index}")

