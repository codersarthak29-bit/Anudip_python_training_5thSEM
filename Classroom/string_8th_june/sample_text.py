# Program to count the number of special characters in a sentence

sentence = input("Enter a sentence: ")
length=0
count1 = 0
for ch in sentence:
    length+=1
    if not ch.isalnum() :
        count1 += 1
print("Number of special characters =", count1)
print("Number of characters =", length)
