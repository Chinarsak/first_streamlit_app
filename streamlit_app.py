import streamlit as st
import pandas as pd

st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt",header=None)
st.dataframe(my_fruit_list)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
st.header("Fruityvice Fruit Advice!")

# Let's put a pick list here so they can pick the fruit they want to include 
# st.multiselect("Pick some fruits:", list(my_fruit_list.index))

# # Display the table on the page.
# my_fruit_list = my_fruit_list.set_index(1)

# st.multiselect("Pick some fruits", my_fruit_list.index.tolist(), ['Peach', 'Pineapple'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]
