#import dependencies
import pandas as pd
import numpy as np

#file
csv_path = "../../Resources/books.csv"

#read
books_df = pd.read_csv(csv_path)

#check df
#books_df

#clean the data
clean_books_df = books_df[['bookID', 'title', 'authors', 'average_rating', 'ratings_count', 'text_reviews_count', 'publication_date', 'publisher']]

#check cleaned data
#clean_books_df