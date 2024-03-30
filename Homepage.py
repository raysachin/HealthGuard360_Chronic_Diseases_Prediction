import streamlit
import streamlit as st
import pickle
import pandas as pd
from PIL import Image


option = ['Select','Yes',
 'No']

# import the model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Proactive Health Management: A Chronic Disease Prediction and Personalization Web App")
col1, col2, col3, col4 = st.columns(4)    # here we take two column

with col1:
    fatigue = st.selectbox('Fatigue', option)    # here we give a dropdown

with col2:
    vomiting = st.selectbox('Vomiting', option)
with col3:
    high_fever = st.selectbox('Fever', option)
with col4:
    headache = st.selectbox('Headache', option)


col5, col6, col7, col8 = st.columns(4)    # here we take two column

with col5:
    yellowing_of_eyes = st.selectbox('Yellow of Eyes', option)
with col6:
    joint_pain = st.selectbox('Joint Pain', option)
with col7:
    itching = st.selectbox('Itiching', option)
with col8:
    skin_rash = st.selectbox('Skin Rash', option)

col9, col10, col11, col12 = st.columns(4)    # here we take two column

with col9:
    sweating = st.selectbox('Sweating', option)
with col10:
    dark_urine = st.selectbox('Dark Urine', option)
with col11:
    dizziness = st.selectbox('Dizziness', option)
with col12:
    stomach_pain = st.selectbox('Stomach Pain', option)

col13, col14, col15, col16 = st.columns(4)    # here we take two column

with col13:
    diarrhoea = st.selectbox('Diarrhoea', option)
with col14:
    weight_loss = st.selectbox('Weight Loss', option)
with col15:
    chest_pain = st.selectbox('Chest pain', option)
with col16:
    acidity = st.selectbox('Acidity', option)


if st.button('Predict Probability'):
    if fatigue == 'Yes':
        fatigue = 1
    if fatigue == 'No':
        fatigue = 0

    if 	vomiting == 'Yes':
        	vomiting = 1
    if 	vomiting == 'No':
        	vomiting = 0

    if headache == 'Yes':
        headache = 1
    if headache == 'No':
        headache = 0

    if high_fever == 'Yes':
        high_fever = 1
    if high_fever == 'No':
        high_fever = 0

    if skin_rash == 'Yes':
        skin_rash = 1
    if skin_rash == 'No':
        skin_rash = 0

    if itching == 'Yes':
        itching = 1
    if itching == 'No':
        itching = 0

    if joint_pain == 'Yes':
        joint_pain = 1
    if joint_pain == 'No':
        joint_pain = 0

    if yellowing_of_eyes == 'Yes':
        yellowing_of_eyes = 1
    if yellowing_of_eyes == 'No':
        yellowing_of_eyes = 0

    if chest_pain == 'Yes':
        chest_pain = 1
    if chest_pain == 'No':
        chest_pain = 0

    if sweating == 'Yes':
        sweating = 1
    if sweating == 'No':
        sweating = 0

    if stomach_pain == 'Yes':
        stomach_pain = 1
    if stomach_pain == 'No':
        stomach_pain = 0

    if dark_urine == 'Yes':
        dark_urine = 1
    if dark_urine == 'No':
        dark_urine = 0


    if diarrhoea == 'Yes':
        diarrhoea = 1
    if diarrhoea == 'No':
        diarrhoea = 0

    if acidity == 'Yes':
        acidity = 1
    if acidity == 'No':
        acidity = 0

    if dizziness == 'Yes':
        dizziness = 1
    if dizziness == 'No':
        dizziness = 0

    if weight_loss == 'Yes':
        weight_loss = 1
    if weight_loss == 'No':
        weight_loss = 0




    input_df = pd.DataFrame({'vomiting': [vomiting], 'fatigue': [fatigue], 'headache': [headache],
                             'high_fever': [high_fever], 'skin_rash': [skin_rash], 'itching': [itching],
                             'joint_pain': [joint_pain], 'yellowing_of_eyes': [yellowing_of_eyes], 'chest_pain': [chest_pain], 'sweating': [sweating], 'stomach_pain': [stomach_pain], 'dark_urine': [dark_urine], 'diarrhoea': [diarrhoea], 'acidity': [acidity], 'dizziness': [dizziness], 'weight_loss': [weight_loss]})
    result = model.predict(input_df)
    st.header("Diseases: " + str(result))