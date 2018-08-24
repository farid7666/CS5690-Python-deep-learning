# -*- coding: utf-8 -*-

#inverting a word
def invert(name):
    j=len(name)
    j=j-1
    name1=[]
    while j>-1:
        name1.append(name[j])
        j=j-1
    return name1

#taking first and last name as input
First=input ('Please enter first name: ')
Second=input ('Please enter second name: ')

#inverting first and last name
a=invert(Second)
a=''.join(a)
b=invert (First)
b=''.join(b)

#print the invert name
print('\nName is', b, a)

#taking two numbers as input
numstring1=input ('Please insert an integer: ')
numstring2=input ('Please insert 2nd integer: ')

num1=int (numstring1)
num2=int (numstring2)
b=num1+num2 #addition
c=abs(num1-num2) #substraction
d=num1*num2 #mutiplication
e=num1/num2 #division

#printing the results
print ('\nThe sum of',num1, 'and', num2, 'is' ,b)
print ('The difference between',num1, 'and', num2, 'is' ,c)
print ('The mutiplication of',num1, 'and', num2, 'is' ,d)
print ('The division of',num1, 'and', num2, 'is' ,e)
