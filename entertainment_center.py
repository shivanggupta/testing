import media
import fresh_tomatoes

moviename = media.Movie("The Martian", "Matt Damon gets stuck in space!", "http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SY317_CR0,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=ej3ioOneTy8")
moviename2 = media.Movie("Everest", "Keira Knigthley gets stuck on a mountain", "http://ia.media-imdb.com/images/M/MV5BMjMzMjIxOTIxMl5BMl5BanBnXkFtZTgwNTk4NDI0NjE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=dOHS-mxn0RQ")
moviename3 = media.Movie("Hitman", "Reminds me of Benji", "http://ia.media-imdb.com/images/M/MV5BMTY3NTQyMDY0Ml5BMl5BanBnXkFtZTgwODkzMjI0NjE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=alQlJDRnQkE")

movie_list = [moviename,moviename2,moviename3]

fresh_tomatoes.open_movies_page(movie_list)