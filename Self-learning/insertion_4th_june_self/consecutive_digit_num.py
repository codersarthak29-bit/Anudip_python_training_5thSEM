#program to accept a number and check whether every digit is exactly 1 greater than its previous digit or not
num=int(input("Enter a number: ")) #input from user
temp=num #temporary variable to store the number for processing
prev=-1 #variable to store the previous digit, initialized to -1
flag=True #flag to indicate whether the number is a consecutive digit number or not, initialized to True
while temp>0: #loop to process each digit of the number 
    digit=temp%10
    if prev!=-1 and digit!=prev-1: #check if the current digit is not 1 greater than the previous digit
        flag=False
        break #exit the loop if the condition is not satisfied
    prev=digit
    temp//=10
if flag: #if the flag is still True, it means the number is a consecutive digit number
    print(num,"is a consecutive digit number.") 
else:    print(num,"is not a consecutive digit number.")   #if the flag is False, it means the number is not a consecutive digit number 
