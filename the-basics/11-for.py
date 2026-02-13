# for loop = used to iterate over a sequence (string, list, tuple,set)
# repeat a block of code an exact amount of times

import time

for i in range(1, 11, 4):
    print(i)

name = "Bro code"
for letter in name:
    print(letter, end="-")

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("HAPPY NEW YEAR!")
