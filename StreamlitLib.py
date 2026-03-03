import streamlit as st
import LangchainHelper

st.title("Missile's and their corresponding Origins & Strength")
missile= st.sidebar.selectbox("Pick a Missile", ("Shaheen 1-A", "RS-28 Sarmat", "Hwasong-17", "M51", "Trident II D5"))

if missile:
    response = LangchainHelper.generate_missileinfo(missile)

    st.subheader("Country of Origin")
    st.write(response["origin"])

    st.subheader("Strength")
    st.write(response["strength"])