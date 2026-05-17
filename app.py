import streamlit as st
import pandas as pd
import joblib


# Load uploaded files from Hugging Face
data = pd.read_pickle("data.pkl")

preprocessor = joblib.load("preprocessor.joblib")

kmeans = joblib.load("kmeans_model.joblib")


def recommend(product_name):

    # Search in Title + Category + Sub-Category
    search_results = data[
        data['Title'].str.contains(product_name, case=False, na=False) |
        data['Category'].str.contains(product_name, case=False, na=False) |
        data['Sub-Category'].str.contains(product_name, case=False, na=False)
    ]

    if search_results.empty:
        return "No products found."

    result = ""

    # Only show actual matching products
    for idx in search_results.index[:5]:

        result += f"""
Product: {data.iloc[idx]['Title']}
Category: {data.iloc[idx]['Category']}
Sub Category: {data.iloc[idx]['Sub-Category']}

"""

    return result


st.title("AI Ecommerce Recommendation System")

user_input = st.text_input(
    "Enter Product Name"
)

if st.button("Recommend"):

    output = recommend(user_input)

    st.text(output)