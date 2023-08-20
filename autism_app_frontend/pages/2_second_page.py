import streamlit as st
import numpy as np
import pandas as pd
import pickle
import joblib
import sklearn

 

st.set_page_config("This is page config",
                   page_icon='🧑‍⚕️',
                   layout="centered")
st.title("Lets get you started")
st.header("First off please fill up some information asked below")

name = st.text_input("1.Please tell us your name")
st.header("")

age = st.slider("2.How old are you?", 0, 130, 25)
st.header("")

gender = st.selectbox(
    "3.Please mention your gender",
    ("f", "m"))


st.header("")

ethnicity = st.selectbox(
    "Please select your ethnicity",
    ['Middle Eastern' ,'Unkown' ,'White-European' ,'Asian' ,'Latino' ,'Others' ,'Black' ,'Pasifika' ,'South Asian' ,'Hispanic','Turkish']

)
st.header("")

contry_of_res = st.text_input("What is your main country of resdience in the last 15 years")
st.header("")

used_app_before = st.selectbox(
    'Have you used our app or similar application before?',
    ('Yes', 'No'))

relation = st.radio("Who is taking the test?",
               ("Patient themself","Patient's Parent", "Doctor","Relative","Other Relation") )
if relation == "Patient themself":
    relation = "Self"
elif relation == "Patient's Parent":
    relation = "Parent"
elif relation == "Doctor":
    relation = "Health care professional"

elif relation == "Relative":
    relation = "Relative"

elif relation == "Other Relation":
    relation = 'Others'

else:
    relation = "Unknown"

st.header("")
jaundice = st.selectbox(
    'Is the patient currently suffering or had a history of suffering from Jaundice?',
    ('Yes', 'No'))

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

A2_Score  = st.radio(
    "2.When I’m reading a story, I find it difficult to work out the characters’ intentions.",
    ("Yes", "No")
)
if A2_Score== "Yes":
    A2_Score = 1
else:
    A2_Score = 0
A3_Score = st.radio(
    "3.I find it easy to 'read between the lines' when someone is talking to me.",
    ("Yes", "No")
)
if A3_Score== "Yes":
    A3_Score = 1
else:
    A3_Score = 0
A4_Score =st.radio(
    "4.I usually concentrate more on the whole picture, rather than the small details.",
    ("Yes", "No")
)
if A4_Score== "Yes":
    A4_Score = 1
else:
    A4_Score = 0
A5_Score = st.radio(
    "5.I know how to tell if someone listening to me is getting bored.",
    ("Yes", "No")
)
if A5_Score== "Yes":
    A5_Score = 1
else:
    A5_Score = 0
A6_Score = st.radio(
    "6.I find it easy to do more than one thing at once.",
    ("Yes", "No")
)
if A6_Score== "Yes":
    A6_Score = 1
else:
    A6_Score = 0
A7_Score= st.radio(
    "7.I find it easy to work out what someone is thinking or feeling just by looking at their face.",
    ("Yes", "No")
)
if A7_Score== "Yes":
    A7_Score = 1
else:
    A7_Score = 0
A8_Score = st.radio(
    "8.If there is an interruption, I can switch back to what I was doing very quickly.",
    ("Yes", "No")
)
if A8_Score== "Yes":
    A8_Score = 1
else:
    A8_Score = 0
A9_Score = st.radio(
    "9.I like to collect information about categories of things.",
    ("Yes", "No")
)
if A9_Score== "Yes":
    A9_Score = 1
else:
    A9_Score = 0

A10_Score = st.radio(
    "10.I find it difficult to work out people’s intentions.",
    ("Yes", "No")
)
if A10_Score== "Yes":
    A10_Score = 1
else: A10_Score = 0

result = A1_Score + A2_Score + A3_Score + A4_Score + A5_Score + A6_Score + A7_Score + A8_Score + A9_Score + A10_Score
st.text(result)
col = ["A1_Score","A2_Score","A3_Score","A4_Score","A5_Score","A6_Score","A7_Score","A8_Score","A9_Score","A10_Score","age","gender","ethnicity", "jaundice","result", "contry_of_res", "relation"]

model = pickle.load(open('ada_ki.pkl','rb'))
def predict():
    prediction = model.predict(
    [A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, A6_Score, A7_Score, A8_Score, A9_Score, A10_Score, age, gender, ethnicity, jaundice, result, contry_of_res, relation]
)
    if prediction[0] == 1: 
        st.success('Patient Needs Further Diagnosis')
    else: 
        st.error('Patient does not needs further') 

trigger = st.button('Predict', on_click=predict)



