import streamlit as st

st.title("📊 Rendiconto Parrocchia Santa Maria Maggiore")
st.write("Benvenuto! L'app sta funzionando correttamente.")

# Un semplice test interattivo
nome = st.text_input("Come ti chiami?")
if nome:
    st.success(f"Ciao {nome}! Pronto per iniziare a gestire i dati?")
