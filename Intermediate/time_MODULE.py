import time

# The time.sleep(number) function sleeps for number of seconds, and then continue where the program left off

count = int(input("How many seconds do you want to count down?\n"))

for x in reversed(range(0, count + 1)):
    time.sleep(1)
    print(x)


print("WOOOO HOOO")