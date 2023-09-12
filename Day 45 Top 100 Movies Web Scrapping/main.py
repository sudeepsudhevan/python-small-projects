import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
empire_website = response.text

soup = BeautifulSoup(empire_website, "html.parser")

films = soup.find_all(name="h3", class_="title")
# print(films)

# for film in films[::-1]:   # reverse the list by using [::-1]
#     film_title = film.getText()
#     with open("movie.txt", "a", encoding="UTF8") as file:
#         file.write(f"{film_title}\n")                         # it append same thing for every run

movie_titles = [film.getText() for film in films]
movies = movie_titles[::-1]
print(movies)

with open("movie.txt", "w", encoding="UTF8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
