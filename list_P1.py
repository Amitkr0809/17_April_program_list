#  find the differences of two lists

list1 = [10,20,30,40,50,80]
list2 = [10,30,50,60,20,70]

set1 = set(list1)
set2 = set(list2)
print("Difference of two list is :",(set1 - set2))


print ("common of two list is : ",(set1 & set2 ))

