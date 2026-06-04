#Program to check that if the number is a strong number or not
#Taking input from the user
num=int(input("Enter a number: "))
while num<0:
    print("Please enter a positive number")
    num=int(input("Enter a number: "))
#Initializing sum to 0
sum=0
#Finding the sum of the factorial of the digits
temp=num
while temp>0:
    digit=temp%10
    factorial=1
    for i in range(1,digit+1):
        factorial*=i
    sum+=factorial
    temp//=10

#Checking if the number is a strong number
if num==sum:
    print(num,"is a strong number")
else:
    print(num,"is not a strong number")