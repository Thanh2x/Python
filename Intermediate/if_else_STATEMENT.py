# if statements execute all the code below it indent by 1 to the right if the expression is true
is_sunny = True
if is_sunny:
    print("IT IS SUNNY TODAY!")

# if else statements execute if the if expression is true, else execute the other
age = 15
if age >= 18:
    print("YOU ARE OLD ENOUGH")
else:
    print("YOU ARE NOT OLD ENOUGH")

# if else if statements execute if the first if statment is true, else if the second and so on is true
is_sunny = False
is_rainning = True
if is_sunny:
    print("IT IS SUNNY TODAY")
elif is_rainning:
    print("IT IS RAINNING TODAY")
else:
    print("GOOD WEATHER I HOPE")

