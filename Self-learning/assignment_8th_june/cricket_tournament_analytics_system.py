
'''Store statistics of at least 30 cricket players. 
Example Structure 
players = { 
    "Virat": { 
        "runs": 645, 
        "matches": 12, 
        "wickets": 0 
    } 
} 
Requirements 
1. Display all player statistics.  
2. Find highest run scorer.  
3. Find lowest run scorer.  
4. Calculate average runs.  
5. Find player with maximum wickets.  
6. Find all-rounders (runs > 300 and wickets > 5).  
7. Display players scoring above average.  
8. Create categories:  
o Star Performer  
o Good Performer  
o Average Performer  
o Poor Performer  
9. Generate team statistics.  
10. Display top 5 batsmen.  
11. Display top 5 bowlers.  
12. Create a separate dictionary for award winners.  
Challenge 
Generate a tournament report.'''
# ==========================================
# CRICKET TOURNAMENT MANAGEMENT SYSTEM
# ==========================================

# Dictionary To Store Player Records
players = {}

# ------------------------------------------
# INPUT DETAILS OF 30 PLAYERS
# ------------------------------------------

for i in range(30):

    print("\nEnter Details Of Player", i + 1)

    # ------------------------------------------
    # Player Name Validation
    # ------------------------------------------

    while True:

        name = " ".join(
            input("Enter Player Name : ").split()
        ).title()

        if not name.replace(" ", "").isalpha():

            print("Name Should Contain Alphabets Only")

        elif name in players:

            print("Player Already Exists")

        else:

            break

    # ------------------------------------------
    # Runs Validation
    # ------------------------------------------

    while True:

        runs = input("Enter Runs : ").strip()

        if not runs.isdigit():

            print("Runs Must Contain Digits Only")
            continue

        runs = int(runs)

        if runs >= 0:
            break

    # ------------------------------------------
    # Matches Validation
    # ------------------------------------------

    while True:

        matches = input("Enter Matches : ").strip()

        if not matches.isdigit():

            print("Matches Must Contain Digits Only")
            continue

        matches = int(matches)

        if matches > 0:
            break

        print("Matches Must Be Greater Than Zero")

    # ------------------------------------------
    # Wickets Validation
    # ------------------------------------------

    while True:

        wickets = input("Enter Wickets : ").strip()

        if not wickets.isdigit():

            print("Wickets Must Contain Digits Only")
            continue

        wickets = int(wickets)

        if wickets >= 0:
            break

    # ------------------------------------------
    # Store Record In Dictionary
    # ------------------------------------------

    players[name] = {
        "runs": runs,
        "matches": matches,
        "wickets": wickets
    }

# ==========================================
# MENU DRIVEN PROGRAM
# ==========================================

while True:

    print("\n")
    print("======================================")
    print(" CRICKET TOURNAMENT MANAGEMENT SYSTEM ")
    print("======================================")
    print("1. Display All Player Statistics")
    print("2. Highest Run Scorer")
    print("3. Lowest Run Scorer")
    print("4. Calculate Average Runs")
    print("5. Player With Maximum Wickets")
    print("6. Find All-Rounders")
    print("7. Players Above Average Runs")
    print("8. Performance Categories")
    print("9. Team Statistics")
    print("10. Top 5 Batsmen")
    print("11. Top 5 Bowlers")
    print("12. Award Winners")
    print("13. Tournament Report")
    print("14. Exit")

    choice = input("\nEnter Your Choice : ").strip()

    # ------------------------------------------
    # 1. Display All Player Statistics
    # ------------------------------------------

    if choice == "1":

        print("\n========== PLAYER RECORDS ==========")

        for player, data in players.items():

            print(
                f'{player} -> '
                f'runs="{data["runs"]}", '
                f'matches="{data["matches"]}", '
                f'wickets="{data["wickets"]}"'
            )

    # ------------------------------------------
    # 2. Highest Run Scorer
    # ------------------------------------------

    elif choice == "2":

        for player in players:

            highest = player
            break

        for player in players:

            if (
                players[player]["runs"]
                >
                players[highest]["runs"]
            ):

                highest = player

        print("\nHighest Run Scorer")

        print(
            highest,
            "->",
            players[highest]
        )

    # ------------------------------------------
    # 3. Lowest Run Scorer
    # ------------------------------------------

    elif choice == "3":

        for player in players:

            lowest = player
            break

        for player in players:

            if (
                players[player]["runs"]
                <
                players[lowest]["runs"]
            ):

                lowest = player

        print("\nLowest Run Scorer")

        print(
            lowest,
            "->",
            players[lowest]
        )

    # ------------------------------------------
    # 4. Calculate Average Runs
    # ------------------------------------------

    elif choice == "4":

        total_runs = 0

        for player in players:

            total_runs += players[player]["runs"]

        average_runs = (
            total_runs / len(players)
        )

        print(
            "\nAverage Runs =",
            round(average_runs, 2)
        )

    # ------------------------------------------
    # 5. Player With Maximum Wickets
    # ------------------------------------------

    elif choice == "5":

        for player in players:

            best_bowler = player
            break

        for player in players:

            if (
                players[player]["wickets"]
                >
                players[best_bowler]["wickets"]
            ):

                best_bowler = player

        print("\nBest Bowler")

        print(
            best_bowler,
            "->",
            players[best_bowler]
        )

    # ------------------------------------------
    # 6. Find All-Rounders
    # ------------------------------------------

    elif choice == "6":

        print("\n========== ALL ROUNDERS ==========")

        found = False

        for player, data in players.items():

            if (
                data["runs"] > 300
                and
                data["wickets"] > 5
            ):

                print(player, "->", data)

                found = True

        if not found:

            print("No All-Rounders Found")
    # ------------------------------------------
    # 7. Players Scoring Above Average Runs
    # ------------------------------------------

    elif choice == "7":

        total_runs = 0

        for player in players:

            total_runs += players[player]["runs"]

        average_runs = total_runs / len(players)

        print("\nPlayers Above Average Runs")

        found = False

        for player, data in players.items():

            if data["runs"] > average_runs:

                print(player, "->", data)

                found = True

        if not found:

            print("No Player Found")

    # ------------------------------------------
    # 8. Performance Categories
    # ------------------------------------------

    elif choice == "8":

        print("\n========== PERFORMANCE CATEGORY ==========")

        for player, data in players.items():

            runs = data["runs"]

            if runs >= 600:

                category = "Star Performer"

            elif runs >= 400:

                category = "Good Performer"

            elif runs >= 200:

                category = "Average Performer"

            else:

                category = "Poor Performer"

            print(player, "->", category)

    # ------------------------------------------
    # 9. Team Statistics
    # ------------------------------------------

    elif choice == "9":

        total_runs = 0
        total_wickets = 0
        total_matches = 0

        for player in players:

            total_runs += players[player]["runs"]
            total_wickets += players[player]["wickets"]
            total_matches += players[player]["matches"]

        print("\n========== TEAM STATISTICS ==========")

        print("Total Players :", len(players))
        print("Total Runs :", total_runs)
        print("Total Wickets :", total_wickets)
        print("Total Matches :", total_matches)

    # ------------------------------------------
    # 10. Top 5 Batsmen
    # ------------------------------------------

    elif choice == "10":

        player_list = list(players.items())

        for i in range(len(player_list) - 1):

            for j in range(i + 1, len(player_list)):

                if (
                    player_list[i][1]["runs"]
                    <
                    player_list[j][1]["runs"]
                ):

                    player_list[i], player_list[j] = (
                        player_list[j],
                        player_list[i]
                    )

        print("\n========== TOP 5 BATSMEN ==========")

        for i in range(5):

            print(
                player_list[i][0],
                "->",
                player_list[i][1]
            )

    # ------------------------------------------
    # 11. Top 5 Bowlers
    # ------------------------------------------

    elif choice == "11":

        player_list = list(players.items())

        for i in range(len(player_list) - 1):

            for j in range(i + 1, len(player_list)):

                if (
                    player_list[i][1]["wickets"]
                    <
                    player_list[j][1]["wickets"]
                ):

                    player_list[i], player_list[j] = (
                        player_list[j],
                        player_list[i]
                    )

        print("\n========== TOP 5 BOWLERS ==========")

        for i in range(5):

            print(
                player_list[i][0],
                "->",
                player_list[i][1]
            )

    # ------------------------------------------
    # 12. Award Winners Dictionary
    # ------------------------------------------

    elif choice == "12":

        award_winners = {}

        for player, data in players.items():

            if (
                data["runs"] >= 500
                or
                data["wickets"] >= 15
            ):

                award_winners[player] = data

        print("\n========== AWARD WINNERS ==========")

        if len(award_winners) == 0:

            print("No Award Winners Found")

        else:

            for player, data in award_winners.items():

                print(player, "->", data)

    # ------------------------------------------
    # 13. Tournament Report
    # ------------------------------------------

    elif choice == "13":

        # Find Highest Run Scorer

        for player in players:

            highest = player
            break

        for player in players:

            if (
                players[player]["runs"]
                >
                players[highest]["runs"]
            ):

                highest = player

        # Find Best Bowler

        for player in players:

            best_bowler = player
            break

        for player in players:

            if (
                players[player]["wickets"]
                >
                players[best_bowler]["wickets"]
            ):

                best_bowler = player

        # Calculate Team Runs

        total_runs = 0
        total_wickets = 0

        for player in players:

            total_runs += players[player]["runs"]
            total_wickets += players[player]["wickets"]

        print("\n")
        print("====================================")
        print("      TOURNAMENT REPORT")
        print("====================================")

        print("Total Players :", len(players))
        print("Total Runs :", total_runs)
        print("Total Wickets :", total_wickets)

        print(
            "Highest Run Scorer :",
            highest
        )

        print(
            "Runs Scored :",
            players[highest]["runs"]
        )

        print(
            "Best Bowler :",
            best_bowler
        )

        print(
            "Wickets Taken :",
            players[best_bowler]["wickets"]
        )

        print("====================================")
        print("      REPORT COMPLETED")
        print("====================================")

    # ------------------------------------------
    # 14. Exit Program
    # ------------------------------------------

    elif choice == "14":

        print("\nExiting Program...")
        break

    # ------------------------------------------
    # Invalid Choice
    # ------------------------------------------

    else:

        print("Invalid Choice! Please Try Again.")