#Program to check if a number is an Armstrong number or not
#Taking input from the user
num=int(input("Enter a number: "))
#Finding the number of digits in the number
order=len(str(num)) 
#Initializing sum to 0
sum=0
#Finding the sum of the digits raised to the power of the number of digits
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
#Checking if the number is an Armstrong number
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")