f = open("movies.txt")

allLines = f.readlines()

f.close()

uniqueMovies = set()

for line in allLines:
    line = line.strip()
    info = line.split(", ") # always split returns a list of strings
    movies = info[1:] # a list of movies
    for movie in movies:
        movie = movie.strip() # removes all white-spaces from beginning and end
        uniqueMovies.add(movie)

print("Number of unique movies:", len(uniqueMovies))

for i in range(5):
    if len(uniqueMovies) == 0:
        break
    minMovie = min(uniqueMovies)
    print(minMovie)
    uniqueMovies.remove(minMovie)