import streamlit as st
import joblib
import numpy as np

model = joblib.load("../models/house_price_model_10features.pkl")

st.set_page_config(page_title="House Price Prediction")

st.title("🏠 House Price Prediction")
st.write("Enter the house details below.")


overall_qual = st.number_input("Overall Quality", min_value=1, max_value=10, value=5)

gr_liv_area = st.number_input("Ground Living Area (sq ft)", min_value=300, value=1500)

garage_cars = st.number_input("Garage Cars", min_value=0, max_value=5, value=2)

garage_area = st.number_input("Garage Area (sq ft)", min_value=0, value=500)

total_bsmt_sf = st.number_input("Total Basement Area", min_value=0, value=1000)

year_built = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000)

full_bath = st.number_input("Full Bathrooms", min_value=0, max_value=5, value=2)

totrms = st.number_input("Total Rooms Above Ground", min_value=1, max_value=20, value=7)

first_flr_sf = st.number_input("1st Floor Area", min_value=300, value=1200)

overall_cond = st.number_input("Overall Condition", min_value=1, max_value=10, value=5)

if st.button("Predict House Price"):

    input_data = np.array([[
        overall_qual,
        gr_liv_area,
        garage_cars,
        garage_area,
        total_bsmt_sf,
        year_built,
        full_bath,
        totrms,
        first_flr_sf,
        overall_cond
    ]])

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")