# to run app -> streamlit run fileName.py
import streamlit as st
import pickle
import requests

def fetch_poster(title):
    request = requests.get('https://www.omdbapi.com/?t={}&apikey=387bc996'.format(title))
    data = request.json()
    return data['Poster']

def recommend(selected_movie_name):
    movie_index = movies_list[movies_list['title']==selected_movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    poster = []

    l=[]
    for i in movie_list:
        l.append(movies_list.iloc[i[0]].title)
        poster.append(fetch_poster(movies_list.iloc[i[0]].title))
    return l,poster


with open('movies.pkl','rb') as file:
    movies_list = pickle.load(file)
  

similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
"Based on your choice, lets see what other movies you might like!",
(movies_list['title']),
)

if st.button('Recommend'):
    name,poster= recommend(selected_movie_name)
    c1,c2,c3,c4,c5 = st.columns(5)
    with c1:
        #st.write(name[0]) 
        st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
        st.image(poster[0],caption=name[0])
    with c2:
        #st.write(name[1]) 
        st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
        st.image(poster[1],caption=name[1])
    with c3:
        #st.write(name[2]) 
        st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
        st.image(poster[2],caption=name[2])
    with c4:
        #st.write(name[3]) 
        st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
        st.image(poster[3],caption=name[3])
    with c5:
        #st.write(name[4]) 
        st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
        st.image(poster[4],caption=name[4])


   