'''Problem Statement 
Runs scored by players in a tournament are given below. 
Sample Data 
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
1. Find the Orange Cap winner.  
2. Find the lowest scorer.  
3. Calculate total runs scored.  
4. Display players scoring more than 500 runs.  
5. Create a list of players scoring below 400.  '''
#program to make Cricket Tournament Statistics 

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
#task1:Find the Orange Cap winner.  
top_scorer=max(runs, key=runs.get)
print(f"The Orange Cap winner is: {top_scorer} with {runs[top_scorer]} runs.")
#task2:Find the lowest scorer.
lowest_scorer=min(runs, key=runs.get)
print(f"The lowest scorer is: {lowest_scorer} with {runs[lowest_scorer]} runs.")
#task3:Calculate total runs scored.
total_runs=sum(runs.values())
print(f"Total runs scored by all players: {total_runs} runs.")
#task4:Display players scoring more than 500 runs. 
for player,score in runs.items():
    if score>500:
        print(f"{player}: {score} runs")
#task5:Create a list of players scoring below 400.
players_below_400 = []
for player, score in runs.items():
    if score < 400:
        players_below_400.append(player)
print(f"Players scoring below 400 runs: {players_below_400}")
