#program to find all the pairs of consecutive numbers

numbers = [4, 5, 6, 10, 11, 15, 16, 17]

numbers1 = []

for i in range(len(numbers) - 1):
    if numbers[i + 1] == numbers[i] + 1:
        print(numbers[i],"and",numbers[i+1],"are consecutive")
        numbers1.append((numbers[i], numbers[i + 1]))

print("Consecutive pairs:", numbers1)