import streamlit as st
import client
import client_dev
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
    df_features = pd.read_csv('features174 meanings.csv', sep=';', header=None)
    df_features.columns = ['TAG_FEAT', 'Meaning']
    return df, df_features

df, df_features = load_data()

st.sidebar.write('# Pret a Depenser')
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:',
                           ['Home', 'Information Client', 'Analyse Initiale', 'Analyse Exploratoire'])

if options == 'Home':
    home.home()
elif options == 'Information Client':
#    client_dev.client(df, df_features)
    client.client(df, df_features)
elif options == 'Analyse Initiale':
    analyse_initiale.run()
elif options == 'Analyse Exploratoire':
    analyse_exploratoire.run(df)
