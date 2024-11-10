import sqlite3



# Create a connection to a new database (or connect to an existing one)

conn = sqlite3.connect('movies.db')



# Create a cursor object

cursor = conn.cursor()



# Don't forget to close the connection when you're done!

conn.close()





conn = sqlite3.connect('movies.db')

cursor = conn.cursor()



# Insert a single movie using string formatting (UNSAFE - vulnerable to SQL injection)

movie = ('The Godfather', 'Francis Ford Coppola', 1972, 9.2)

cursor.execute(f'''

INSERT INTO movies (title, director, year, rating)

VALUES ('{movie[0]}', '{movie[1]}', {movie[2]}, {movie[3]})

''')



# Insert a single movie using a parameterized query (SAFE)

cursor.execute('''

INSERT INTO movies (title, director, year, rating)

VALUES (?, ?, ?, ?)

''', ('Pulp Fiction', 'Quentin Tarantino', 1994, 8.9))



# List of movies to insert

movies = [

    ('The Shawshank Redemption', 'Frank Darabont', 1994, 9.3),

    ('Inception', 'Christopher Nolan', 2010, 8.8),

    ('The Matrix', 'Lana and Lilly Wachowski', 1999, 8.7),

    ('Interstellar', 'Christopher Nolan', 2014, 8.6)

]



# Insert multiple movies

cursor.executemany('''

INSERT INTO movies (title, director, year, rating)

VALUES (?, ?, ?, ?)

''', movies)



# Commit the changes and close the connection

conn.commit()

conn.close()

conn = sqlite3.connect('movies.db')

cursor = conn.cursor()



# Select all movies

cursor.execute('SELECT * FROM movies')

all_movies = cursor.fetchall()

print("All movies:")

for movie in all_movies:

    print(movie)



# Select movies after 2000

cursor.execute('SELECT title, year FROM movies WHERE year > 2000')

recent_movies = cursor.fetchall()

print("\nMovies after 2000:")

for movie in recent_movies:

    print(f"{movie[0]} ({movie[1]})")



# Select average rating

cursor.execute('SELECT AVG(rating) FROM movies')

avg_rating = cursor.fetchone()[0]

print(f"\nAverage rating: {avg_rating:.2f}")



conn.close()