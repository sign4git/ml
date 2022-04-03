import requests
from bs4 import BeautifulSoup

response = requests.\
    get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text,"html.parser")
movies_tag = soup.find_all(name="h3" ,class_="title")
movies_list = []
with open("movies_to_watch.txt",mode="w") as file:
    for movies in movies_tag:
        movies_list.append(movies.getText())
        file.writelines(movies.getText()+"\n")


