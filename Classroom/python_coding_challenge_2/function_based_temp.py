'''Problem Statement 
Daily temperatures recorded in Celsius are given below. 
Sample Data 
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31] 
Tasks 
Create functions to: 
1. Convert Celsius to Fahrenheit.  
2. Display all temperatures in Fahrenheit.  
3. Find the highest Fahrenheit temperature.  
4. Find the lowest Fahrenheit temperature.  
5. Calculate the average Fahrenheit temperature.  
Sample Output 
Temperatures in Fahrenheit: 
77.0 
86.0 
95.0 
104.0 
82.4 
89.6 
100.4 
71.6 
80.6 
87.8 
Highest Temperature: 104.0°F 
Lowest Temperature: 71.6°F 
A company wants to maintain backups of important documents. Create a program to copy the contents of 
one file into another. 
Average Temperature: 87.14°F'''
# Sample Data
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31]

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to display all temperatures in Fahrenheit
def display_fahrenheit(temp_list):
    print("Temperatures in Fahrenheit:")
    fahrenheit_list = []

    for temp in temp_list:
        f = celsius_to_fahrenheit(temp)
        fahrenheit_list.append(f)
        print(f)

    return fahrenheit_list

# Function to find highest Fahrenheit temperature
def highest_temperature(fahrenheit_list):
    return max(fahrenheit_list)

# Function to find lowest Fahrenheit temperature
def lowest_temperature(fahrenheit_list):
    return min(fahrenheit_list)

# Function to calculate average Fahrenheit temperature
def average_temperature(fahrenheit_list):
    return sum(fahrenheit_list) / len(fahrenheit_list)

# Main Program
fahrenheit_temperatures = display_fahrenheit(temperatures)

print("\nHighest Temperature:", highest_temperature(fahrenheit_temperatures), "°F")
print("Lowest Temperature:", lowest_temperature(fahrenheit_temperatures), "°F")
print("Average Temperature:", round(average_temperature(fahrenheit_temperatures), 2), "°F")