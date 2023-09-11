import streamlit as st
import yaml
from yaml.loader import SafeLoader

with open('db.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

st.title('test')
