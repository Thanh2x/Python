# A list is basically an array or a vector, that is indexable, ordered and changeable, duplicates are allowed

# Empty list
my_list1 = []

my_list2 = [1,2]
# If need help print this line
print(help(my_list2))
print(dir(my_list2))

# Initializing a list
names = [ "Thanh", "Pro", "Jayden"]

# You can add new element by using append() method

names.append("ADLSA")
for name in names:
    print(f"{name} ", end = "")
print()

# List indexing

my_name = names[0]

# List in loops, the variable acts as an alias for the elements in the list

for name in names:
    print(f"{name} ", end = "")
print()

# You can also do indexing like how you do with strings

subnames = names[0 : 2]

for name in subnames:
    print(f"{name} ", end = "")
print()

subnamesSkip = names[0 : : 2]

for name in subnamesSkip:
    print(f"{name} ", end = "")
print()

reversedNames = names[::-1]


for name in reversedNames:
    print(f"{name} ", end = "")
print()

# There are many more method for a list, like
# len()
# clear()
# copy()
# count()
# extend()
# and many more, print help(a list) for more information
