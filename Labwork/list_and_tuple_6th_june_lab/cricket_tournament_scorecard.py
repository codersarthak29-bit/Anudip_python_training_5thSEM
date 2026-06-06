'''A batsman's scores in different matches are stored in a list. 
scores = [45, 78, 12, 100, 67, 8, 90, 55] 
Write a program to: 
• Count half-centuries and centuries.  
• Find the highest score.  
• Display all scores below 20.  
• Calculate the average score. '''
scores = [45, 78, 12, 100, 67, 8, 90, 55] 
#Task1: Count half-centuries and centuries
half_centuries=0
centuries=0
for i in scores:
    if i>=50 and i<100:
        half_centuries+=1
    if i>=100:
        centuries+=1
print("Half Centuries: ",half_centuries)
print("Centuries: ",centuries)
#Task2:Find the highest score.
highest=scores[0]
for i in scores:
    if i>highest:
        highest=i
print("The highest score is: ",highest)
#Task3: Display all scores below 20.
print("The scores under 20 are: ")
for i in scores:
    if i<20:
        print(i)
#Task4:Calculate the average score.
total=sum(scores)
num=len(scores)
avg=total/num
print("The average score is : ",avg)