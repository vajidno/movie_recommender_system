import streamlit as st
import pickle
import pandas as pd
import requests
import gzip

# Function to fetch movie poster
def fetch_poster(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=e5a82cdc41770314fc6e9df762e593e2&language=en-US".format(
            movie_id
        )
    )
    data = response.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function for movie recommendation
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movie_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies, recommended_movie_poster

# Load data and similarity
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

# Load compressed similarity data
with gzip.open("compressed_similarity.pkl.gz", "rb") as f:
    similarity = pickle.load(f)

# Set page configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
)

# App title
st.title("🎬 Movie Recommender System")

# User input
selected_movie_name = st.selectbox("Select a movie:", movies["title"].values)

# Recommendation button
if st.button("Get Recommendations"):
    recommended_movie_names, recommended_movie_posters = recommend(
        selected_movie_name
    )

    # Display recommended movies and posters in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
