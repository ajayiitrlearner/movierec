import streamlit as st
import pandas as pd
import numpy as np

# Function to get recommendations based on selected movies
def get_recommendations(selected_movies):
    # Your recommendation logic goes here
    recommendations = ["Recommendation 1", "Recommendation 2", "Recommendation 3"]
    return recommendations

# List of movies
movies = ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"]

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
    # Check if the script is run as the main module
    if __name__ == "__main__":
        main()

# Display images and names (replace the placeholders with actual images and names)
# Move this code block outside of the main() function to ensure it's executed after the main content
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image("me.JPG", caption="Ajay Macharla")
with col2:
    st.image("movva.jpeg", caption="Ravi Teja Movva")
with col3:
    st.image("me.JPG", caption="Shashi Karrenagari")
with col4:
    st.image("me.JPG", caption="Rakesh Pallagani")
with col5:
    st.image("me.JPG", caption="Sri Ram")
