#!/usr/bin/env python3
import os

with open("hw.txt", "w") as homework:
    for i in range(0, 369):
        homework.write("{} I am not a failure".format(i))
    homework.close()

for i in range(0, 10 + 1):
    os.system("cat hw.txt >> hw{}.txt".format(i))

print("Good girl")
