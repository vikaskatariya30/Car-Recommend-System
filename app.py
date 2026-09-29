import streamlit as st
import pandas as pd
import pickle


similarity = pickle.load(open('similarity.pkl', 'rb'))
car=pd.read_csv('car.csv')

def recommend(model):
    car_index=car[car['name']==model].index[0]
    distance=similarity[car_index]
    car_list=sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]
    car_names=[]
    for i in car_list:
        car_names.append(car.iloc[i[0]]['name'])
    return car_names

st.title('Car Recommendation System')
st.subheader('Find the best car for your needs!🏎️💨')

model=st.text_input('Enter car model or brand:', key='car_input')
if st.button('recommend'):
    recommended_cars = recommend(model)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(recommended_cars[0])
        print(car[car['name'] == recommended_cars[0]])
    with col2:
        st.write(recommended_cars[1])
        print(car[car['name'] == recommended_cars[1]])
    with col3:
        st.write(recommended_cars[2])
        print(car[car['name'] == recommended_cars[2]])
    with col4:
        st.write(recommended_cars[3])
        print(car[car['name'] == recommended_cars[3]])
    with col5:
        st.write(recommended_cars[4])
        print(car[car['name'] == recommended_cars[4]])
