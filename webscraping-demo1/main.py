from bs4 import BeautifulSoup
import requests

data = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
soup = BeautifulSoup(data.text, "html.parser")

header = ['Serial No', 'Title', 'Year', 'Rating']
movies = []

titles_with_tags = soup.find_all("td", "titleColumn")
ratings_with_tags = soup.find_all("td", "ratingColumn imdbRating")

serial_no = []
title = []
year = []
rating = []


print(header)
for i in range(0, len(titles_with_tags)):
    
    serial_no.append(i+1)
    title.append(titles_with_tags[i].a.text)
    year.append(titles_with_tags[i].span.text)
    rating.append(ratings_with_tags[i].text.strip())
    
    movie = []
    movie.append(serial_no[i])
    movie.append(title[i])
    movie.append(year[i])
    movie.append(rating[i])
    movies.append(movie)

    
for movie in movies:
    print(movie)
