import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

try:
    # Define the breakfast menu
    st.header('Breakfast Menu')
    st.text('Omega 3 & Blueberry Oatmeal')
    st.text('Kale, Spinach & Rocket Smoothie')
    st.text('Hard-Boiled Free-Range Egg')

    # Load the fruit macros data from an external URL and display it in a dataframe
    st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
    my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt",header=None)
    st.dataframe(my_fruit_list)

    # Get information about a specific fruit from the Fruityvice API
    st.header("Fruityvice Fruit Advice!")
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
    st.text(fruityvice_response.json())

    # Normalize the JSON response and display it in a dataframe
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    st.dataframe(fruityvice_normalized)

    # Allow the user to select fruits for their smoothie
    fruits_selected = st.multiselect("Pick some fruits", my_fruit_list.index.tolist(), ['Peach', 'apple'])
    fruits_to_show = my_fruit_list.loc[fruits_selected]

    # Allow the user to enter a fruit and display the input on the page
    fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
    st.write('The user entered ', fruit_choice)

    # Let's put a pick list here so they can pick the fruit they want to include 
    st.multiselect("Pick some fruits:", list(my_fruit_list.index))

    # Establish a connection to Snowflake and execute a SQL query to fetch data from a table
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
    my_data_row = my_cur.fetchone()
    st.text("Hello from Snowflake:")
    st.text(my_data_row)
    my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
    my_data_row = my_cur.fetchall()
    st.header("Loaded data from my_fruit_list:")
    st.dataframe(my_data_row)

    fruit_choice_2 = st.text_input('What is your second fruit choice?', 'Apple')
    st.write('The user entered', fruit_choice_2)

    # Construct the SQL INSERT statement and execute it
    my_cur.execute(f"INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('{fruit_choice_2}')")

except Exception as e:
    st.error(f"An error occurred: {e}")
