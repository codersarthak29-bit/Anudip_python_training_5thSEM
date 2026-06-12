# Program: Trending Hashtag Analysis

# Read hashtags from file
file = open("hashtags.txt", "r")

hashtags = []
for line in file:
    hashtags.append(line.strip())

file.close()

# 1. Count occurrences of each hashtag
frequency = {}

for tag in hashtags:
    if tag in frequency:
        frequency[tag] += 1
    else:
        frequency[tag] = 1

print("Hashtag Frequency:")
for tag, count in frequency.items():
    print(tag, ":", count)

# 2. Display the top trending hashtag(s)
max_count = max(frequency.values())

print("\nTop Trending Hashtags:")
for tag, count in frequency.items():
    if count == max_count:
        print(tag)

# 3. Create a set of unique hashtags
unique_hashtags = set(hashtags)

print("\nUnique Hashtags:")
print(unique_hashtags)

# 4. Identify hashtags used more than twice
print("\nHashtags Used More Than Twice:")
popular_tags = []

for tag, count in frequency.items():
    if count > 2:
        print(tag)
        popular_tags.append(tag)

# 5. Generate a trend report file
file = open("trend_report.txt", "w")

file.write("Hashtag Frequency:\n")
for tag, count in frequency.items():
    file.write(f"{tag} : {count}\n")

file.write("\nTop Trending Hashtags:\n")
for tag, count in frequency.items():
    if count == max_count:
        file.write(tag + "\n")

file.close()

print("\nTrend Report Generated Successfully.")