# ==========================================================
# RESUME ANALYZER SYSTEM
# ==========================================================
# This program analyzes a resume and:
# 1. Counts total words
# 2. Counts total characters
# 3. Extracts email IDs
# 4. Extracts phone numbers
# 5. Counts skills mentioned
# 6. Finds repeated keywords
# 7. Finds most frequent word
# 8. Generates skill frequency report
# 9. Detects duplicate skills
# 10. Creates a summary dashboard
# ==========================================================


# Sample Resume Text
resume = """
Name: Rahul Sharma

Email: rahul.sharma@gmail.com
Phone: 9876543210

Education:
Bachelor of Technology in Computer Science

Skills:
Python Java SQL React Python Communication
Leadership SQL Python Java

Projects:
Developed a web application using Python and React.
Created a database management system using SQL.
Built automation scripts using Python.

Achievements:
Won coding competitions.
Received best project award.
Strong communication and leadership skills.
"""


# ==========================================================
# Function to validate resume text
# ==========================================================
def validate_resume(text):

    # Check if resume is empty
    if text.strip() == "":
        return False

    return True


# ==========================================================
# Function to clean and extract words
# ==========================================================
def get_words(text):

    words = []

    for word in text.split():

        # Remove punctuation and convert to lowercase
        cleaned_word = word.strip(
            ".,!?;:()[]{}\"'"
        ).lower()

        # Ignore empty strings
        if cleaned_word != "":
            words.append(cleaned_word)

    return words


# ==========================================================
# Function to count total words
# ==========================================================
def count_words(words):

    return len(words)


# ==========================================================
# Function to count total characters
# ==========================================================
def count_characters(text):

    return len(text)


# ==========================================================
# Function to extract email IDs
# Validation:
# Must contain @ and .
# ==========================================================
def extract_emails(text):

    emails = []

    for word in text.split():

        word = word.strip(
            ".,!?;:()[]{}\"'"
        )

        if (
            "@" in word
            and "." in word
            and word.index("@") > 0
            and word.index(".") > word.index("@")
        ):

            # Avoid duplicate emails
            if word not in emails:
                emails.append(word)

    return emails


# ==========================================================
# Function to extract phone numbers
# Validation:
# Only digits
# Length must be 10
# ==========================================================
def extract_phone_numbers(text):

    phones = []

    for word in text.split():

        if word.isdigit():

            if len(word) == 10:

                if word not in phones:
                    phones.append(word)

    return phones


# ==========================================================
# Function to create word frequency dictionary
# ==========================================================
def create_frequency_dictionary(words):

    frequency = {}

    for word in words:

        frequency[word] = (
            frequency.get(word, 0) + 1
        )

    return frequency


# ==========================================================
# Function to analyze skills
# ==========================================================
def analyze_skills(words):

    # Predefined skills list
    skill_list = [
        "python",
        "java",
        "sql",
        "react",
        "communication",
        "leadership",
        "html",
        "css",
        "javascript"
    ]

    skill_frequency = {}

    for word in words:

        if word in skill_list:

            skill_frequency[word] = (
                skill_frequency.get(word, 0) + 1
            )

    return skill_frequency


# ==========================================================
# Function to display repeated keywords
# ==========================================================
def display_repeated_keywords(frequency):

    print("\nRepeated Keywords")
    print("-" * 40)

    found = False

    for word, count in frequency.items():

        if count > 1:
            print(word, ":", count)
            found = True

    if not found:
        print("No repeated keywords found.")


# ==========================================================
# Function to display skill frequency report
# ==========================================================
def display_skill_report(skill_frequency):

    print("\nSkill Frequency Report")
    print("-" * 40)

    if len(skill_frequency) == 0:
        print("No skills found.")
        return

    for skill, count in skill_frequency.items():
        print(skill, ":", count)


# ==========================================================
# Function to detect duplicate skills
# ==========================================================
def display_duplicate_skills(skill_frequency):

    print("\nDuplicate Skills")
    print("-" * 40)

    found = False

    for skill, count in skill_frequency.items():

        if count > 1:
            print(skill, ":", count)
            found = True

    if not found:
        print("No duplicate skills found.")


# ==========================================================
# Function to display top 5 keywords
# ==========================================================
def display_top_keywords(frequency):

    print("\nTop 5 Keywords")
    print("-" * 40)

    if len(frequency) == 0:
        print("No keywords available.")
        return

    sorted_words = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for word, count in sorted_words[:5]:
        print(word, ":", count)


# ==========================================================
# Function to generate dashboard
# ==========================================================
def generate_dashboard(text):

    # Validation 1
    if not validate_resume(text):
        print("Resume is empty.")
        return

    words = get_words(text)

    # Validation 2
    if len(words) == 0:
        print("No valid words found.")
        return

    # Create frequency dictionary
    frequency = create_frequency_dictionary(words)

    # Extract emails and phones
    emails = extract_emails(text)
    phones = extract_phone_numbers(text)

    # Analyze skills
    skill_frequency = analyze_skills(words)

    # Find most frequent word
    if len(frequency) > 0:

        most_frequent_word = max(
            frequency,
            key=frequency.get
        )

    else:
        most_frequent_word = "None"

    # Find most frequent skill
    if len(skill_frequency) > 0:

        most_frequent_skill = max(
            skill_frequency,
            key=skill_frequency.get
        )

    else:
        most_frequent_skill = "None"

    # ==================================================
    # DASHBOARD
    # ==================================================
    print("\n")
    print("=" * 50)
    print("RESUME ANALYSIS REPORT")
    print("=" * 50)

    print("Total Words:",
          count_words(words))

    print("Total Characters:",
          count_characters(text))

    print("Email IDs Found:",
          len(emails))

    print("Phone Numbers Found:",
          len(phones))

    print("Most Frequent Word:",
          most_frequent_word)

    print("Most Frequent Skill:",
          most_frequent_skill)

    print("Total Skills Mentioned:",
          sum(skill_frequency.values()))

    # Display Emails
    print("\nEmails Found")
    print("-" * 40)

    if len(emails) == 0:
        print("No emails found.")
    else:
        for email in emails:
            print(email)

    # Display Phones
    print("\nPhone Numbers Found")
    print("-" * 40)

    if len(phones) == 0:
        print("No phone numbers found.")
    else:
        for phone in phones:
            print(phone)

    # Display Top Keywords
    display_top_keywords(frequency)

    # Display Repeated Keywords
    display_repeated_keywords(frequency)

    # Display Skill Report
    display_skill_report(skill_frequency)

    # Display Duplicate Skills
    display_duplicate_skills(skill_frequency)


# ==========================================================
# MAIN PROGRAM
# ==========================================================

generate_dashboard(resume)