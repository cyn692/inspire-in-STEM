#writea program to check if a number is divisible by 5 or 7

num=int(input("Enter the number:"))
if(num%5==0) and (num%7==0):
    print(num," is divisible by 5 or 7")
else:
    print(num,"is not divisible by 5 or 7")