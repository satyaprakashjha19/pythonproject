#Getting input from users using for loop

from array import *
stu_roll = array('i', [])
n = int(input("enter no. of elements: "))

for i in range(n):
    stu_roll.append(int(input("enter elements: ")))

for i in range(len(stu_roll)):
    print(stu_roll[i])