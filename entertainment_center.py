import media
import fresh_tomatoes

# Creating the objects of movies

rampage = media.Movie("Rampage",
                      "A story about the Gorilla that grows like giant because of experiment",
                      "http://t1.gstatic.com/images?q=tbn:ANd9GcQpTCKCvU_Fz0SwP_oyuSSKdf_unn88WWa5evQC4F3U7EfHyQVJ",
                      "https://www.youtube.com/watch?v=coOKvrsmQiI")

jumanji = media.Movie("Jumanji",
                     "4 kids in game world",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcSGLiKxLm4FSbjNzysaI8xVoUEE27RDObZg9pSiP28nvSEwy7Mb",
                     "hhttps://www.youtube.com/watch?v=2QKg5SZ_35I")


batman = media.Movie("Batman: the dark knight rises",
                     "A story about the hero in Gotham city",
                     "http://t1.gstatic.com/images?q=tbn:ANd9GcQSGF8_VbDqKF0B_4IQ0NF87VMDSy7_MPKryawR-qLnSIPQwo5z",
                     "https://www.youtube.com/watch?v=GokKUqLcvD8")

madmax= media.Movie("Mad Max",
                    "Story about the hero in wasteland",
                    "http://t0.gstatic.com/images?q=tbn:ANd9GcQuK41mExh1Qv3kbXoxohWYGlcstOQ6zEnnNdSI2BGIKywQwgRI",
                    "https://www.youtube.com/watch?v=hEJnMQG9ev8")


ratatouille = media.Movie("Ratatouille",
                          "Storyline",
                          "http://www.gstatic.com/tv/thumb/movieposters/165058/p165058_p_v8_aj.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("Hunger Games",
                          "Storyline",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcS58mYVyiI3LTihImFjn6QBLU_mcHXZP3LaGoWN9u5bzuvW3lvC",
                          "https://www.youtube.com/watch?v=mfmrPu43DF8"
                        )


#Creating the list of movies from the created objects
movies = [rampage, jumanji, batman, madmax, ratatouille, hunger_games]

#Call the function open_movies_page from module fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)


