'''Problem Statement 
A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words.  
 
Sample Output 
Total Words: 8 
 
Word Frequencies: 
This -> 1 
product -> 1 
is -> 1 
excellent -> 3 
and -> 1 
very -> 1 
useful -> 1 
 
Most Frequent Word: excellent 
 
Words Appearing Once: 
['This', 'product', 'is', 'and', 'very', 'useful'] 
 
Unique Words: 
['This', 'product', 'is', 'excellent', 'and', 'very', 'useful']'''
# Program to perform various operations on a customer review

# Taking review as input from the user
review = input("Enter Review: ")

print("\nReview:")
print(review)

# --------------------------------------------------
# Task 1: Count total words
# --------------------------------------------------

# Splitting the review into words
words = review.split()

# Counting total words
total_words = len(words)

print("\nTotal Words:", total_words)

# --------------------------------------------------
# Task 2: Create a dictionary containing
# word frequencies
# --------------------------------------------------
frequency = {}

# Counting frequency of each word
for word in words:

    # Adding new word or increasing its count
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")

# Displaying word frequencies
for word, count in frequency.items():
    print(word, "->", count)

# --------------------------------------------------
# Task 3: Find the most frequently used word
# --------------------------------------------------

# Assuming the first word has the highest frequency
most_frequent_word = list(frequency.keys())[0]
highest_frequency = list(frequency.values())[0]

# Traversing the frequency dictionary
for word, count in frequency.items():

    # Updating highest frequency and word
    if count > highest_frequency:
        highest_frequency = count
        most_frequent_word = word

print("\nMost Frequent Word:", most_frequent_word)

# --------------------------------------------------
# Task 4: Find all words appearing only once
# --------------------------------------------------
single_words = []

# Checking frequency of each word
for word, count in frequency.items():

    # Adding words that appear only once
    if count == 1:
        single_words.append(word)

print("\nWords Appearing Once:")
print(single_words)

# --------------------------------------------------
# Task 5: Count words having more than 5 characters
# --------------------------------------------------
count = 0

# Checking length of each word
for word in words:

    # Incrementing count if length is greater than 5
    if len(word) > 5:
        count += 1

print("\nWords Having More Than 5 Characters:", count)

# --------------------------------------------------
# Task 6: Display words in reverse order
# --------------------------------------------------
print("\nWords in Reverse Order:")

# Displaying words from last to first
for word in words[::-1]:
    print(word, end=" ")

# --------------------------------------------------
# Task 7: Create a list of unique words
# --------------------------------------------------
unique_words = []

# Adding words only if not already present
for word in words:

    # Checking uniqueness
    if word not in unique_words:
        unique_words.append(word)

print("\n\nUnique Words:")
print(unique_words)