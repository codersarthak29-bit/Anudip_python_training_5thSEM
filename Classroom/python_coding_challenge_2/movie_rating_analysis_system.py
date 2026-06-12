'''Problem Statement 
Ratings given by users for movies are stored below. 
Sample Data 
ratings = { 
    "Inception": 4.8, 
    "Avatar": 4.3, 
    "Titanic": 4.5, 
    "Joker": 4.7, 
    "Frozen": 3.8, 
    "Interstellar": 4.9, 
    "Dune": 4.6, 
    "Up": 4.1, 
    "Coco": 4.4, 
    "Cars": 3.9 
} 
Tasks 
1. Display movies rated above 4.5.  
2. Find the highest-rated movie.  
3. Find the lowest-rated movie.  
4. Calculate average rating.  
5. Create a recommendation list (rating ≥ 4.5). '''
#program to make  Movie Rating Analysis System 
ratings = { 
    "Inception": 4.8, 
    "Avatar": 4.3, 
    "Titanic": 4.5, 
    "Joker": 4.7, 
    "Frozen": 3.8, 
    "Interstellar": 4.9, 
    "Dune": 4.6, 
    "Up": 4.1, 
    "Coco": 4.4, 
    "Cars": 3.9 
}
#task1:Display movies rated above 4.5.  
for movie,rate in ratings.items():
    if rate > 4.5:
        print(movie)
#task2:Find the highest-rated movie.
highest_rated_movie = max(ratings, key=ratings.get)
print(f"The highest-rated movie is: {highest_rated_movie} with a rating of {ratings[highest_rated_movie]}")
#task3:Find the lowest-rated movie.
lowest_rated_movie = min(ratings, key=ratings.get)
print(f"Lowest rating Movie: {lowest_rated_movie} with a rating of {ratings[lowest_rated_movie]}")
#task4:Calculate average rating.
average_rating = sum(ratings.values()) / len(ratings)
print(f"The average rating of all movies is: {average_rating:.2f}")
#task5:Create a recommendation list (rating >= 4.5).
print("Recommended Movies (rating >= 4.5):")
recommended=[]
for movie, rating in ratings.items():
    if rating >= 4.5:
        recommended.append(movie)
print(recommended)

