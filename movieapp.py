import streamlit as st
import pandas as pd
import numpy as np
import os  # Import the os module
import warnings
from warnings import filterwarnings
filterwarnings('ignore')

column_movies = ["movieId", "title", "genres"] 
column_ratings = ["userId", "movieId", "rating", "timestamp"]

movies = pd.read_csv("movies2.csv")
ratings = pd.read_csv("ratings.csv")

movie_ratings = pd.merge(movies, ratings, on='movieId', how='inner')
movie_ratings.drop('timestamp', axis=1, inplace=True)

reviews = movie_ratings.groupby(['title'])['rating'].agg(['count','mean']).round(1)

movie_ratings = movie_ratings.astype({'movieId': 'int32', 'userId': 'int32', 'genres': 'category'})

user_counts = movie_ratings['userId'].value_counts()

valid_user_ids = user_counts[user_counts > 0].index
filtered_ratings = movie_ratings[movie_ratings['userId'].isin(valid_user_ids)]

user_rating_list = [] 
user_rating = pd.DataFrame()

batch_size = 5000  # Set the batch size
total_users = len(valid_user_ids)
num_batches = total_users // batch_size + 1
for i in range(num_batches):
    start_index = i * batch_size
    end_index = start_index + batch_size
    batch_users = valid_user_ids[start_index:end_index]

    batch_mov = pd.crosstab(index=filtered_ratings[filtered_ratings['userId'].isin(batch_users)]['userId'],
                            columns=filtered_ratings[filtered_ratings['userId'].isin(batch_users)]['title'],
                            values=filtered_ratings[filtered_ratings['userId'].isin(batch_users)]['rating'],
                            aggfunc='sum')
    user_rating_list.append(batch_mov)

user_rating = pd.concat(user_rating_list, ignore_index=True)

# Function to get recommendations based on selected movies
def get_recommendations(selected_movies):
    
    userInput = selected_movies
    
    similarity = user_rating.corrwith(user_rating[userInput[0]], method='pearson') \
                 + user_rating.corrwith(user_rating[userInput[1]], method='pearson') \
                 + user_rating.corrwith(user_rating[userInput[2]], method='pearson')
    
    correlatedMovies = pd.DataFrame(similarity, columns=['correlation'])
    correlatedMovies = pd.merge(correlatedMovies, reviews, on='title')
    correlatedMovies = pd.merge(correlatedMovies, movies, on='title')
    
    final_recommendation = correlatedMovies.query('mean > 3.5 and count > 300').sort_values('correlation', ascending=False)
    final_recommendation = final_recommendation[np.isin(final_recommendation['title'], userInput, invert=True)]
    recommendations =  final_recommendation['title'].head(3).tolist()
    
    return recommendations

# Read movie titles from the CSV file if it exists
movies_df = pd.read_csv("movies2.csv") if "movies2.csv" in os.listdir() else None
# If movies_df is None or empty, fallback to the default list
movies2 = movies_df["title"].tolist() if movies_df is not None else ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"]

# Streamlit app
def main():
    st.title("Movie Recommender System")
    
    # Select multiple movies
    selected_movies = st.multiselect("Select Movies", movies2)
    
    if st.button("Get Recommendations"):
        recommendations = get_recommendations(selected_movies)
        st.write("Here are your movie recommendations based on your selection:")
        for recommendation in recommendations:
            st.write(recommendation)
        
        # Feedback
        st.write("Please provide feedback:")
        thumbs_up = st.button("👍")
        thumbs_down = st.button("👎")
        if thumbs_up:
            st.write("You liked the recommendations! Thanks for the feedback.")
        elif thumbs_down:
            st.write("We're sorry you didn't like the recommendations. We'll try to improve.")
        
        # Redirect to another page
        st.experimental_set_query_params(recommendations=recommendations)
    
    # Display in small text
    st.write("A project by:")
    
    # Display images and names (replace the placeholders with actual images and names)
    # Display images and names
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image("ajay.jpg", caption="Ajay Macharla")
    with col2:
        st.image("ravi.jpg", caption="Ravi Teja Movva")
    with col3:
        st.image("shashi.jpeg", caption="Shashi Karrenagari")
    with col4:
        st.image("rakesh.jpg", caption="Rakesh Pallagani")
    with col5:
        st.image("sriram.jpg", caption="Sriram Ganeshraj")

# Call the main function
if __name__ == "__main__":
    main()
