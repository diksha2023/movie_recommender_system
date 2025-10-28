import streamlit as st
import pickle
import pandas as pd
import requests
from joblib import load


movies_df = pickle.load(open("movies.pkl", "rb"))
#similarity = pickle.load(open("similarity.pkl","rb"))
similarity = load('similarity1.pkl')

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=c55042c46a5a74e6980a1266355832e6".format(movie_id))
    data = response.json()
    #print(data)
    return  "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies_df[movies_df["title"]==movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key = lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies_df.iloc[i[0]].id

        recommended_movies.append(movies_df.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie you like:",
    movies_df["title"].values
)

if st.button("Recommend"):
    names, poster = recommend(selected_movie_name)
    st.write("### Recommended Movies:")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
