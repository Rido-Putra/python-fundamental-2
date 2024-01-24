'''number = (1, 2, 3)  # tuple -> immutable #list -> mutablle -> bisa dirubah2
number[1]
print(number)

# looping==> For Loop dan While
x = 1
while x < 10:
    print(x)
    x = x + 1
    print("Hello world")

print("Program has finished")
# x >= 13
y = 13
while y > 7:
    print(y)
    y = y - 1

number = [1, 2, 3]
for y in "ban ana":
    print(y)

for y in number:
    print(y)

fruits = ["papaya", "banana", "melon", "jackfruit"]
for fruit in fruits:
    if fruit == "melon":
        break
    print(fruit)
""""""
print("------------------------------")
for i in range(1, 10):  # print 1 - 9
    print(i)

for z in range(2, 6):
    print(z)


x = 1
y = 13
while x < 10 and y > 10:
    print(x)
    if x == 5 or y < 10:
        break
    x = x + 1
    y = y - 2


fruits = ["papaya", "banana", "melon", "jackfruit"]
for fruit in fruits:
    if fruit == "melon":
        continue
    print(fruit)

print("buah melon kena skip")

if "banana" in fruits:
    print("banana is in the fruits")

if "apel" not in fruits:
    print("apel is not in the fruits!!")

variable = "1234"
variable1 = int(variable)
print(variable1)
print(type(variable1))'''


# latihan
number = int(input("Enter a number : "))
count = 1
while count <= 10:
    product = number * count
    print(number, "x", count, "=", product)
    count = count + 1

number1 = int(input("Enter a number : "))
count = 10
while count >= 1:
    product = number1 * count
    print(number1, "x", count, "=", product)
    count = count - 1
