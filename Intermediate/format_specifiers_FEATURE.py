# Formatt specifiers help you format your print statement outputs
# {values:flags}
# .numberf = round to that many decimal places
pie = 3.14565
print(f"rounded to 2 decimal place is {pie:.2f}")

# :number = allocate that many space of the value (space padding)
# :0number = allocated that many space and 0 pads it
# :< left justify, basically it is from left to right
# :> right justify
# :^ center align
print(f"center aligned: {pie:^10}")

# :+ print a plus sign to indicate positive vavllue
# := place a sign to leftmost position
print(f":= {pie: }")

# :  insert a sign to leftmost postion
# :, comma separator, like 1000 is 1,000

# NOTE: you can mix and match all these
pie = 230123.32123
print(f"Some mixes of format specifiers: {pie:+^15.3f}")

