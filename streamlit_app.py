import streamlit as st
import pandas as pd
import snowflake.connector
st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt",header=None)
st.dataframe(my_fruit_list)

st.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json())


# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)


fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)


# Let's put a pick list here so they can pick the fruit they want to include 
# st.multiselect("Pick some fruits:", list(my_fruit_list.index))

# # Display the table on the page.
# my_fruit_list = my_fruit_list.set_index(1)

# st.multiselect("Pick some fruits", my_fruit_list.index.tolist(), ['Peach', 'Pineapple'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]
