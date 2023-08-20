import streamlit as st

st.set_page_config("This is page config",
                   page_icon='🧑‍⚕️',
                   layout="centered")
st.header("""Welcome to our ML based autism diagnosis applicaiton""") 
st.header("")
st.header("Please head on to the second page given on left for further process")

st.sidebar.success("Choose pages from here")

if (["A1_Score","A2_Score","A3_Score","A4_Score","A5_Score","A6_Score","A7_Score","A8_Score","A9_Score","A10_Score","name","age","gender","ethnicity", "jaundice", "contry_of_res", "used_app_before", "relation"]) not in st.session_state:
    st.session_state["A1_Score","A2_Score",	"A3_Score",	"A4_Score",	"A5_Score",	"A6_Score",	"A7_Score",	"A8_Score",	"A9_Score",	"A10_Score","name","age","gender","ethnicity", "jaundice", "contry_of_res", "used_app_before", "relation"] = ""


