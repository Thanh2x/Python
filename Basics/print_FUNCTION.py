# Normal print method, once executed it will automatically add a newline character
print("This is a print statement")

# Print method where you can set the ending character to be some other than the newline character
print("This is a print statement", end = " helo!\n")

# Formatted print method where you can put variables inside the string
# the print method basically prints what is called a formatted string, which you can have other variables inside of it
formatted_variable1 = "!!!"
formatted_variable2 = 1
print(f"Th{formatted_variable2}s is a formatted print statement {formatted_variable1}")

