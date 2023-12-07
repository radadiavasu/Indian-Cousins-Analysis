import streamlit as st
import pandas as pd
import helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df = pd.read_csv('cuisine_updated.csv')

st.sidebar.title("Cuisines Analysis")
analysis_options = ['Overall Analysis']

user_menu = st.sidebar.selectbox('Select Analysis Option:', analysis_options)

if user_menu == 'Overall Analysis':
    cuisines = df['cuisine'].nunique()
    courses = df['course'].nunique()
    diets = df['diet'].nunique()
    
    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("cuisines")
        st.title(cuisines)
    with col2:
        st.header("courses")
        st.title(courses)
    with col3:
        st.header("diets")
        st.title(diets)
        
    cuisine_over_time = helper.data_over_time(df, 'diet')
    fig = px.bar(cuisine_over_time, x="cuisine", y="count", color="cuisine", labels={"count": "Number of Cuisines"})
    fig.update_layout(showlegend=False, xaxis_title="Cuisine", yaxis_title="Number of Cuisines")
    st.title("Cuisines")
    st.plotly_chart(fig)
    
    cuisine_data, count_data = helper.get_cuisine_diet_data(df)

    fig = px.bar(count_data, x="cuisine", y="count", color="diet", title="Cuisines with Their Diets")
    fig.update_layout(xaxis_title="Cuisine", yaxis_title="Number of Cuisines")
    fig.update_layout(autosize=True, width=900, height=600)
    st.plotly_chart(fig)

    st.title("Cuisines Analysis")
    st.subheader("Cuisine Summary")
    st.dataframe(cuisine_data)

    st.subheader("Diet Types")
    diet_counts = df['diet'].value_counts().reset_index()
    diet_counts.columns = ['Diet', 'Number of Dishes']
    diet_distribution = diet_counts.iloc[1:9]  # Filtered diet distribution data
    st.dataframe(diet_distribution)

    # Pie chart
    st.subheader("Diet Distribution")
    diet_subdata = diet_distribution['Number of Dishes']
    diet_sublabels = diet_distribution['Diet']

    pie_fig = px.pie(names=diet_sublabels, values=diet_subdata, title="Diet Distribution")
    st.plotly_chart(pie_fig)