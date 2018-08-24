# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:50:28 2018

@author: farid
"""
#input sentence
sentence = input("write down the sentence: ")
#length of the sentence
length = len(sentence)

#counter for digit and letter
digit = 0
letter = 0

#loop for counting digits and letters
for i in range(length):
    temp=sentence[i]
    if temp.isdigit():
        digit +=1
    if temp.isalpha():
        letter +=1

#printing number of letters and digits
print ("Number of digits in the sentence:", digit)
print ("Number of the letters in the sentence", letter)

        
    
