#!/usr/bin/python

number = list(range(1, 21))
n = 1

for i in range(1, 20):
    n = n * number[i]
    for j in range(i):
        if number[i] % number[j] == 0:
            n = n / number[j]
            number[i] = number[i] / number[j]
print(n)
