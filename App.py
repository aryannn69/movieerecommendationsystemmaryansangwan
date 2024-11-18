import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
     response = requests.get('http://api.themoviedb.org/3/movie/{}?api_key=9d48c33fb71267a595d3337e7eeac232&language=en-US'.format(movie_id))
     data = response.json()
     print (data)
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:21]

    recommended_movies =  []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('MOVIE RECOMMENDATION SYSTEM')

selected_movie_name = st.selectbox(
    "Choose Movie to Recommend",
    (movies['title'].values),
)

if st.button('Show Recommendations'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5, = st.columns(5)
    with col1:
        st.image(posters[0])
    with col2:
        st.image(posters[1])
    with col3:
        st.image(posters[2])
    with col4:
        st.image(posters[3])
    with col5:
        st.image(posters[4])
        
    col6, col7, col8, col9, col10, = st.columns(5)
    with col1:
        st.image(posters[5])
    with col2:
        st.image(posters[6])
    with col3:
        st.image(posters[7])
    with col4:
        st.image(posters[8])
    with col5:
        st.image(posters[9])

    co11, col12, co13, co14, col15, = st.columns(5)
    with col1:
        st.image(posters[10])
    with col2:
        st.image(posters[11])
    with col3:
        st.image(posters[12])
    with col4:
        st.image(posters[13])
    with col5:
        st.image(posters[14])

    col16, col17, col18, col19, col20, = st.columns(5)
    with col1:
        st.image(posters[15])
    with col2:
        st.image(posters[16])
    with col3:
        st.image(posters[17])
    with col4:
        st.image(posters[18])
    with col5:
        st.image(posters[19])

