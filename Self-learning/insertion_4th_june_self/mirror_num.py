#program to check whether the left half of a number is identical to the right half
num=input("Enter the number: ")
length=len(num)
if length%2!=0:
    print("Not a Mirror Number")
else:
    half = length // 2
    left = num[0:half]
    right = num[half:length]
    if left==right:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")