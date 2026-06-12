'''Problem Statement 
A text file contains the following paragraph. 
Sample Input/Data (article.txt) 
Python is easy to learn. 
Python is powerful. 
Python supports multiple programming paradigms. 
Programming with Python is enjoyable. 
Tasks 
1. Count the total number of words.  
2. Count the frequency of each word.  
3. Find the most frequently occurring word.  
4. Display words appearing only once.  
Display all unique words. 
'''
# Read the file
file = open("article.txt", "r")
text = file.read().lower()
file.close()

# Remove punctuation
text = text.replace(".", "")

# Split into words
words = text.split()

# 1. Count total number of words
total_words = len(words)
print("Total Number of Words:", total_words)

# 2. Count frequency of each word
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")
for word in frequency:
    print(word, ":", frequency[word])

# 3. Find the most frequently occurring word
most_word = ""
max_count = 0

for word in frequency:
    if frequency[word] > max_count:
        max_count = frequency[word]
        most_word = word

print("\nMost Frequently Occurring Word:", most_word)
print("Frequency:", max_count)

# 4. Display words appearing only once
print("\nWords Appearing Only Once:")
for word in frequency:
    if frequency[word] == 1:
        print(word)

# 5. Display all unique words
print("\nUnique Words:")
for word in frequency:
    print(word)