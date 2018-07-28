import media
import fresh_tomatoes

# Creating the objects of movies

rampage = media.Movie(
    "Rampage",
    "A story about the Gorilla that grows like giant because of experiment",
    "images/rampage.jpeg",
    "https://www.youtube.com/watch?v=coOKvrsmQiI")

jumanji = media.Movie(
    "Jumanji",
    "4 kids in game world",
    "images/jumanji.jpeg",
    "https://www.youtube.com/watch?v=2QKg5SZ_35I")


batman = media.Movie(
    "Batman: the dark knight rises",
    "A story about the hero in Gotham city",
    "images/batman.jpeg",
    "https://www.youtube.com/watch?v=GokKUqLcvD8")

madmax = media.Movie(
    "Mad Max",
    "Story about the hero in wasteland",
    "images/madmax.jpeg",
    "https://www.youtube.com/watch?v=hEJnMQG9ev8")


ratatouille = media.Movie(
    "Ratatouille",
    "Storyline",
    "images/rat.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie(
    "Hunger Games",
    "Storyline",
    "images/hunger.jpeg",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")


#Creating the list of movies from the created objects
movies = [rampage, jumanji, batman, madmax, ratatouille, hunger_games]

#Call the function open_movies_page from module fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)


