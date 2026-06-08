'''Runs scored by players in a tournament: 
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 
Tasks 
1. Display players scoring more than 500 runs.  
2. Find the Orange Cap winner.  
3. Find the lowest scorer.  
4. Calculate total runs scored.  
5. Create a list of players scoring below 400.  
6. Count players scoring between 400 and 600 runs.  
Sample Output 
Players Scoring More Than 500 Runs: 
Virat 
Rohit 
Gill 
Pant 
 
Orange Cap Winner: Gill (698) 
 
Lowest Scorer: Hardik (278) 
 
Total Tournament Runs: 4657 
 
Players Scoring Below 400: 
['Hardik', 'Surya', 'Jadeja'] 
 
Players Between 400 and 600 Runs: 5'''
# Program to perform various operations on tournament runs data

# Dictionary containing player names as keys and runs scored as values
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# --------------------------------------------------
# Task 1: Display players scoring more than 500 runs
# --------------------------------------------------
print("Players Scoring More Than 500 Runs:")

# Traversing the dictionary
for player, score in runs.items():

    # Checking if runs scored are greater than 500
    if score > 500:
        print(player)

# --------------------------------------------------
# Task 2: Find the Orange Cap winner
# --------------------------------------------------

# Assuming the first player's runs as the highest initially
orange_cap = list(runs.keys())[0]
highest_runs = list(runs.values())[0]

# Traversing the dictionary
for player, score in runs.items():

    # Updating highest runs and player name
    if score > highest_runs:
        highest_runs = score
        orange_cap = player

print("\nOrange Cap Winner:", orange_cap, "(", highest_runs, ")")

# --------------------------------------------------
# Task 3: Find the lowest scorer
# --------------------------------------------------

# Assuming the first player's runs as the lowest initially
lowest_player = list(runs.keys())[0]
lowest_runs = list(runs.values())[0]

# Traversing the dictionary
for player, score in runs.items():

    # Updating lowest runs and player name
    if score < lowest_runs:
        lowest_runs = score
        lowest_player = player

print("\nLowest Scorer:", lowest_player, "(", lowest_runs, ")")

# --------------------------------------------------
# Task 4: Calculate total runs scored
# --------------------------------------------------
total_runs = 0

# Calculating total tournament runs
for score in runs.values():
    total_runs += score

print("\nTotal Tournament Runs:", total_runs)

# --------------------------------------------------
# Task 5: Create a list of players scoring below 400
# --------------------------------------------------
below_400 = []

# Adding players with runs below 400 to the list
for player, score in runs.items():

    # Checking if runs are below 400
    if score < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400:")
print(below_400)

# --------------------------------------------------
# Task 6: Count players scoring between
# 400 and 600 runs
# --------------------------------------------------
count = 0

# Checking runs scored by each player
for score in runs.values():

    # Incrementing count if runs lie between 400 and 600
    if 400 <= score <= 600:
        count += 1

print("\nPlayers Between 400 and 600 Runs:", count)
'''
OUTPUT:
Players Scoring More Than 500 Runs: 
Virat 
Rohit 
Gill 
Pant 
 
Orange Cap Winner: Gill (698) 
 
Lowest Scorer: Hardik (278) 
 
Total Tournament Runs: 4657 
 
Players Scoring Below 400: 
['Hardik', 'Surya', 'Jadeja'] 
 
Players Between 400 and 600 Runs: 5 '''