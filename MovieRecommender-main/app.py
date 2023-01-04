import streamlit as st
import pickle
import pandas as pd
Movies_Dict=pickle.load(open('movies_dict.pkl','rb'))
Movies_dataFrame=pd.DataFrame(Movies_Dict)
Similarity=pickle.load(open('Similarity.pkl','rb'))
def recommend(Movie_Name):
        movie_index = Movies_dataFrame[Movies_dataFrame['title'] == Movie_Name].index[0]
        distances = Similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

        Desired_Movies=[]
        for i in movie_list:
            Desired_Movies.append(Movies_dataFrame.iloc[i[0]].title)
        return Desired_Movies
st.title('Movie Recommender')
Selected_Movie = st.selectbox( 'Enter Your Choice',Movies_dataFrame['title'].values)
if st.button('Recommend Me'):
   Recommendations= recommend(Selected_Movie)
   for i in Recommendations:
       st.write(i)