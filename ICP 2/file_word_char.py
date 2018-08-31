# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:44:18 2018

@author: farid
"""
#getting the input file
fileName= input("What  file are the words  in? ")
infile= open(fileName,'r')
#declare the counter for word and character
word_count=1
char_count=0
#put the first line in line variable
line = infile.readline()
while line != "":
    #if there is a new line feed in a line, removing that line feed
    if line[len(line)-1]== "\n":
        p= len(line)-1
        text = line [0:len(line)-1]
    else:
        p=len(line)
        text = line
    #loop for word and character count
    for i in range(p):
        if line[i] == " ":
            word_count +=1
        if line[i] != " ":
            char_count +=1
    #printing the line with word and character number
    print ("%s %d,%d" %(text, word_count, char_count))
    #go to the next line
    line = infile.readline()
    #refresh the counter values
    word_count=1
    char_count=0
