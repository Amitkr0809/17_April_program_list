# Program to print all numbers which are divisible by M and N in the List

list = [10,15,27,40,30,89,4]
M = 3
N = 5

for num in list:
    if (num % M == 0 and num % N ==0):
        print(num)
