import numpy as np
import pandas as pd
def get_overall_statistics(data):
    cuisines = data['cuisine'].nunique()
    courses = data['course'].nunique()
    diets = data['diet'].nunique()

    return cuisines, courses, diets

def data_over_time(df, col):
    df['cuisine'] = df['cuisine'].fillna('')  # Replace missing values with empty strings
    filtered_df = df[df['cuisine'].str.contains("Indian", case=False)]
    cuisine_over_time = filtered_df.groupby(['cuisine', col]).size().reset_index(name='count')
    return cuisine_over_time

def get_cuisine_diet_data(df):
    cuisine_counts = df['cuisine'].value_counts().reset_index()
    cuisine_counts.columns = ['cuisine', 'Number of Cuisines']

    diet_counts = df['diet'].value_counts().reset_index()
    diet_counts.columns = ['Diet', 'Number of Diet Dishes']

    cuisine_diet_data = cuisine_counts.merge(diet_counts, left_on='cuisine', right_on='Diet', how='left')

    count_data = df.groupby(['cuisine', 'diet']).size().reset_index(name='count')

    return cuisine_diet_data, count_data