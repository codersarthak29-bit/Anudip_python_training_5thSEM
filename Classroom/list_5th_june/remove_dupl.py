'''Program to create a list of 20 number given by the user. 
ask the user to input any other number .
Remove all the duplicate eneteries of this number from the list'''

numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Taking a num which user want to remove the duplicates from the list
num_to_remove = int(input("Enter a number to remove from the list: "))
count=numbers.count(num_to_remove)
if (count==1):
    print(num_to_remove," is not repeated")
elif(count==0):
    print("Element not found!!")
else:
    numbers.reverse()
    for i in range(1,count):
        numbers.remove(num_to_remove)
    numbers.reverse()

print("List after removing duplicates of ",num_to_remove,":",numbers)

