# typecasting is when you want to turn a variable of some data type into another datatype

test_variable1 = "123"
test_variable2 = 123.2
test_variable3 = 0

# This is how you print the type of the variable
print(type(test_variable1))

# This is how you typecast into an int
# NOTE: when typecasting a floating number into a integer, it will be truncated/rounded down
int_typecast = int(test_variable1)

# This is how you typecase into a float
float_typecast = float(test_variable1)

# This is how you typecast into a string
string_typecast = str(test_variable2)

# This is how you typecast into a boolean
boolean_typecast = bool(test_variable3)