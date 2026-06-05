#program to check if the secert code is valid or not, it contains exactly 6 digits and sum of first 3 digits is equal to the sum of last 3 digits
code = input("Enter the secert code: ") #input from user, taken as a string to process each character easily
flag = True #flag to indicate whether the secert code is valid or not, initialized to True

if len(code) != 6: #check if the length of the code is not equal to 6, if it is not, then the code is not valid
    flag = False
else:
    sum_first_3=0 #variable to store the sum of the first 3 digits, initialized to 0
    sum_last_3=0 #variable to store the sum of the last 3 digits, initialized to 0
    for i in range(3): #loop to calculate the sum of the first 3 digits
        sum_first_3 += int(code[i])
    for i in range(3, 6): #loop to calculate the sum of the last 3 digits
        sum_last_3 += int(code[i])
    if sum_first_3 != sum_last_3: 
        flag = False
        '''check if the sum of the first 3 digits is not equal to the sum of the last 3 digits,
          if it is not, then the code is not valid'''

if flag:
    print("The secert code is valid.")
else:
    print("The secert code is not valid.")