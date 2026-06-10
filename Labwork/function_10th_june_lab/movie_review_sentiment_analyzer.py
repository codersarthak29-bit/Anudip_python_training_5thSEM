'''
Movie reviews are stored as follows:

reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

Requirements:
1. count_sentiments(reviews)
   Counts:
   • Excellent
   • Good
   • Average
   • Poor reviews

2. most_common_word(reviews)
   Returns the most frequently occurring word.

3. longest_review(reviews)
   Returns the review containing the maximum number of characters.

4. reviews_with_keyword(reviews, keyword)
   Displays all reviews containing a given keyword.
'''

# ==========================================================
# Movie Review Analyzer
# ==========================================================

# List containing movie reviews
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# ----------------------------------------------------------
# Function: count_sentiments()
# Purpose : Count Excellent, Good, Average, and Poor reviews
# ----------------------------------------------------------
def count_sentiments(reviews):

    # Initialize sentiment counters
    excellent = 0
    good = 0
    average = 0
    poor = 0

    # Traverse through each review
    for review in reviews:

        # Check sentiment and update counter
        if "excellent" in review:
            excellent += 1

        elif "good" in review:
            good += 1

        elif "average" in review:
            average += 1

        elif "poor" in review:
            poor += 1

    # Return all sentiment counts
    return excellent, good, average, poor


# ----------------------------------------------------------
# Function: most_common_word()
# Purpose : Find the most frequently occurring word
# ----------------------------------------------------------
def most_common_word(reviews):

    # Create an empty dictionary to store word frequencies
    frequency = {}

    # Traverse through each review
    for review in reviews:

        # Split review into individual words
        words = review.split()

        # Count frequency of each word
        for word in words:

            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

    # Find the word with maximum frequency
    max_count = 0
    most_common = ""

    for word in frequency:

        if frequency[word] > max_count:
            max_count = frequency[word]
            most_common = word

    # Return the most common word
    return most_common


# ----------------------------------------------------------
# Function: longest_review()
# Purpose : Find the review with maximum characters
# ----------------------------------------------------------
def longest_review(reviews):

    # Assume the first review is the longest
    longest = reviews[0]

    # Traverse through all reviews
    for review in reviews:

        # Compare lengths of reviews
        if len(review) > len(longest):
            longest = review

    # Return the longest review
    return longest


# ----------------------------------------------------------
# Function: reviews_with_keyword()
# Purpose : Display reviews containing a given keyword
# ----------------------------------------------------------
def reviews_with_keyword(reviews):

    # Take keyword input from user
    keyword = input("Enter keyword to search: ")

    print("\nReviews containing keyword:", keyword)

    # Flag to check whether keyword is found
    found = False

    # Traverse through all reviews
    for review in reviews:

        # Check if keyword exists in review
        if keyword.lower() in review.lower():

            # Display matching review
            print(review)

            # Update flag
            found = True

    # If no matching review is found
    if found == False:
        print("No reviews found containing the keyword.")


# ==========================================================
# Main Program
# ==========================================================

# Count sentiments
excellent, good, average, poor = count_sentiments(reviews)

# Display sentiment counts
print("Excellent Reviews :", excellent)
print("Good Reviews      :", good)
print("Average Reviews   :", average)
print("Poor Reviews      :", poor)

# Display most common word
print("\nMost Common Word :", most_common_word(reviews))

# Display longest review
print("Longest Review   :", longest_review(reviews))

# Display reviews containing a keyword
reviews_with_keyword(reviews)