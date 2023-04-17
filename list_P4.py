# Program to Create two lists with EVEN numbers and ODD numbers from a list

list = [10,11,25,67,66,88,89,87]
evenlist = []
oddlist = []


for i in list:
    if i % 2 ==0:
        evenlist.append(i)
    else:
        oddlist.append(i)

print("evenlist = ", evenlist)
print("oddlist = ", oddlist)

