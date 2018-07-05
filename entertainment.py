import media
import fresh_tomatoes

# Movie details

Jilla = media.Movie("Jilla", "Jilla is a crime-drama which"
                    " shows the relationship between father and son",
                    "https://goo.gl/AQkEFU",
                    "https://www.youtube.com/watch?v=VyectFJCP_s"
                    )

Tangled = media.Movie("Tangled","This movie is about Rapunzel a princess"
                      "who lives with witch who lives with the power of"
                      " the princess hair how she mets her love of life"
                      " and met her parents portraits the movie",
                      "https://goo.gl/a5NfZv",
                      "https://www.youtube.com/watch?v=JYKpIr1lSG0"
                      )                                       
Frozen = media.Movie("Frozen",
                     "A movie which explains the bond between two sisters one "
                     "born with the boon which later become dangerous to her little sister",
                     "https://goo.gl/6W2NUm",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc"
                     )

# creating a list of all the movies
list_of_movies = [
                  Jilla,
                  Tangled,
                  Frozen,
                 ]

# sending the list to fresh_tomatoes.py file to open web page
fresh_tomatoes.open_movies_page(list_of_movies)
