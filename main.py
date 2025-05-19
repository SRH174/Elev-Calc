import streamlit as st

def predict_elevator_output(H, L):
    if H <= 37:
        if L <= 3195:
            return 17390
        elif L <= 4941.5:
            return 47558
        else:
            return 36221
    else:
        if L <= 4128:
            return 59174
        else:
            return 64747

st.title("🚀 SRH Elevator Parameter Code Calculator")

st.write("Enter the elevator parameters below to get the predicted output.")

H = st.number_input("H (Start Delay)", min_value=0, max_value=10000, step=1)
L = st.number_input("L (Load or Travel Length)", min_value=0, max_value=10000, step=1)

if st.button("Predict"):
    result = predict_elevator_output(H, L)
    st.success(f"🔢 Predicted Answer: {result}")
