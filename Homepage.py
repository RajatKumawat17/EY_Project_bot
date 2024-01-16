import pickle
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
from pathlib import Path


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="MediAPP", page_icon="🩺", layout="wide")


# --- USER AUTHENTICATION ---
names = ["Ayush", "Rajat"]
usernames = ["Ayush123", "Rajat2"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw1.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

# Create a dictionary for credentials
credentials = {
   "usernames": {
       usernames[0]: {
           "name": names[0],
           "password": hashed_passwords[0]
       },
       usernames[1]: {
           "name": names[1],
           "password": hashed_passwords[1]
       }
   }
}

# Pass the credentials dictionary to the Authenticate method
authenticator = stauth.Authenticate(credentials, "medapp", "abcdef", cookie_expiry_days=30)


name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    
    # ---- SIDEBAR ----
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    
    st.link_button("EMERGENCY 📞 💬", "\Emergency")
    st.link_button("CONSULT DOCTOR 📞 💬", "\Doctor")
    st.link_button("SELF EVALUATION 📞 💬", "\Evaluation")
    
    res = card(
        title="GEN-AI CHATBOT",
        text="click here to use the chatbot",
        image="https://st3.depositphotos.com/1071909/19574/i/450/depositphotos_195745476-stock-photo-artificial-intelligence-ai.jpg",
        url="/Chatbot",
        styles={
            "card": {
                "width": "100%", 
                "height": "300px"
            }
        }
    )