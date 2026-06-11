'''Problem Statement
A messaging application wants to analyze chat messages.
Store at least 20 chat messages in a list.
Requirements
For each message:
    1.Count total words.
    2.Count total characters.
    3.Count vowels and consonants.
    4.Find longest word.
    5.Find shortest word.
    6.Count occurrence of each word.
    7.Display repeated words.
    8.Display words starting with vowels.
    9.Display words longer than 5 characters.
    10.Create a dictionary containing word frequencies.
Challenge
Generate a report showing:
Most Frequently Used Word Longest Message Shortest Message Average Words Per Message'''

# Chat Message Analytics Dashboard

# List containing chat messages
messages = [
    "Hello how are you",
    "I am doing great today",
    "Python programming is fun",
    "Data science is amazing",
    "Machine learning is powerful",
    "Hello everyone welcome",
    "Today is a beautiful day",
    "Keep learning new things",
    "Practice makes a person perfect",
    "Programming improves problem solving",
    "Cloud computing is the future",
    "Cyber security is important",
    "Networking connects computers",
    "Database management is useful",
    "Artificial intelligence is growing",
    "Python is easy to learn",
    "Learning Python improves skills",
    "Welcome to the Python class",
    "Data analysis helps businesses",
    "Have a great learning experience"
]

# Validation: Check whether the list contains messages
if len(messages) == 0:
    print("No messages available for analysis.")
else:

    # Dictionary to store frequency of all words
    word_frequency = {}

    # Variables required for final report
    longest_message = messages[0]
    shortest_message = messages[0]
    total_words_all_messages = 0

    print("CHAT MESSAGE ANALYTICS")
    print("=" * 50)

    # Process each message one by one
    for message_no, message in enumerate(messages, start=1):

        print(f"\nMessage {message_no}: {message}")

        # Remove extra spaces from beginning and end
        message = message.strip()

        # Validation: Skip empty messages
        if message == "":
            print("Empty message found. Skipping analysis.")
            continue

        # Split message into words
        words = message.split()

        # Validation: Ensure message contains words
        if len(words) == 0:
            print("No valid words found.")
            continue

        # --------------------------------------------------
        # 1. Count Total Words
        # --------------------------------------------------
        total_words = len(words)
        print("Total Words:", total_words)

        # --------------------------------------------------
        # 2. Count Total Characters (excluding spaces)
        # --------------------------------------------------
        total_characters = len(message.replace(" ", ""))
        print("Total Characters:", total_characters)

        # --------------------------------------------------
        # 3. Count Vowels and Consonants
        # --------------------------------------------------
        vowels = 0
        consonants = 0

        for char in message.lower():

            # Consider only alphabetic characters
            if char.isalpha():

                if char in "aeiou":
                    vowels += 1
                else:
                    consonants += 1

        print("Vowels:", vowels)
        print("Consonants:", consonants)

        # --------------------------------------------------
        # 4. Find Longest Word
        # --------------------------------------------------
        longest_word = max(words, key=len)
        print("Longest Word:", longest_word)

        # --------------------------------------------------
        # 5. Find Shortest Word
        # --------------------------------------------------
        shortest_word = min(words, key=len)
        print("Shortest Word:", shortest_word)

        # --------------------------------------------------
        # 6. Count Occurrence of Each Word
        # --------------------------------------------------
        for word in words:

            # Convert to lowercase so that
            # Python and python are treated as same
            word = word.lower()

            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        # --------------------------------------------------
        # Update longest message
        # --------------------------------------------------
        if len(message) > len(longest_message):
            longest_message = message

        # --------------------------------------------------
        # Update shortest message
        # --------------------------------------------------
        if len(message) < len(shortest_message):
            shortest_message = message

        # Add current message word count
        # for average calculation later
        total_words_all_messages += total_words

    # ==================================================
    # 6. Display Word Frequencies
    # ==================================================
    print("\n\nWORD FREQUENCIES")
    print("=" * 50)

    if len(word_frequency) > 0:

        for word, count in word_frequency.items():
            print(word, ":", count)

    else:
        print("No words found.")

    # ==================================================
    # 7. Display Repeated Words
    # ==================================================
    print("\nREPEATED WORDS")
    print("=" * 50)

    repeated_found = False

    for word, count in word_frequency.items():

        if count > 1:
            print(word, ":", count)
            repeated_found = True

    if not repeated_found:
        print("No repeated words found.")

    # ==================================================
    # 8. Display Words Starting with Vowels
    # ==================================================
    print("\nWORDS STARTING WITH VOWELS")
    print("=" * 50)

    vowel_word_found = False

    for word in word_frequency:

        if word[0].lower() in "aeiou":
            print(word)
            vowel_word_found = True

    if not vowel_word_found:
        print("No words start with vowels.")

    # ==================================================
    # 9. Display Words Longer Than 5 Characters
    # ==================================================
    print("\nWORDS LONGER THAN 5 CHARACTERS")
    print("=" * 50)

    long_word_found = False

    for word in word_frequency:

        if len(word) > 5:
            print(word)
            long_word_found = True

    if not long_word_found:
        print("No words longer than 5 characters found.")

    # ==================================================
    # 10. Display Word Frequency Dictionary
    # ==================================================
    print("\nWORD FREQUENCY DICTIONARY")
    print("=" * 50)
    print(word_frequency)

    # ==================================================
    # CHALLENGE REPORT
    # ==================================================
    print("\nCHAT ANALYTICS REPORT")
    print("=" * 50)

    # Validation before using max()
    if len(word_frequency) > 0:

        # Find word having highest frequency
        most_used_word = max(word_frequency,
                             key=word_frequency.get)

        print("Most Frequently Used Word:",
              most_used_word)

        print("Frequency:",
              word_frequency[most_used_word])

    else:
        print("No words available for frequency analysis.")

    print("\nLongest Message:")
    print(longest_message)

    print("\nShortest Message:")
    print(shortest_message)

    # Validation before division
    if len(messages) > 0:

        average_words = (
            total_words_all_messages / len(messages)
        )

        print("\nAverage Words Per Message:",
              round(average_words, 2))

    else:
        print("\nAverage Words Per Message: 0")