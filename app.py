import streamlit as st
import joblib

# Page settings
st.set_page_config(
    page_title="Weather Prediction System",
    page_icon="🌦️",
    layout="wide"
)

# Load model
try:
    model = joblib.load("model.pkl")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Title
st.title("🌦️ Weather Prediction System")
st.markdown("Predict weather conditions using Machine Learning")

# Sidebar inputs
st.sidebar.header("Enter Weather Details")

temp = st.sidebar.number_input(
    "Temperature (°C)",
    min_value=0.0,
    max_value=50.0,
    value=25.0
)

hum = st.sidebar.number_input(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

wind = st.sidebar.number_input(
    "Wind Speed (km/h)",
    min_value=0.0,
    max_value=100.0,
    value=10.0
)

press = st.sidebar.number_input(
    "Pressure (hPa)",
    min_value=900.0,
    max_value=1100.0,
    value=1013.0
)

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Input Summary")

    st.write(f"**Temperature:** {temp} °C")
    st.write(f"**Humidity:** {hum} %")
    st.write(f"**Wind Speed:** {wind} km/h")
    st.write(f"**Pressure:** {press} hPa")

with col2:
    st.subheader("🔮 Prediction")

    if st.button("Predict Weather"):

        try:
            prediction = model.predict([[temp, hum, wind, press]])

            st.success(
                f"🌤️ Predicted Weather: {prediction[0]}"
            )

        except Exception as e:
            st.error(f"Prediction Error: {e}")