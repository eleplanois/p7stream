import streamlit as st
import client
import home
import analyse_initiale
import analyse_exploratoire
import pandas as pd

st.set_page_config(layout="wide", page_title='dashboard P7')

@st.cache
def load_data():
    df = pd.read_csv('df_feats_sample.csv', index_col=0)
    df.drop(columns='TARGET', inplace=True)
    index1500 = [i for i in range(0,1500)]
    df.index = index1500
    return df

df = load_data()

st.sidebar.write('# Pret a Depenser')
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:',
                           ['Home', 'Information Client', 'Analyse Initiale', 'Analyse Exploratoire'])

if options == 'Home':
    home.home()
elif options == 'Information Client':
    client.client(df)
elif options == 'Analyse Initiale':
    analyse_initiale.run()
elif options == 'Analyse Exploratoire':
    analyse_exploratoire.run(df)
