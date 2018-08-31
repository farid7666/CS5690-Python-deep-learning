# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:07:45 2018

@author: farid
"""
#Give the number of elements in the list
n=eval(input("How many numbers do you have?"))
#create an empty list
list1=[]
# loop for getting the elements of the list
for i in range(n):
    x=int(input("enter a number"))
    list1.append(x)
#print the list
print("the list is",list1)

a=list1[0]
b=list1[n-1]
tuple1=(a,b)
#print the tuple containing the first and last element of the list
print ("the tuple is", tuple1)