#program to check if a number is a mountain number or not
num = input("Enter a number: ") #input from user, taken as a string to process each digit easily

peak_found = False #flag to indicate whether a peak has been found in the number, initialized to False
flag = True #flag to indicate whether the number is a mountain number or not, initialized to True

for i in range(1, len(num)): #loop to process each digit of the number starting from the second digit
    
    if not peak_found: #if a peak has not been found yet, we are still going up the mountain
        if num[i] > num[i-1]: #if the current digit is greater than the previous digit, it means we are still going up the mountain, so we can
            continue
        elif num[i] < num[i-1]: #if the current digit is less than the previous digit, it means we have found a peak and we are now going down the mountain
            peak_found = True
        else: #if the current digit is equal to the previous digit, it means the number cannot be a mountain number
            flag = False
            break
    
    else: #if a peak has been found, we are now going down the mountain
        if num[i] >= num[i-1]:
            flag = False
            break

if flag and peak_found: #if the flag is still True and a peak has been found, it means the number is a mountain number
    print(num, "is a mountain number")
else:
    print(num, "is not a mountain number")