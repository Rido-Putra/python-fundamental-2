name = input("What is your name?")
print("Hallo" + " " + name)

location = input("Where do you live?")
print(location + " " + "is near here!")

mood = input("What was your day? perfect, nice, bad")
mood1= int(mood)
if type(mood1) == type((mood)):
    print('Awesome, what wonderful day, Yesterday was "History", Tomorrow is "Mystery",Today is a gift that is why it called "Present"')
elif type(mood1) != type((mood)):
    print('Hmmm, something smeel fishy!!!, please check your input')
else:
    print('Wish you have a great oppotunity to find happiness')

print(type(mood))