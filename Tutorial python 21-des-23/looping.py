# while loops, dan for loops

number = 6
number2 = 0
while number > 5:
    number2 = number2 + 1
    print(number2)
    if number2 == 100:
        print("number2 value is " + str(number2))
        break

number1 = 6
number2 = 0
number_string = "32"
if type(number1) == type(int(number_string)):
    print("they're equal")

if number1 == number2:
    print("they're not equal")
elif number1 < number2: 
    print("they're not the same")
else:
    print("All condition is not met")