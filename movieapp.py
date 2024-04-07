import streamlit as st
import pandas as pd
import numpy as np

# Function to get recommendations based on selected movies
def get_recommendations(selected_movies):
    # Your recommendation logic goes here
    recommendations = ["Recommendation 1", "Recommendation 2", "Recommendation 3"]
    return recommendations

# Read movie titles from the CSV file if it exists
movies_df = pd.read_csv("movies.csv") if "movies.csv" in os.listdir() else None
# If movies_df is None or empty, fallback to the default list
movies = movies_df["title"].tolist() if movies_df is not None else ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"]

# Streamlit app
def main():
    st.title("Movie Recommender System")
    
    # Select multiple movies
    selected_movies = st.multiselect("Select Movies", movies)
    
    if st.button("Get Recommendations"):
        recommendations = get_recommendations(selected_movies)
        st.write("Here are your movie recommendations based on your selection:")
        for recommendation in recommendations:
            st.write(recommendation)
        
        # Redirect to another page
        st.experimental_set_query_params(recommendations=recommendations)
    
    # Display in small text
    st.write("A project by:")
    
    # Display images and names (replace the placeholders with actual images and names)
    # Display images and names
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image("me.JPG", caption="Ajay Macharla")
    with col2:
        st.image("movva.jpeg", caption="Ravi Teja Movva")
    with col3:
        st.image("shashi.jpeg", caption="Shashi Karrenagari")
    with col4:
        st.image("me.JPG", caption="Rakesh Pallagani")
    with col5:
        st.image("sriram.jpeg", caption="Sriram Ganeshraj")

# Call the main function
if __name__ == "__main__":
    main()
