import streamlit as st



st.sidebar.write("Menú")

pg = st.navigation([st.Page("primera.py"), st.Page("segunda.py")])
st.sidebar.button(pg)
st.sidebar.write("Brissa Aracely Carrasco Iglesias 395007")
st.sidebar.write("Isadora Armendariz")
st.sidebar.write("Leonardo Eusebio Martinez")
st.sidebar.write("Audric Lorenzo Gómez Carrera 394911")
