import streamlit as st
from openai import OpenAI

st.title("EVALUATION")
with st.form(key='my_form'):
    patient_name = st.text_input('Name' , placeholder="Enter your name")
    weight = st.text_input('Weight' , placeholder="Enter weight")
    gender = st.text_input('Gender' , placeholder="Enter gender")

    st.subheader("Symptoms")
    Symptoms = st.text_input('Enter your symptoms' , placeholder="Describe your symptoms")
    travel = st.selectbox('Have you travelled to any specific location?', ['choose the option','yes', 'no'], key=1)
    medical_conditions = st.selectbox('Do you have any medical conditons?', ['choose the option','yes', 'no'], key=2)
    past_surgeries = st.selectbox('Did you had any surgeries in the past', ['choose the option','yes', 'no'], key=3)
    allergies = st.selectbox('Do you have any allergies?', ['choose the option','yes', 'no'], key=4)
    pain_meter =st.slider(label='On a scale of 1-10 how would you rate the severity of symptoms', min_value=0, max_value=10, key=5)

    submit = st.form_submit_button(label='Submit')
    
