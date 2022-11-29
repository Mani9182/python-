import sqlite3

con = sqlite3.connect('q2.db')

cursor = con.cursor()

cursor.execute(
    "CREATE TABLE movies (movie_id integer, movie_name text, genre text, language text, rating real)")

movies = [
    (101, "John Wick", "action", "english", 7.9),
    (102, "kgf2", "superhero", "hindi", 1.2),
    (103, "doctor strange", "mystic", "english", 9.1),
]

cursor.executemany("INSERT INTO movies VALUES (?, ?, ?, ?, ?)", movies)

cursor.execute("UPDATE movies SET rating = (rating + (rating * 0.1))")
cursor.execute("SELECT * FROM movies")
print(cursor.fetchall())

cursor.execute("DELETE from movies WHERE movie_id = 102")
cursor.execute("SELECT * FROM movies")
print(cursor.fetchall())

cursor.execute("SELECT movie_name, rating FROM movies WHERE rating > 3")
print(cursor.fetchall())

con.commit()

con.close()
