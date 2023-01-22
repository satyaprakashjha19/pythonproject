#Getting input from users using for loop

from array import *
stu_roll = array('i', [])
n = int(input("enter no. of elements: "))

for i in range(n):
    stu_roll.append(int(input("enter elements: ")))

for i in range(len(stu_roll)):
    print(stu_roll[i]) 


# Getting input from user using while loop

from array import *
stu_roll1 = array('i', [])
n = int(input("enter no. of elements:"))

i = 0
while i<n:
    stu_roll1.append(int(input("enetr elements: ")))
    i+=1

j = 0
while (j<len(stu_roll1)):
    print(stu_roll1[j])
    j+=1
