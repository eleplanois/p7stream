import streamlit as st
import client
import home

st.set_page_config(layout="wide", page_title='dashboard P7')

st.sidebar.write('# Pret a Depenser')
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:',
                           ['Home', 'Information Client', 'Analyse Initiale', 'Analyse Exploratoire'])

if options == 'Home':
    home.home()
elif options == 'Information Client':
    client.client()
