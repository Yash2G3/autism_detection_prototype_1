import streamlit as st
import numpy as np
import pandas as pd
import joblib
st.set_page_config("This is page config",
                   page_icon='🧑‍⚕️',
                   layout="centered")

st.title("Lets get started with the diagnosis")
st.header("")
A1_Score = st.radio(
    "1.I often notice small rounds when others do not.",
    ("Yes", "No")
)
if A1_Score== "Yes":
    A1_Score = 1
else:
    A1_Score = 0

A2_Score = st.header("")
st.radio(
    "2.When I’m reading a story, I find it difficult to work out the characters’ intentions.",
    ("Yes", "No")
)
if A2_Score== "Yes":
    A2_Score = 1
else:
    A2_Score = 0
A3_Score = st.header("")
st.radio(
    "3.I find it easy to 'read between the lines' when someone is talking to me.",
    ("Yes", "No")
)
if A3_Score== "Yes":
    A3_Score = 1
else:
    A3_Score = 0
A4_Score = st.header("")
st.radio(
    "4.I usually concentrate more on the whole picture, rather than the small details.",
    ("Yes", "No")
)
if A4_Score== "Yes":
    A4_Score = 1
else:
    A4_Score = 0
A5_Score = st.header("")
st.radio(
    "5.I know how to tell if someone listening to me is getting bored.",
    ("Yes", "No")
)
if A5_Score== "Yes":
    A5_Score = 1
else:
    A5_Score = 0
A6_Score = st.header("")
st.radio(
    "6.I find it easy to do more than one thing at once.",
    ("Yes", "No")
)
if A6_Score== "Yes":
    A6_Score = 1
else:
    A6_Score = 0
A7_Score= st.header("")
st.radio(
    "7.I find it easy to work out what someone is thinking or feeling just by looking at their face.",
    ("Yes", "No")
)
if A7_Score== "Yes":
    A7_Score = 1
else:
    A7_Score = 0
A8_Score = st.header("")
st.radio(
    "8.If there is an interruption, I can switch back to what I was doing very quickly.",
    ("Yes", "No")
)
if A8_Score== "Yes":
    A8_Score = 1
else:
    A8_Score = 0
A9_Score = st.header("")
st.radio(
    "9.I like to collect information about categories of things.",
    ("Yes", "No")
)
if A9_Score== "Yes":
    A9_Score = 1
else:
    A9_Score = 0
A10_Score = st.header("")
st.radio(
    "10.I find it difficult to work out people’s intentions.",
    ("Yes", "No")
)
if A10_Score== "Yes":
    A10_Score = 1
else: A10_Score =0


st.button("Predict")






