#Program to take the score of 11 players and printing the score and the highest score
#taking the score of 11 players
player_scores = [] #list to store the scores of the players
for i in range(11):
    score = int(input(f"Enter the score of player {i+1}: ")) #taking the score of each player and appending it to the list
    player_scores.append(score)

# printing the scores and the highest score
print("Scores of all players:")
for i in range(len(player_scores)):
    print(f"Player {i+1}: {player_scores[i]}")

highest_score = max(player_scores)
print(f"The highest score is: {highest_score}")