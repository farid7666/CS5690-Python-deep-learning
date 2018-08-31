# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:17:27 2018

@author: farid
"""
#To display the first letter of my name
#n is the font size
def display(n):
    #outer loop for print
    for i in range(n):
        #inner loop for print
        for j in range((n // 2)+1):
            #condition for print *
            if (i == 0 or i == n // 2) or (j==0 and j<(n//2)+1):
                print("*", end = "")
            else:
                print(" ", end = "")
        print()
     
#calling the function      
display(10)