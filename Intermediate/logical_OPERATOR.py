# Logical operations, 
# logical and, true when both side of the expression is true
# logical or, true when at least one side of the expression is true
# logical not, true when the expression is false

age = 18
is_sunny = True
of_age = age >= 18
is_rainning = False
is_hot = False

if (is_sunny or is_hot) and of_age and not is_rainning:
    print("WHAT IS GOING ON??")