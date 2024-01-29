import streamlit as st
from sklearn.datasets import load_wine
import pandas as pd
import pandas_bokeh

@st.cache_data
def load_data(): ## Dataset
    wine = load_wine()
    wine_df = pd.DataFrame(wine.data, columns=wine.feature_names) 
    wine_df["WineType"] = [wine.target_names[t] for t in wine.target]
    return wine_df

wine_df = load_data()
ingredients = wine_df.drop(columns=["WineType"]).columns

st.markdown("### Scatter Chart: Explore Relationship between Ingredients.")

col1, col2 = st.columns(2)
with col1:
    x_axis = st.selectbox(label="X-Axis", options=ingredients, index=0)
with col2:
    y_axis = st.selectbox(label="Y-Axis", options=ingredients, index=1)

color_encode = st.checkbox(label="Color-Encode")

scatter_fig = wine_df.plot_bokeh.scatter(x=x_axis, y=y_axis, category="WineType" if color_encode else None,
                                         xlabel=x_axis.capitalize(), ylabel=y_axis.capitalize(),
                                         title="{} vs {}".format(x_axis.capitalize(), y_axis.capitalize()),
                                         fontsize_title=25, fontsize_label=12,
                                         figsize=(650,500), show_figure=False
                                         )

st.bokeh_chart(scatter_fig, use_container_width=True)

