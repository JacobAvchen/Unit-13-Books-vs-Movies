Project 2: ETL Challenge
Jacob Avchen, Jacob Hollander, Salvatore Russo
The Jupyter Notebooks in our project are designed to extract, transform, and load data about book reviews, movie reviews, and a link between the two with a table that connects movies with the books they were based on in an effort to see the relation between how well a book was rated and how well the movie based on it was rated.
The program takes 4 tables based on data from Kaggle, IMDB, and Wikipedia and normalizes the data in order to be compared in PostgreSQL.
The following processes were completed using BeautifulSoup and Pandas’ built-in read_csv function to perform operations.
EXTRACT:
1.	books.csv - source: kaggle.com
2.	title.basics.tsv.gz - source: IMDB Data Files
3.	title.ratings.tsv.gz - source: IMDB Data Files
4.	Wikipedia’s list of fiction works with feature film adaptations using BeautifulSoup - source: Wikipedia
TRANSFORM:
1.	Books
a.	Remove unnecessary columns
b.	Clean titles to standard format with no parentheses
c.	Change column names to standard underscore notation
2.	Movies
a.	Remove unnecessary columns
b.	Remove entries that are not movies, ie: shorts, tv shows, etc.
c.	Remove entries with no release year, or that have not been released yet
d.	Remove entries with no entry in ratings_df via the tconst column
e.	Change column names to standard underscore notation
3.	Ratings
a.	Remove entries with no entry in movie_df via the tconst column
b.	Change column names to standard underscore notation
4.	Wiki
a.	Create single A-Z dataframe from 4 separate alphabetized tables
b.	Clean book titles to standard format with no parentheses
c.	Change column names to standard underscore notation
LOAD:
Before we loaded the data into PostgreSQL, we had to create the books_movies_db on our local computers in pgAdmin4 to store it. We loaded the data into PostgreSQL using SQLAlchemy and Pandas’ to_sql function to create tables for each dataframe in books_movies_db and load the data in at once. Below are diagrams of the relations between the tables on quickdatabasediagrams.com and a visualization of the entire ETL process.


Challenges and Limitations:
During this project we ran into a few challenges. Taking data from multiple different sources, each source had their own way of formatting the titles of books and movies. This made it difficult to relate them to each other when one source had a book titled “Harry Potter and the Prisoner of Azkaban (1999)” and the other had it titled “Harry Potter and the Prisoner of Azkaban (Harry Potter #3)”. This was easily solved by removing everything in the parentheses for both columns, but the problem was even worse when relating the movies to each other because, in some cases, multiple movies had been made of the same book. Wikipedia’s table denoted this by having all movies made of a single book in one cell. This led us to relate our own movies.primary_title to wiki.movie_title by looking in wiki.movie_title for the string found in movies.primary_title using the following Join in our SQL Query.
“INNER JOIN wiki AS w ON POSITION (m[ovies].primary_title IN w.movie_title)<>0”
This query allows us to find movie titles in the wiki table even if the title as it’s written in the movies table is only part of the value in the wiki table. In theory this worked and returned the values we needed, but it ran into problems when it looked for simple movie titles like “Brother” and “L” and found every instance of “Brother” and “L” and thought it had found books related to those movies, when in reality it had found “My Blind Brother” for both movies because the title “My Blind Brother” contains both “Brother” and “L”. Given more time, this issue could be solved with more intensive cleaning of the wiki.movie_title column and a stricter query to find only titles that matched exactly.
