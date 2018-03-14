import movie
import fresh_tomatoes

# Create movies.
pans_labyrinth = movie.Movie("Pan's Labyrinth",
                             "https://upload.wikimedia.org/wikipedia/"
                             "en/6/67/Pan%27s_Labyrinth.jpg",
                             "https://www.youtube.com/watch?v=4Evmr2ZCjWc")

pacific_rim = movie.Movie("Pacific Rim",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/f/f3/Pacific_Rim_FilmPoster.jpeg",
                          "https://www.youtube.com/watch?v=-hNVKNFsyu0")

the_simpsons = movie.Movie("The Simpsons Movie",
                           "https://upload.wikimedia.org/wikipedia/"
                           "en/thumb/a/a0/Simpsons_final_poster.png/"
                           "220px-Simpsons_final_poster.png",
                           "https://www.youtube.com/watch?v=PulHR2LfPVk")

it = movie.Movie("IT",
                 "https://upload.wikimedia.org/wikipedia/"
                 "en/5/5a/It_%282017%29_poster.jpg",
                 "https://www.youtube.com/watch?v=xKJmEC5ieOk")

full_metal = movie.Movie("Full Metal Alchemist",
                         "https://upload.wikimedia.org/wikipedia/"
                         "en/d/dc/Fullmetal_Alchemist.png",
                         "https://www.youtube.com/watch?v=azPVumixZuE")

tokyo_ghoul = movie.Movie("Tokyo Ghoul",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/thumb/f/fa/Tokyo_Ghoul_%28film%29_poster.jpeg/"
                          "220px-Tokyo_Ghoul_%28film%29_poster.jpeg",
                          "https://www.youtube.com/watch?v=YQ6NAu6HW6w")

# Fill movies array.
movies = [
    pans_labyrinth,
    pacific_rim,
    the_simpsons,
    it,
    full_metal,
    tokyo_ghoul
    ]

# Display web page with favorite movies.
fresh_tomatoes.open_movies_page(movies)
