'''A chat application stores a message: 
Python is awesome and Python is easy to learn 
Tasks 
Write a program to: 
1. Count total characters.  
2. Count total words.  
3. Find the longest word.  
4. Find the shortest word.  
5. Count how many times the word "Python" appears.  
6. Create a list of words having more than 4 characters.  
7. Display all words starting with a vowel.  
8. Count the number of vowels and consonants.  
Sample Output 
Message: 
Python is awesome and Python is easy to learn 
 
Total Characters: 45 
Total Words: 8 
 
Longest Word: awesome 
Shortest Word: is 
 
Occurrences of Python: 2 
 
Words Longer Than 4 Characters: 
['Python', 'awesome', 'Python', 'learn'] 
 
Vowels: 16 
Consonants: 22'''
# Program to perform various operations on a message

# Message stored in a string
message = "Python is awesome and Python is easy to learn"

print("Message:")
print(message)

# --------------------------------------------------
# Task 1: Count total characters
# --------------------------------------------------

# Counting total characters in the message
total_characters = len(message)

print("\nTotal Characters:", total_characters)

# --------------------------------------------------
# Task 2: Count total words
# --------------------------------------------------

# Splitting the message into words
words = message.split()

# Counting total words
total_words = len(words)

print("Total Words:", total_words)

# --------------------------------------------------
# Task 3: Find the longest word
# --------------------------------------------------

# Assuming the first word is the longest initially
longest_word = words[0]

# Traversing the word list
for word in words:

    # Updating longest word if a longer word is found
    if len(word) > len(longest_word):
        longest_word = word

print("\nLongest Word:", longest_word)

# --------------------------------------------------
# Task 4: Find the shortest word
# --------------------------------------------------

# Assuming the first word is the shortest initially
shortest_word = words[0]

# Traversing the word list
for word in words:

    # Updating shortest word if a shorter word is found
    if len(word) < len(shortest_word):
        shortest_word = word

print("Shortest Word:", shortest_word)

# --------------------------------------------------
# Task 5: Count how many times the word
# "Python" appears
# --------------------------------------------------
python_count = 0

# Checking each word
for word in words:

    # Incrementing count if word is Python
    if word == "Python":
        python_count += 1

print("\nOccurrences of Python:", python_count)

# --------------------------------------------------
# Task 6: Create a list of words having
# more than 4 characters
# --------------------------------------------------
long_words = []

# Adding words with length greater than 4
for word in words:

    # Checking word length
    if len(word) > 4:
        long_words.append(word)

print("\nWords Longer Than 4 Characters:")
print(long_words)

# --------------------------------------------------
# Task 7: Display all words starting with a vowel
# --------------------------------------------------
vowel_words = []

# Checking each word
for word in words:

    # Checking if the first letter is a vowel
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

print("\nWords Starting With a Vowel:")
print(vowel_words)

# --------------------------------------------------
# Task 8: Count the number of vowels
# and consonants
# --------------------------------------------------
vowel_count = 0
consonant_count = 0

# Checking each character in the message
for ch in message.lower():

    # Considering only alphabetic characters
    if ch.isalpha():

        # Checking for vowels
        if ch in "aeiou":
            vowel_count += 1

        # Remaining alphabetic characters are consonants
        else:
            consonant_count += 1

print("\nVowels:", vowel_count)
print("Consonants:", consonant_count)