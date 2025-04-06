# This is how to get the length of a string
test_string = "HelloABC123o"
length = len(test_string)
print(f"{test_string} has a length of {length}")

# This is how to find a substring within a string, it returns the index of the first occurence substring
index = test_string.find("ABC")
print(f"The first index of the string ABC is {index}")

# This is how to find a substirng within a string, such that it is the last occurence in the string
indexLast = test_string.rfind("o")
print(f"The last occurence of the letter o is at index {indexLast}")

# This is how to capitalize the first character of a string
name = "thanh"
name = name.capitalize()
print(f"Capitalized: {name}")

# This is how to make every letter in a string be upper case
name = name.upper()
print(f"Uppered: {name}")

# This is how to make every letter in a string to be lower case
name = name.lower()
print(f"lowered: {name}")

# This is how to test if a string only contains digits
test_string2 = "1232"
is_digit = test_string2.isdigit()
if is_digit:
    print("String only contains digits")

# This is how to test if a string only contains letters
test_string3 = "asadah"
is_alpha = test_string3.isalpha()
if is_alpha:
    print("String only contains alphabets")

# This is how to count the number of occurence of something within a string
binary_string = "1110111010110111110"
count = binary_string.count("110")
print(f"There are {count} numbers of 110s substrings")

# This is how to replace a substring within a string with another substring
string_replace = "Hello what is REPLACE THIS my dude?"
replaced = string_replace.replace("REPLACE THIS", "good")
print(replaced)



# For more information, do print(help(str)) for more strings methods and comprehensive explanations
