#!/bin/usr/python
#####################
#    Name : Cynthia Muriuki
#    palindroms
#    Date : 8/6/2022
###########################


#ask user to select  which input to check number or letter
#After user enters there input the programm should print in the input  user


number = (input("enter the number"))
if(number == number[:: -1]):
    print("the number is a palindrom")
else:
    print("the number is not a palindrom")
