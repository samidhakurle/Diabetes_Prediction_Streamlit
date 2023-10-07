import streamlit as st  

import pickle  

import numpy as np  

 

h=open("diabetes_pred_model.pkl","rb")  

lr=pickle.load(h)  

 

pregnancies=st.number_input("number of Pregnancies:",0,20,2)  

glucose=st.number_input("Glucose:",0,800,80)  

bp=st.number_input("Blood Pressure:",0,200,110)  

skin_thickness=st.number_input("Skin Thickness:",0,100,15)  

insulin=st.number_input("Insulin:",30,200,30)  

bmi=st.number_input("BMI:",20,80,20)  

DBF=st.number_input("Diabetes Pedigree Function:",0.0,4.0,0.1)  

AGE=st.number_input("Age:",0,120,20)  

data=[np.array([pregnancies,glucose,bp,skin_thickness,insulin,bmi,DBF,AGE])] 

 
 

#=np.array(data).reshape(1,-1)  
prediction=lr.predict(data) 

 

if st.button("Diabetes Prediction"):  

    #st.write(str(prediction)) 
    if prediction==0:
        st.write("Diabetic")
    else:
        st.write("Non Diabetic")

 