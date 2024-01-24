"""
name = input("Write your name here")
print(name)
age = input("How old are you?")
age_to_int = int(age)
print(age_to_int)
print(type(age_to_int))
"""
x = 1
while True:
    print(x)
    x = x + 1
    if x == 10:
        break

exit()
status = input("are you student?")
status = status.lower()
no_keywords = ["no", "0", "n", "tidak", "g"]
print(status)
if status == "yes" or status == "y" or status == "1":
    status = True
elif status in no_keywords:
    status = False
else:
    print("Please check your input!!!")
print(status)
