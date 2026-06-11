# ==========================================================
# NEWS ARTICLE ANALYZER
# ==========================================================
# This program analyzes a news article and generates:
# 1. Total Characters
# 2. Total Words
# 3. Total Sentences
# 4. Vowels and Consonants
# 5. Longest Word
# 6. Shortest Word
# 7. Most Frequent Word
# 8. Word Frequency Dictionary
# 9. Words Appearing Only Once
# 10. Words Appearing More Than 5 Times
# 11. Words Starting With Each Alphabet
# 12. All Unique Words
# Challenge:
# Complete Text Summary
# ==========================================================


# Article containing 300+ words
article = """
Technology has transformed the way people communicate, learn, work,
and conduct business. The internet has made information accessible
to millions of people across the world. Students use online resources
for learning, professionals collaborate using digital tools, and
organizations depend on technology to improve productivity.

Artificial intelligence is one of the fastest-growing fields in
technology. It helps businesses automate repetitive tasks and improve
decision-making. Machine learning systems analyze large volumes of
data and identify patterns that would be difficult for humans to
detect. These technologies are being used in healthcare, finance,
education, transportation, and many other industries.

The growth of cloud computing has enabled organizations to store
and process data efficiently. Businesses can scale their operations
without investing heavily in physical infrastructure. Cybersecurity
has also become increasingly important because digital systems are
frequently targeted by attackers. Companies invest significant
resources in protecting sensitive information.

Technology continues to evolve rapidly. Researchers are developing
innovative solutions that improve quality of life. Governments,
businesses, and educational institutions are working together to
ensure that technology is used responsibly and effectively. The
future of technology promises new opportunities, greater efficiency,
and improved connectivity for people around the world.

Technology is important because technology improves communication.
Technology also improves learning and technology improves business.
Many people use technology every day because technology has become
an essential part of modern life.
"""


# ==========================================================
# Function to clean words
# Removes punctuation and converts to lowercase
# ==========================================================
def get_words(text):

    words = []

    for word in text.split():

        cleaned_word = word.strip(".,!?;:()[]{}\"'").lower()

        if cleaned_word != "":
            words.append(cleaned_word)

    return words


# ==========================================================
# Function to count vowels and consonants
# ==========================================================
def count_vowels_consonants(text):

    vowels = 0
    consonants = 0

    for char in text.lower():

        if char.isalpha():

            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


# ==========================================================
# Function to create word frequency dictionary
# ==========================================================
def create_frequency_dictionary(words):

    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# ==========================================================
# Function to count words starting with each alphabet
# ==========================================================
def count_starting_alphabets(words):

    alphabet_count = {}

    for word in words:

        first_letter = word[0].upper()

        if first_letter.isalpha():

            if first_letter in alphabet_count:
                alphabet_count[first_letter] += 1
            else:
                alphabet_count[first_letter] = 1

    return alphabet_count


# ==========================================================
# Function to analyze article
# ==========================================================
def analyze_article(text):

    # Validation 1
    if text.strip() == "":
        print("Article is empty.")
        return

    words = get_words(text)

    # Validation 2
    if len(words) == 0:
        print("No valid words found.")
        return

    # Count characters excluding spaces
    total_characters = len(text.replace(" ", "").replace("\n", ""))

    # Count words
    total_words = len(words)

    # Count sentences
    total_sentences = (
        text.count(".")
        + text.count("?")
        + text.count("!")
    )

    # Validation 3
    if total_sentences == 0:
        total_sentences = 1

    vowels, consonants = count_vowels_consonants(text)

    frequency = create_frequency_dictionary(words)

    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)

    most_frequent_word = max(
        frequency,
        key=frequency.get
    )

    # --------------------------------------------------
    # Display Results
    # --------------------------------------------------
    print("TEXT ANALYSIS REPORT")
    print("=" * 60)

    print("Total Characters :", total_characters)
    print("Total Words      :", total_words)
    print("Total Sentences  :", total_sentences)
    print("Vowels           :", vowels)
    print("Consonants       :", consonants)
    print("Longest Word     :", longest_word)
    print("Shortest Word    :", shortest_word)

    print(
        "Most Frequent Word :",
        most_frequent_word,
        "(",
        frequency[most_frequent_word],
        "times )"
    )

    # --------------------------------------------------
    # Word Frequency Dictionary
    # --------------------------------------------------
    print("\nWORD FREQUENCY DICTIONARY")
    print("=" * 60)

    print(frequency)

    # --------------------------------------------------
    # Words appearing only once
    # --------------------------------------------------
    print("\nWORDS APPEARING ONLY ONCE")
    print("=" * 60)

    found = False

    for word, count in frequency.items():

        if count == 1:
            print(word)
            found = True

    if not found:
        print("No such words found.")

    # --------------------------------------------------
    # Words appearing more than 5 times
    # --------------------------------------------------
    print("\nWORDS APPEARING MORE THAN 5 TIMES")
    print("=" * 60)

    found = False

    for word, count in frequency.items():

        if count > 5:
            print(word, ":", count)
            found = True

    if not found:
        print("No words found.")

    # --------------------------------------------------
    # Count words starting with each alphabet
    # --------------------------------------------------
    alphabet_count = count_starting_alphabets(words)

    print("\nWORDS STARTING WITH EACH ALPHABET")
    print("=" * 60)

    for alphabet, count in sorted(alphabet_count.items()):
        print(alphabet, ":", count)

    # --------------------------------------------------
    # Unique Words
    # --------------------------------------------------
    print("\nUNIQUE WORDS")
    print("=" * 60)

    unique_words = sorted(set(words))

    for word in unique_words:
        print(word)

    # --------------------------------------------------
    # Challenge Report
    # --------------------------------------------------
    total_word_length = 0

    for word in words:
        total_word_length += len(word)

    average_word_length = (
        total_word_length / total_words
    )

    vocabulary_size = len(set(words))

    print("\nTEXT SUMMARY")
    print("=" * 60)

    print("Total Words         :", total_words)
    print("Total Sentences     :", total_sentences)
    print(
        "Average Word Length :",
        round(average_word_length, 2)
    )
    print(
        "Most Frequent Word  :",
        most_frequent_word
    )
    print(
        "Vocabulary Size     :",
        vocabulary_size
    )


# ==========================================================
# MAIN PROGRAM
# ==========================================================
analyze_article(article)