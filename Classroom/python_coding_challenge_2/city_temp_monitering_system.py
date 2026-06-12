'''Problem Statement 
Daily temperatures of different cities are stored below. 
Sample Data 
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
Tasks 
1. Display cities with temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (<35°C).  
'''
#program to make  City Temperature Monitoring System 
#sample data:
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
#task1:Display cities with temperature above 40°C. 
print("Cities Above 40°C: ")
for city,temp in temperature.items():
    if temp>40:
        print(city)
#task2:Find the hottest city.  
hottest=max(temperature,key=temperature.get)

print(f"Hottest city: ",hottest,temperature[hottest],"°C")
#task3:Find the coolest city.
coolest=min(temperature,key=temperature.get)
print(f"Coolest city: ",coolest,temperature[coolest],"°C")
#task4:Calculate average temperature.
average_temp=sum(temperature.values())/len(temperature)
print(f"Average Temperature: ",average_temp)
#task5: Create a list of pleasant cities (<35°C).  
pleasant_cities=[]
for city,temp in temperature.items():
    if temp<35:
        pleasant_cities.append(city)
print(f"Pleasant Cities: ",pleasant_cities)
