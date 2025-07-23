from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
import  google.generativeai as genai 

load_dotenv()

# Set the Google API key
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# Create the front end of the application here.....
st.header("👩🏻‍⚕️Healthcare :blue[Advisor]",divider=True)
user_input = st.text_input("Hi I am your medical expert. Ask me infromation about health, disease and fitness only")
st.subheader("Disclaimer:")
st.write("1.This is an AI Advisor and should not be considered as medical advice")
st.write("2. Please consult a doctor before taking any action")


st.sidebar.header("BMI Calculator ﮩـﮩﮩ٨ـ🫀ﮩ٨ـﮩﮩ٨ـ")
weight = st.sidebar.number_input("Enter your weight (kgs):", value=70)
height = st.sidebar.number_input("Enter your height (cms):", value = 170)
st.sidebar.markdown("The BMI is:")

if height >0 :
    bmi = weight/((height/100)**2)
    st.sidebar.write("Your BMI is:", round(bmi,2))
    if bmi <18.5 :
        st.sidebar.write("You are underweight...Please Eat")
    elif 18.5 <= bmi <25:
        st.sidebar.write("You have normal weight.")
    elif 25 <= bmi <30:
        st.sidebar.write ("You are Overweight...Stop Eating")
    else:
        st.sidebar.write("You are Obese...Sirf Paani pii")


def guide_me_on(user_input):
    model = genai.GenerativeModel("gemini-2.5-pro")
    if user_input!="":
        prompt = f''' Act as a Dietician, Health coach and Expert and address the queries, questions, apprehensions 
        related to health,fitness, diseases and things associated with empathy towards the user. Any query or
        question that is not related to health should pass the following message - "I am a Healthcare Expert and 
        I can answer questions related to Health, Fitness and Diet only."
        If someone asks about medicine for any ailment, just pass the message - "I am an AI model and cannot 
        answer questions related to diagnosis and medicines. Please reach out to your doctor" '''
        response = model.generate_content(prompt + user_input)
        return(response.text)
    else:
        return(st.write("Please write the Prompt"))
    
# submit button
submit = st.button("Submit")
if submit:
    response = guide_me_on(user_input)
    st.subheader(":blue[response]")
    st.write(response)
