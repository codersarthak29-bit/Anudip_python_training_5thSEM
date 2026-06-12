'''Daily mobile screen time (in minutes) of a student is recorded for 10 days. 
Sample Data 
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260] 
Tasks 
1. Calculate average screen time.  
2. Find the highest and lowest screen time.  
3. Count days exceeding 200 minutes.  
4. Display days with healthy usage (<180 minutes).  
5. Categorize usage:  
o Healthy (<180)  
o Moderate (180–240)  
o Excessive (>240) '''
#program to make Mobile Screen Time Analyzer 
#screen times:
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260] 
#task1:Calculate average screen time.  
avg_screen_time=sum(screen_time)/len(screen_time)
print("Average screen time:",avg_screen_time,"minutes")
#task2:Find the highest and lowest screen time.
highest=max(screen_time)
lowest=min(screen_time)  
print("Highest screen time:",highest,"minutes")
print("Lowest screen time:",lowest,"minutes")
#task3:Count days exceeding 200 minutes. 
exceeding_200_minutes=0
for time in screen_time:
    if time > 200:
        exceeding_200_minutes+=1
print("Days exceeding 200 minutes:",exceeding_200_minutes,"days")
#task4:Display days with healthy usage (<180 minutes).
print("Healthy Usage Days: ")
for day in range(len(screen_time)):
    if screen_time[day]< 180:
        print("Day ", day + 1, ":", screen_time[day], "minutes")
#task5:Categorize usage:
healthy = 0
moderate = 0
excessive = 0
for time in screen_time:
    if time < 180:
        healthy += 1
    elif 180 <= time <= 240:
        moderate += 1
    else:
        excessive += 1
print("Healthy usage days:", healthy)
print("Moderate usage days:", moderate)
print("Excessive usage days:", excessive)
