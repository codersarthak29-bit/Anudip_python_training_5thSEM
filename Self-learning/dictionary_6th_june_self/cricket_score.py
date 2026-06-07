'''scores = { 
    "Virat": 78, 
    "Rohit": 112, 
    "Gill": 45, 
    "Rahul": 89, 
    "Hardik": 32, 
    "Jadeja": 61, 
    "Surya": 105, 
    "Pant": 95, 
    "Bumrah": 18, 
    "Shami": 25 
} 
Tasks 
• Display players who scored 50 or more runs.  
• Count the number of centuries.  
• Find the player with the highest score.  
• Create a list of players scoring below 30 runs.  
• Determine how many players scored between 50 and 99. '''
# Program to perform various operations on cricket players' scores

# Dictionary containing player names as keys and scores as values
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# --------------------------------------------------
# Task 1: Display players who scored 50 or more runs
# --------------------------------------------------
print("Players who scored 50 or more runs:")

# Traversing the dictionary
for player, runs in scores.items():

    # Checking if runs are 50 or more
    if runs >= 50:
        print(player, "-", runs)

# --------------------------------------------------
# Task 2: Count the number of centuries
# (Score 100 or more)
# --------------------------------------------------
century_count = 0

# Checking score of each player
for runs in scores.values():

    # Incrementing count if score is 100 or more
    if runs >= 100:
        century_count += 1

print("\nNumber of Centuries:", century_count)

# --------------------------------------------------
# Task 3: Find the player with the highest score
# --------------------------------------------------

# Assuming the first score as the highest score
highest_player = ""
highest_score = 0

# Traversing the dictionary
for player, runs in scores.items():

    # Updating highest score and player name
    if runs > highest_score:
        highest_score = runs
        highest_player = player

print("\nPlayer with Highest Score:")
print(highest_player, "-", highest_score)

# --------------------------------------------------
# Task 4: Create a list of players scoring
# below 30 runs
# --------------------------------------------------
low_scorers = []

# Adding players with score below 30 to the list
for player, runs in scores.items():

    # Checking if score is below 30
    if runs < 30:
        low_scorers.append(player)

print("\nPlayers Scoring Below 30 Runs:")
print(low_scorers)

# --------------------------------------------------
# Task 5: Determine how many players scored
# between 50 and 99 runs
# --------------------------------------------------
count_50_99 = 0

# Checking score of each player
for runs in scores.values():

    # Incrementing count if score lies between 50 and 99
    if 50 <= runs <= 99:
        count_50_99 += 1

print("\nNumber of Players Scoring Between 50 and 99 Runs:", count_50_99)