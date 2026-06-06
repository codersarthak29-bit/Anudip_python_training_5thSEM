'''Correct answers: 
correct = ['A', 'C', 'B', 'D', 'A'] 
Student answers: 
student = ['A', 'B', 'B', 'D', 'C'] 
Write a program to: 
• Calculate score.  
• Display incorrectly answered question numbers.  
• Count correct and wrong answers.  
• Determine pass/fail (minimum 60%).  '''
# Correct answers and student answers
correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

# Variables
score = 0
wrong_questions = []

# Compare answers
for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1
    else:
        wrong_questions.append(i + 1)  # Question number

# Count correct and wrong answers
correct_count = score
wrong_count = len(correct) - score

# Calculate percentage
percentage = (score / len(correct)) * 100

# Determine pass/fail
if percentage >= 60:
    result = "Pass"
else:
    result = "Fail"

# Display results
print("Score:", score, "/", len(correct))
print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)
print("Incorrectly Answered Question Numbers:", wrong_questions)
print("Percentage:", percentage, "%")
print("Result:", result)