# Program: Research Abstract Similarity Check

abstract1 = "Artificial intelligence is transforming education and healthcare."
abstract2 = "Healthcare and education are rapidly transforming through artificial intelligence."

# Convert abstracts into sets of words
words1 = set(abstract1.lower().replace(".", "").split())
words2 = set(abstract2.lower().replace(".", "").split())

# 2. Identify common words
common_words = words1.intersection(words2)

# 3. Identify unique words in each abstract
unique1 = words1.difference(words2)
unique2 = words2.difference(words1)

# 4. Calculate percentage similarity
all_words = words1.union(words2)
similarity = (len(common_words) / len(all_words)) * 100

# Display results
print("Common Words:")
print(common_words)

print("\nUnique Words in Abstract 1:")
print(unique1)

print("\nUnique Words in Abstract 2:")
print(unique2)

print("\nSimilarity Percentage:")
print(f"{similarity:.1f}%")

# 5. Check plagiarism review requirement
print("\nPlagiarism Review Required:")
if similarity > 50:
    print("Yes")
else:
    print("No")