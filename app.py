import streamlit as st
import pickle

with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

st.title('Restaurant Rating')