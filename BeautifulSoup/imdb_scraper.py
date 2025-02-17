from imdb import IMDb
import pandas as pd

# Initialize IMDb instance
ia = IMDb()

# Fetch top 250 movies
top_movies = ia.get_top250_movies()

# Prepare an empty list to store movie data
movies_data = []

# Extract necessary details for each movie
for movie in top_movies:
    try:
        # Get movie details
        movie_details = ia.get_movie(movie.movieID)
        title = movie_details.get('title', 'N/A')
        year = movie_details.get('year', 'N/A')
        rating = movie_details.get('rating', 'N/A')
        genres = ', '.join(movie_details.get('genres', []))
        directors = ', '.join([person['name'] for person in movie_details.get('directors', [])])
        votes = movie_details.get('votes', 'N/A')

        # Append data to the list
        movies_data.append({
            'Title': title,
            'Year': year,
            'Rating': rating,
            'Genres': genres,
            'Directors': directors,
            'Votes': votes
        })

    except Exception as e:
        print(f"Error fetching data for movie ID {movie.movieID}: {e}")

# Convert list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(movies_data)

# Save the DataFrame to a CSV file
output_file = "imdb_top250_movies.csv"
df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Data successfully saved to {output_file}")
