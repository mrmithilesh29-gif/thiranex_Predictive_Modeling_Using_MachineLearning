import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
with open("flight_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("✈️ Flight Price Category Prediction")
st.write("Enter flight details to predict whether the price is Low, Medium, or High.")

duration = st.number_input("Duration (minutes)", min_value=30, max_value=1000, step=10)
total_stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4])
date = st.number_input("Date of Journey", min_value=1, max_value=31)
month = st.selectbox("Month of Journey", list(range(1,13)))
arrival_hour = st.number_input("Arrival Hour", min_value=0, max_value=23)
arrival_min = st.number_input("Arrival Minute", min_value=0, max_value=59)
dep_hour = st.number_input("Departure Hour", min_value=0, max_value=23)
dep_min = st.number_input("Departure Minute", min_value=0, max_value=59)

airlines = [
    'Air Asia','Air India','GoAir','IndiGo','Jet Airways',
    'Jet Airways Business','Multiple carriers',
    'Multiple carriers Premium economy','SpiceJet','Trujet',
    'Vistara','Vistara Premium economy'
]
airline = st.selectbox("Airline", airlines)

sources = ['Banglore','Chennai','Delhi','Kolkata','Mumbai']
source = st.selectbox("Source", sources)

destinations = ['Banglore','Cochin','Delhi','Hyderabad','Kolkata','New Delhi']
destination = st.selectbox("Destination", destinations)

input_data = {
    'Duration': duration,
    'Total_Stops': total_stops,
    'Date': date,
    'Month': month,
    'ArrivalTime_Hours': arrival_hour,
    'ArrivalTime_Min': arrival_min,
    'DepTime_Hours': dep_hour,
    'DepTime_Min': dep_min,
}


for a in airlines:
    input_data[f'Airline_{a}'] = 1 if airline == a else 0
for s in sources:
    input_data[f'Source_{s}'] = 1 if source == s else 0
for d in destinations:
    input_data[f'Destination_{d}'] = 1 if destination == d else 0

input_df = pd.DataFrame([input_data])

if st.button("Predict Price Category"):
    prediction = model.predict(input_df)[0]
    categories = {0: "Low", 1: "Medium", 2: "High"}
    st.success(f"Predicted Price Category: {categories[prediction]}")
