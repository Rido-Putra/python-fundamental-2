name = input("What is your name?")
print("Hallo" + " " + name)

location = input("Where do you live?")
print(location + " " + "is near here!")

mood = input("What was your day? perfect, nice, bad")
check = ""
#mood1= int(mood)
try:
    mood = int(mood)
except ValueError:
    pass

if type(mood) == type(check): #input must be a str
    print('Awesome, what wonderful day, Yesterday was "History", Tomorrow is "Mystery",Today is a gift that is why it called "Present"')
elif type(mood) != type(check): #input must be an int
    print('Hmmm, something smeel fishy!!!, please check your input')
else:
    print('Wish you have a great opportunity to find happiness')

print(type(mood))