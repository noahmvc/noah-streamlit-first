#streamlit run 4-streamlit.py
import streamlit as st
import pandas

data = {
    'Series_1': [1,3,6,7,10],
    'Series_2' : [10,30,40,50,70]
}

df = pandas.DataFrame(data)

st.title('My first Streamlit app')
st.subheader('Introducting Streamlit, by Noah')
st.write(f'''Hello guys, today I will be showcasing my first Streamlit web app
         
         Hope you enjoy!''')

st.write(df)