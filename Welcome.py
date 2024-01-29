import streamlit as st
import pandas as pd
from sklearn.datasets import load_wine

wine = load_wine()

st.title("Wine Dataset :green[Analysis] :tea: :coffee: :chart: :bar_chart:")
st.markdown("Explore relationship between **ingredients** used in creation of 3 different types of wine (class_0, class_1 & class_2).")

st.write(wine.DESCR)