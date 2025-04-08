# While loops, while loops continue to execute if the condition remain true
name = input("Enter your name\n")

while name == "":
    name = input("Please enter your name")

print(f"Hello {name}!")

# for loops, execute a block of code a fixed number of times,
# you can iterate over a range(), string, sequence, something that is iteratable

for x in range(0, 10, 1):
    print(f"{x} ", end = "")

print()

# NOTE: the range function, returns a list, from start to end -1, you can add a third argument if you want to step
for x in range(0, 10, 2):
    print(f"{x} ", end = "")

print()

for x in name:
    print(f"{x} ", end = "")

print()

# You can iterate in reversed order using the reversed() function
# The reversed function basically reverse the list and returns it to you

for x in reversed(range(0, 10)):
    print(f"{x} ", end = "")

print()

# Break and continue statement, break stops the loop immediately, and continue goes to the next iteration

for x in range(0, 20):
    if (x == 13):
        continue
    if (x == 17):
        break
    print(f"{x} ", end = "")

print()