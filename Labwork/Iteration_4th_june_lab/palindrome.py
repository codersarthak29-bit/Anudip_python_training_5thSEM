# program to check its a palindrome or not and print the reverse of the number

num = int(input("Enter a number: "))

# store the original number for later comparison
original_num = num
reverse_num = 0 

while num > 0:
    digit = num % 10  # get the last digit
    reverse_num = reverse_num * 10 + digit  # build the reverse number
    num //= 10  # remove the last digit

print(f"The reverse of {original_num} is {reverse_num}.")

# check if the original number is equal to its reverse
if original_num == reverse_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")