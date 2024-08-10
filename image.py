import streamlit as st

st.header(" Les jeux olympiques de Paris")


tab1, tab2, tab3 = st.tabs(["Medaille de Bronze", "Medaille d'or", "Medaille d'argent"])

with tab1:
    st.header("Medaille de Bronze")
    st.image("https://thumbs.dreamstime.com/z/m%C3%A9daille-de-bronze-de-jeux-olympiques-de-vancouver-2010-12865258.jpg", width=200)
with tab2:
    st.header("Medaille d'or")
    st.image("https://th.bing.com/th/id/OIP.43yyH9a4Sn8PrTowMxANSAAAAA?rs=1&pid=ImgDetMain", width=200)

with tab3:
    st.header("Medaille d'argent")
    st.image("https://th.bing.com/th/id/OIP.A9O6grvrDnSewJJfBRjFdgAAAA?rs=1&pid=ImgDetMain", width=200)
