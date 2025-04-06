# This is how you access a string character via indexing
full_name = "Thanh PRO 123"
first_character = full_name[0]
print(f"The first character of my name is {first_character}")

# This is how to substring using indexing, last index is exclusive
first_name = full_name[0 : 5]
print(f"My first name is {first_name}")

# This is how you can use the step method to skip over (first character is inclusive)
randomString = "2002002002002002"
two_only = randomString[0 : len(randomString) : 3]
print(f"Skipping over 3 hops each time we get {two_only}")

# This is how you can step back wards to reverse a string
secret_message = "uoy evoL I"
reversed = secret_message[ : : -1]
print(f"The revresed message is {reversed}")