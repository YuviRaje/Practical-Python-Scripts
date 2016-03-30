#!/usr/bin/env python
import csv #importing the csv module
txtfile=open("REST_Curl_Log Component.txt",'w')  #opening a file in read mode
entry=" " #an empty string 
while entry.upper()!='QUIT': #getting user input unless he types 'quit'
    entry=str(input('Write something to file in a Name, age format')) #have the input in entry
    if entry=='quit' or QUIT: 
        break #break from loop if quit pressed
    else:
        txtfile.write(str(entry)+'\n') #writing the entry to the file with a new line after each entry
txtfile.close() #closing the file for saving the values   

txtfile=open('REST_Curl_Log Component.txt','r') #opening the file again in read mode
data=txtfile.readlines() #readine the data line by line 
print (data)

with open ('anewfile.csv','w') as csvfile: #created a csv file and say it csvfile in the program
    writer=csv.writer(csvfile,delimiter='\n', quoting=csv.QUOTE_ALL) #this is the default csv writer. we have the csv file name, the delimiter which is in our case is newline character and quoting to say to quote all the inputs, don't care if the value is numeric or not.
    for line in data: #Getting to each line of the data
        line=line.split() #splitting the data by white space
       # print line
        writer.writerow(line) #write line to csv file as row basis 
    csvfile.close() #closing the file 
    print ("Successfully Done")
f=open('anewfile.csv','r') #Opening the csv file
rows=csv.reader(f) #read the content to rows
for line in rows : #display each row
    print (line)
