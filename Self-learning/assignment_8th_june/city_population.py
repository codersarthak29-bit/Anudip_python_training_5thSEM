'''The government wants to analyze city data. 
Store details of at least 30 cities. 
Example Structure 
cities = { 
    "Delhi": { 
        "population": 32000000, 
        "area": 1484, 
        "literacy": 89 
    } 
} 
Requirements 
1. Display all city details.  
2. Find the most populated city.  
3. Find the least populated city.  
4. Calculate average population.  
5. Display cities with literacy rate above 90%.  
6. Display cities with literacy below average.  
7. Calculate population density.  
8. Find city with highest density.  
9. Categorize cities:  
o Small  
o Medium  
o Large  
10. Create a development-priority list.  
11. Generate separate dictionaries for:  
o High Literacy Cities  
o Low Literacy Cities  
12. Generate a national summary report.  
Challenge 
Rank all cities based on population density.'''
# ==========================================
# CITY ANALYSIS SYSTEM
# ==========================================

# Dictionary To Store City Records
cities = {}

# ------------------------------------------
# INPUT DETAILS OF 30 CITIES
# ------------------------------------------

for i in range(30):

    print("\nEnter Details Of City", i + 1)

    # ------------------------------------------
    # City Name Validation
    # ------------------------------------------

    while True:

        city = " ".join(
            input("Enter City Name : ").split()
        ).title()

        if not city.replace(" ", "").isalpha():

            print("City Name Should Contain Alphabets Only")

        elif city in cities:

            print("City Already Exists")

        else:

            break

    # ------------------------------------------
    # Population Validation
    # ------------------------------------------

    while True:

        population = input(
            "Enter Population : "
        ).strip()

        if not population.isdigit():

            print("Population Must Contain Digits Only")
            continue

        population = int(population)

        if population > 0:
            break

        print("Population Must Be Greater Than Zero")

    # ------------------------------------------
    # Area Validation
    # ------------------------------------------

    while True:

        area = input(
            "Enter Area (sq km) : "
        ).strip()

        if not area.isdigit():

            print("Area Must Contain Digits Only")
            continue

        area = int(area)

        if area > 0:
            break

        print("Area Must Be Greater Than Zero")

    # ------------------------------------------
    # Literacy Validation
    # ------------------------------------------

    while True:

        literacy = input(
            "Enter Literacy Rate (0-100) : "
        ).strip()

        if not literacy.isdigit():

            print("Literacy Must Contain Digits Only")
            continue

        literacy = int(literacy)

        if 0 <= literacy <= 100:
            break

        print("Literacy Must Be Between 0 And 100")

    # ------------------------------------------
    # Store Record In Dictionary
    # ------------------------------------------

    cities[city] = {
        "population": population,
        "area": area,
        "literacy": literacy
    }

# ==========================================
# MENU DRIVEN PROGRAM
# ==========================================

while True:

    print("\n")
    print("===================================")
    print("      CITY ANALYSIS SYSTEM")
    print("===================================")
    print("1. Display All City Details")
    print("2. Most Populated City")
    print("3. Least Populated City")
    print("4. Average Population")
    print("5. Cities With Literacy Above 90%")
    print("6. Cities With Literacy Below Average")
    print("7. Calculate Population Density")
    print("8. City With Highest Density")
    print("9. Categorize Cities")
    print("10. Development Priority List")
    print("11. Literacy Dictionaries")
    print("12. National Summary Report")
    print("13. Rank Cities By Density")
    print("14. Exit")

    choice = input(
        "\nEnter Your Choice : "
    ).strip()

    # ------------------------------------------
    # 1. Display All City Details
    # ------------------------------------------

    if choice == "1":

        print("\n========== CITY DETAILS ==========")

        for city, data in cities.items():

            print(
                f'{city} -> '
                f'population="{data["population"]}", '
                f'area="{data["area"]}", '
                f'literacy="{data["literacy"]}"'
            )

    # ------------------------------------------
    # 2. Most Populated City
    # ------------------------------------------

    elif choice == "2":

        for city in cities:

            most_populated = city
            break

        for city in cities:

            if (
                cities[city]["population"]
                >
                cities[most_populated]["population"]
            ):

                most_populated = city

        print(
            "\nMost Populated City :",
            most_populated
        )

        print(cities[most_populated])

    # ------------------------------------------
    # 3. Least Populated City
    # ------------------------------------------

    elif choice == "3":

        for city in cities:

            least_populated = city
            break

        for city in cities:

            if (
                cities[city]["population"]
                <
                cities[least_populated]["population"]
            ):

                least_populated = city

        print(
            "\nLeast Populated City :",
            least_populated
        )

        print(cities[least_populated])

    # ------------------------------------------
    # 4. Average Population
    # ------------------------------------------

    elif choice == "4":

        total_population = 0

        for city in cities:

            total_population += (
                cities[city]["population"]
            )

        average_population = (
            total_population / len(cities)
        )

        print(
            "\nAverage Population =",
            round(average_population, 2)
        )

    # ------------------------------------------
    # 5. Literacy Above 90%
    # ------------------------------------------

    elif choice == "5":

        print(
            "\nCities With Literacy Above 90%"
        )

        found = False

        for city, data in cities.items():

            if data["literacy"] > 90:

                print(city, "->", data)

                found = True

        if not found:

            print("No City Found")

    # ------------------------------------------
    # 6. Literacy Below Average
    # ------------------------------------------

    elif choice == "6":

        total_literacy = 0

        for city in cities:

            total_literacy += (
                cities[city]["literacy"]
            )

        average_literacy = (
            total_literacy / len(cities)
        )

        print(
            "\nCities Below Average Literacy"
        )

        for city, data in cities.items():

            if data["literacy"] < average_literacy:

                print(city, "->", data)
        # ------------------------------------------
    # 7. Calculate Population Density
    # Density = Population / Area
    # ------------------------------------------

    elif choice == "7":

        print("\n========== POPULATION DENSITY ==========")

        for city, data in cities.items():

            density = (
                data["population"] /
                data["area"]
            )

            print(
                city,
                "-> Density =",
                round(density, 2)
            )

    # ------------------------------------------
    # 8. City With Highest Density
    # ------------------------------------------

    elif choice == "8":

        for city in cities:

            highest_density_city = city
            break

        highest_density = (
            cities[highest_density_city]["population"]
            /
            cities[highest_density_city]["area"]
        )

        for city in cities:

            current_density = (
                cities[city]["population"]
                /
                cities[city]["area"]
            )

            if current_density > highest_density:

                highest_density = current_density
                highest_density_city = city

        print(
            "\nCity With Highest Density :",
            highest_density_city
        )

        print(
            "Density =",
            round(highest_density, 2)
        )

    # ------------------------------------------
    # 9. Categorize Cities
    # ------------------------------------------

    elif choice == "9":

        print("\n========== CITY CATEGORIES ==========")

        for city, data in cities.items():

            population = data["population"]

            if population >= 10000000:

                category = "Large"

            elif population >= 1000000:

                category = "Medium"

            else:

                category = "Small"

            print(city, "->", category)

    # ------------------------------------------
    # 10. Development Priority List
    # Literacy < 75
    # ------------------------------------------

    elif choice == "10":

        print(
            "\n========== DEVELOPMENT PRIORITY LIST =========="
        )

        found = False

        for city, data in cities.items():

            if data["literacy"] < 75:

                print(city, "->", data)

                found = True

        if not found:

            print(
                "No City Requires Development Priority"
            )

    # ------------------------------------------
    # 11. High Literacy And Low Literacy Dictionaries
    # ------------------------------------------

    elif choice == "11":

        high_literacy = {}
        low_literacy = {}

        for city, data in cities.items():

            if data["literacy"] >= 90:

                high_literacy[city] = data

            elif data["literacy"] < 75:

                low_literacy[city] = data

        print(
            "\n========== HIGH LITERACY CITIES =========="
        )

        for city, data in high_literacy.items():

            print(city, "->", data)

        print(
            "\n========== LOW LITERACY CITIES =========="
        )

        for city, data in low_literacy.items():

            print(city, "->", data)

    # ------------------------------------------
    # 12. National Summary Report
    # ------------------------------------------

    elif choice == "12":

        total_population = 0
        total_area = 0
        total_literacy = 0

        for city in cities:

            total_population += (
                cities[city]["population"]
            )

            total_area += (
                cities[city]["area"]
            )

            total_literacy += (
                cities[city]["literacy"]
            )

        average_population = (
            total_population / len(cities)
        )

        average_literacy = (
            total_literacy / len(cities)
        )

        print("\n")
        print("====================================")
        print("      NATIONAL SUMMARY REPORT")
        print("====================================")

        print(
            "Total Cities :",
            len(cities)
        )

        print(
            "Total Population :",
            total_population
        )

        print(
            "Total Area :",
            total_area
        )

        print(
            "Average Population :",
            round(average_population, 2)
        )

        print(
            "Average Literacy :",
            round(average_literacy, 2)
        )

        print("====================================")
        print("       REPORT COMPLETED")
        print("====================================")

    # ------------------------------------------
    # 13. Rank Cities By Population Density
    # Challenge Question
    # ------------------------------------------

    elif choice == "13":

        city_list = []

        for city, data in cities.items():

            density = (
                data["population"]
                /
                data["area"]
            )

            city_list.append(
                [city, density]
            )

        # Manual Sorting
        # Highest Density First

        for i in range(len(city_list) - 1):

            for j in range(i + 1, len(city_list)):

                if (
                    city_list[i][1]
                    <
                    city_list[j][1]
                ):

                    city_list[i], city_list[j] = (
                        city_list[j],
                        city_list[i]
                    )

        print(
            "\n========== CITY DENSITY RANKING =========="
        )

        rank = 1

        for city in city_list:

            print(
                rank,
                ".",
                city[0],
                "-> Density =",
                round(city[1], 2)
            )

            rank += 1

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

        print(
            "Invalid Choice! Please Try Again."
        )