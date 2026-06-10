'''
Problem Statement:
A compressed message is given:

AAABBBCCCDDDAAA

Tasks:
1. Count occurrences of each character.
2. Create a dictionary of character frequencies.
3. Display unique characters.
4. Find the most frequent character.
5. Create a compressed output.
6. Calculate compression ratio.
'''

# ==========================================================
# Compressed Message Analyzer
# ==========================================================

# Original message
message = "AAABBBCCCDDDAAA"

# ----------------------------------------------------------
# Step 1 & 2: Count character frequencies
# ----------------------------------------------------------

# Create an empty dictionary
frequency = {}

# Traverse through each character
for ch in message:

    # Update frequency count
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# ----------------------------------------------------------
# Step 3: Display unique characters
# ----------------------------------------------------------

# Create list of unique characters
unique_characters = []

for ch in frequency:
    unique_characters.append(ch)

# ----------------------------------------------------------
# Step 4: Find the most frequent character
# ----------------------------------------------------------

most_frequent = ""
max_count = 0

for ch in frequency:

    if frequency[ch] > max_count:
        max_count = frequency[ch]
        most_frequent = ch

# ----------------------------------------------------------
# Step 5: Create compressed output
# ----------------------------------------------------------

compressed = ""

current_char = message[0]
count = 1

# Traverse from second character onwards
for i in range(1, len(message)):

    if message[i] == current_char:
        count += 1

    else:
        compressed += current_char + str(count)

        current_char = message[i]
        count = 1

# Add last character group
compressed += current_char + str(count)

# ----------------------------------------------------------
# Step 6: Calculate compression ratio
# ----------------------------------------------------------

original_length = len(message)
compressed_length = len(compressed)

compression_ratio = (compressed_length / original_length) * 100

# ==========================================================
# Output Section
# ==========================================================

print("Original Text:")
print(message)

print("\nCharacter Frequencies:")

for ch in frequency:
    print(ch, "->", frequency[ch])

print("\nUnique Characters:")
print(unique_characters)

print("\nMost Frequent Character:")
print(most_frequent)

print("\nCompressed Output:")
print(compressed)

print("\nOriginal Length:", original_length)
print("Compressed Length:", compressed_length)

print("\nCompression Ratio:", round(compression_ratio, 2), "%")