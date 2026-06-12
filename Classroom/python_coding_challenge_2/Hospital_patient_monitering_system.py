'''Problem Statement 
Patient heart rates are recorded below. 
Sample Data 
heart_rate = { 
    "P101": 72, 
    "P102": 105, 
    "P103": 88, 
    "P104": 120, 
    "P105": 65, 
    "P106": 98, 
    "P107": 110, 
    "P108": 70, 
    "P109": 85, 
    "P110": 130 
} 
Tasks 
1. Display critical patients (heart rate >100).  
2. Find highest and lowest heart rate.  
3. Calculate average heart rate.  
4. Count stable patients (60–100 bpm). '''
#program to make Hospital Patient Monitoring System 

heart_rate = { 
    "P101": 72, 
    "P102": 105, 
    "P103": 88, 
    "P104": 120, 
    "P105": 65, 
    "P106": 98, 
    "P107": 110, 
    "P108": 70, 
    "P109": 85, 
    "P110": 130 
}
#task1:Display critical patients (heart rate >100). 
print("Critical Patients: ")
for pid, rate in heart_rate.items():
    if rate > 100:
        print(f"Patient ID: {pid}, Heart Rate: {rate}")

#task2:Find highest and lowest heart rate. 
highest_rate = max(heart_rate,key=heart_rate.get)
lowest_rate = min(heart_rate,key=heart_rate.get)
print(f"Highest Heart Rate: ",highest_rate,heart_rate[highest_rate],"bpm")
print(f"Lowest Heart Rate: ",lowest_rate,heart_rate[lowest_rate],"bpm")
#task3:Calculate average heart rate.
average_heart_rate = sum(heart_rate.values()) / len(heart_rate)
print(f"Average Heart Rate: {average_heart_rate:.2f} bpm")
#task4:Count stable patients (60–100 bpm).
stable_patients_count = sum(1 for rate in heart_rate.values() if 60 <= rate <= 100)
print(f"Number of Stable Patients: {stable_patients_count}")
