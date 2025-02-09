import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import os

# Set page configuration
st.set_page_config(
    page_title="Prediction of Disease Outbreaks",
    layout="wide",
    page_icon="🏥"
)

working_dir = os.path.dirname(os.path.relpath(__file__))

#loading The saved models

Diabetes_Model = pickle.load(open(r"SavedModels\Diabetes_Model.sav",'rb'))
HeartDisease_Model = pickle.load(open(r"SavedModels\HeartDisease_Model.sav",'rb'))
ParkinsonDisease_Model = pickle.load(open(r"SavedModels\ParkinsonDisease_Model.sav",'rb'))

#Sidebar Navigation

with st.sidebar:
    selected = option_menu('Prediction Of Disease Outbreaks Syatem',
                           [
                               'Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'
                           ],
                           menu_icon='hospital-fill',
                           icons=['activity','heart','person'],
                           default_index=0
                           )

#Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    #page title
    st.title('Diabetes Prediction Using Machine Learning')

    #Getting the input from the user
    col1, col2, col3 =st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number Of Pregnancies")

    with col2:
        Glucose =st.text_input("Glucose Level")

    with col3:
        BloddPressure = st.text_input("Blood Pressure Value")
    
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")

    with col2:
        Insulin = st.text_input("Insulin Level")

    with col3:
        BMI = st.text_input("BMI Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")

    with col2:
        Age = st.text_input("Age of the person")
    diab_diagnosis =''


#RETURN RESULTS AND AlERT THE USER TO ENTER ALL THE REQUIRED DATA
    if st.button('Get Diabetes Test Result'):
        user_input=[Pregnancies, Glucose, BloddPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        if '' in user_input:
            st.warning("Please enter all the required data")
        else:
            user_input = [float(x) for x in user_input]
            diab_diagnosis = Diabetes_Model.predict([user_input])
            
            if diab_diagnosis[0] == 1:
                diab_diagnosis = "The Person is Diabetic"
            else:
                diab_diagnosis = "The Person is not Diabetic"
            
            st.success(diab_diagnosis)
        
    
    
#HEART DISEASE PREDICTION
if selected =="Heart Disease Prediction":

    st.title("Heart Disease Prediction Using Machine Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input("Sex (Male=1 Female =0)")
    with col3:
        cp = st.text_input("Chest Pain Types")
    with col1:
        trestbps = st.text_input("Resting Blodd Pressure")
    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl")
    with col3:
        fbs = st.text_input("Fasting Blodd Sugar > 120 mg/dl")
    with col1:
        restecg= st.text_input("Resting Electrocardiographic Results")
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")
    with col3:
        exang = st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak = st.text_input("ST Depression Induced by Exercise")
    with col2:
        slope = st.text_input("Slope of the peak Exercise ST segment")
    with col3:
        ca = st.text_input("Major vessels colored by flourosopy")
    with col1:
        thal = st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
    
    heart_diagnosis=""


#RETURN RESULTS AND AlERT THE USER TO ENTER ALL THE REQUIRED DATA

    if st.button("Get Heart Disease Test Result"):
        user_input=[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        if '' in user_input:
            st.warning("Please enter all the required data")
        else:
            user_input = [float(x) for x in user_input]
            heart_prediction = HeartDisease_Model.predict([user_input])
            
            if heart_prediction[0] == 1:
                heart_diagnosis = "The Person is having Heart Disease"
            else:
                heart_diagnosis = "The person does not have any heart disease"
            
            st.success(heart_diagnosis)
        
    

# PARKINSON'S PREDECTION PAGE
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction Using Machine Learning")
    col1 , col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo = st.text_input("MDVP: Flo(Hz)")
    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col1:
        RAP = st.text_input("MDVP:RAP")
    with col2:
        PPQ  = st.text_input("MDVP:PPQ")
    with col3:
        DDP = st.text_input("Jitter:DDP")
    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")
    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col1:
        APQ3 = st.text_input("Shimmer:APQ3")
    with col2:
        APQ5 = st.text_input("Shimmer:APQ5")
    with col3:
        APQ =st.text_input("MDVP:APQ")
    with col4:
        DDA  = st.text_input("Shimmer:DDA")
    with col5:
        NHR =st.text_input("NHR")
    with col1:
        HNR  = st.text_input("HNR")
    with col2:
        RDPE = st.text_input("RDPE")
    with col3:
        DFA = st.text_input("DFA")
    with col4:
        spread1 = st.text_input("spread1")
    with col5:
        spread2 = st.text_input("spread2")
    with col1:
        D2 = st.text_input("D2")
    with col2:
        PPE = st.text_input("PPE")
    
    parkinsons_diagnosis=""


#RETURN RESULTS AND AlERT THE USER TO ENTER ALL THE REQUIRED DATA

    if st.button("Get Parkinson's Test Result"):
        user_input=[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RDPE, DFA, spread1, spread2, D2, PPE] # type: ignore

        if '' in user_input:
            st.warning("Please enter all the required data")
        else:
            user_input = [float(x) for x in user_input]
            parkinsons_predictions = ParkinsonDisease_Model.predict([user_input])
            
            if parkinsons_predictions[0] == 1:
                parkinsons_diagnosis = "The person has parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have parkinson's disease"
            
            st.success(parkinsons_diagnosis)

    


    

