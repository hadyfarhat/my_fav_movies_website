import movies
import fresh_tomatoes

the_butler = movies.Movie("The Butler",
                          "Cecil Gaines gets the opportunity of a lifetime"
                          " when he is hired as a butler at the White House.",
                          "http://weinsteinco.com/sites/leedanielsthebutler/"
                          "images/TheButler.jpg",
                          "https://www.youtube.com/watch?v=FuojHqfe4Vk")

concussion = movies.Movie("Concussion",
                          "Dr. Bennet Omalu discovers neurological"
                          " deterioration that is similar to"
                          " Alzheimer's disease.",
                          "http://taylorholmes.com/wp-content/uploads"
                          "/2015/12/concussion-failed-movie.jpg",
                          "https://www.youtube.com/watch?v=Io6hPdC41RM")

deadpool = movies.Movie("Deadpool",
                        "Wade Wilson's world comes crashing down when"
                        " evil scientist Ajax tortures, disfigures and"
                        " transforms him into Deadpool.",
                        "http://www.space.ca/wp-content/uploads/2016/09"
                        "/deadpool.jpg",
                        "https://www.youtube.com/watch?v=ZIM1HydF9UA")

movies = [the_butler, concussion, deadpool]

fresh_tomatoes.open_movies_page(movies)
