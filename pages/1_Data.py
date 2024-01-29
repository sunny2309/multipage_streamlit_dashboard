import streamlit as st
from sklearn.datasets import load_wine
import pandas as pd

@st.cache_data
def load_data(): ## Dataset
    wine = load_wine()
    wine_df = pd.DataFrame(wine.data, columns=wine.feature_names) 
    wine_df["WineType"] = [wine.target_names[t] for t in wine.target]
    return wine_df

wine_df = load_data()
ingredients = wine_df.drop(columns=["WineType"]).columns

avg_wine_df = wine_df.groupby("WineType").mean().reset_index() ## Avg Ingredients.

st.header("Wine Dataset")
st.write(wine_df)
st.write(avg_wine_df)