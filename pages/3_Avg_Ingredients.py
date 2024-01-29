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

st.header("Bar Chart: Average Ingredients per Wine Type.")

bar_multiselect = st.multiselect(label="Ingredients", options=ingredients, default=["alcohol", "malic_acid", "ash"])

st.bar_chart(avg_wine_df, x="WineType", y=bar_multiselect, height=500, use_container_width=True)
