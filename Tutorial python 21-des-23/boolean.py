True
False

number1 = 1
number2 = 2

if number1 == number2:
    print(False)

fruits = []
while True:
    fruit = input("Insert your fruit here, input break to stop inputting : ")
    fruits.append(fruit)
    print(fruits)
    if fruit == "0":
        print("Hello world")
        break

