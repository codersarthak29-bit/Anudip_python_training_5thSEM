#program to find the longest increasing subsequence in a list of numbers

n = int(input("Enter number of elements: ")) #input from user to specify the number of elements in the list

print("Enter elements:")
prev = int(input()) #input the first element and store it in the variable 'prev' to compare with the next elements

current_length = 1
max_length = 1

for i in range(n - 1):
    num = int(input()) #input each subsequent element and store it in the variable 'num'

    if num > prev: 
        current_length += 1
        '''if the current number is greater than the previous number,
        it means we are still in an increasing sequence, 
        so we can increment the current length'''
    else: 
        current_length = 1
        '''if the current number is not greater than the previous number,
        it means we have broken the increasing sequence,
        so we reset the current length to 1'''

    if current_length > max_length:
        max_length = current_length

    prev = num

print("Longest Sequence Length =", max_length)