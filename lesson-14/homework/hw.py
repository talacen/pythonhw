import json
import requests
import random
import os


data = '''{
    "Student":
                [
                    {
                        "id":7,
                        "name":"Alex",
                        "age":25,
                        "pets":["dogs","cats","bird"],
                        "FamilyMembers":
                            [
                                {
                                    "name":"David",
                                    "age":56,
                                    "relative":"father"
                                    
                                },
                                {
                                    "name":"Sara",
                                    "age":53,
                                    "relative":"mother"
                                    
                                },
                                {
                                    "name":"Rob",
                                    "age":26,
                                    "relative":"brother"
                                }
                            ]
                    },
                    {
                        "id":8,
                        "name":"Mironshox",
                        "age":19,
                        "pets":["dogs","cats","bird"],
                        "FamilyMembers":
                            [
                                {
                                    "name":"A",
                                    "age":45,
                                    "relative":"father"
                                    
                                },
                                {
                                    "name":"B",
                                    "age":42,
                                    "relative":"mother"
                                    
                                },
                                {
                                    "name":"Islom",
                                    "age":21,
                                    "relative":"brother"
                                }
                            ]
                    }
                ]
}'''

# Task 1: JSON Parsing
def parse_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        for student in data.get("students", []):
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# Task 2: Weather API
def fetch_weather(city):
    api_key = '730b0b038bf29d425d0c9a5efcc72433'  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        print(f"Weather in {city}: {temp}°C, {humidity}% humidity, {description}")
    else:
        print("Failed to fetch weather data.")

# Task 3: JSON Modification
def modify_books(filename):
    with open(filename, 'r+') as file:
        data = json.load(file)
        print("1. Add Book\n2. Update Book\n3. Delete Book")
        choice = int(input("Choose an option: "))
        if choice == 1:
            title = input("Title: ")
            author = input("Author: ")
            data["books"].append({"title": title, "author": author})
        elif choice == 2:
            title = input("Title to update: ")
            for book in data["books"]:
                if book["title"] == title:
                    book["author"] = input("New Author: ")
        elif choice == 3:
            title = input("Title to delete: ")
            data["books"] = [book for book in data["books"] if book["title"] != title]
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

# Task 4: Movie Recommendation System
def movie_recommendation(genre):
    api_key = 'aeba228'  
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get("Search", [])
        if movies:
            movie = random.choice(movies)
            print(f"Recommended Movie: {movie['Title']} ({movie['Year']})")
        else:
            print("No movies found for the given genre.")
    else:
        print("Failed to fetch movie data.")

os.chdir("c:/Users/firad/Desktop/pythonhw/pythonhw/lesson-14/homework")

# Example usage
if __name__ == "__main__":
    print("Task 1: JSON Parsing")
    parse_json("students.json")
    print("\nTask 2: Weather API")
    fetch_weather("Tashkent")
    print("\nTask 3: JSON Modification")
    modify_books("books.json")
    print("\nTask 4: Movie Recommendation System")
    genre = input("Enter movie genre: ")
    movie_recommendation(genre)

