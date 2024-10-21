#streamlit run 4-streamlit.py
# git add 
# git commit -m ''
#git push -u origin main --> auto updates after pushing to github
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
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrengheit is', myslider * (9/5) + 32)