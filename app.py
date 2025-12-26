import streamlit as st
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "227e8011f24774c040d2c04674a75cb3"

st.set_page_config(page_title="Weather", page_icon="🌤️")
st.title("WEATHER")
with st.form("Weather"): 
    city = st.text_input("City:")
    submitted = st.form_submit_button("Confirm")
if submitted:
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    try:
        data = requests.get(url).json()
        if str(data["cod"]) == "200":
            st.header(data["name"])
            st.write(f"Main: {data['weather'][0]['main']}")
            st.write(f"Description: {data['weather'][0]['description']}")
            st.write(f"Temperature: {data['main']['temp']}°C")
            st.write(f"Humidity: {data['main']['humidity']}%")
            st.write(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            st.error(data["message"])
    except requests.exceptions.RequestException as e:
        st.error(str(e))