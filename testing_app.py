import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import time

# Load the dataset from the CSV file
df = pd.read_csv('cuisine_updated.csv')

# Display a sidebar with a selectbox to choose an image
st.title("Indian Cuisines")
selected_file = st.file_uploader("Upload an image")

if st.button("Generate"):
    if selected_file is not None:
        # Read the selected image file
        image = Image.open(selected_file)

        # Display the selected image
        st.image(image, caption='Selected Image')

        for index, row in df.iterrows():
            response = requests.get(row['image_url'])
            dataset_image = Image.open(BytesIO(response.content))

            if image == dataset_image:
                            recipe_name = row['name']
                            recipe_description = row['description']
                            recipe_cuisine = row['cuisine']
                            recipe_course = row['course']
                            recipe_diet = row['diet']
                            recipe_preparation_time = row['prep_time']
                            recipe_ingredients = row['ingredients']
                            recipe_instructions = row['instructions']
                            recipe_image_available = row['image_available']
                            
                            # Extract other recipe details accordingly

                            # Display the selected recipe details
                            st.write("# Recipe Details")
                            st.write(f"**Name:** {recipe_name}")
                            st.write(f"**Description:** {recipe_description}")
                            st.write(f"**Cuisine:** {recipe_cuisine}")
                            st.write(f"**Course:** {recipe_course}")
                            st.write(f"**Diet:** {recipe_diet}")
                            st.write(f"**Preparation Time:** {recipe_preparation_time}")
                            st.write(f"**Ingredients:** {recipe_ingredients}")
                            st.write(f"**Instructions:** {recipe_instructions}")
                            st.write(f"**Is Image Available:** {recipe_image_available}")
                            break
    else:
        st.write("Please select an image.")
        
        # for index, row in df.iterrows():
        #             response = None
        #             while response is None:
        #                 try:
        #                     response = requests.get(row['image_url'])
        #                 except requests.exceptions.RequestException as e:
        #                     print(f"Connection Error: {e}")
        #                     print("Retrying connection after 3 seconds...")
        #                     time.sleep(3)  # Wait for 3 seconds before retrying

        #             dataset_image = Image.open(BytesIO(response.content))
        # Compare the uploaded image with the image URLs in the dataset