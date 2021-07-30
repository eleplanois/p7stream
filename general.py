import pandas as pd
import shap
import requests
import plotly.graph_objects as go
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def general(df, df_appli):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.subheader("General Information")
    note_pie = df_appli['TARGET'].value_counts()
    st.text("payment Default")
    fig = go.Figure(data=[go.Pie(labels=['payment OK', 'payment default'],
                                 values=note_pie,
                                 pull=[0, 0.3])])
    st.plotly_chart(fig)

    age_data = df_appli[['TARGET', 'DAYS_BIRTH']]
    age_data['YEARS_BIRTH'] = age_data['DAYS_BIRTH'] / 365
    age_data['YEARS_BINNED'] = pd.cut(age_data['YEARS_BIRTH'], bins = np.linspace(20, 70, num = 11))
#    age_groups  = age_data.groupby('YEARS_BINNED').mean()
    st.write(age_data)

    st.subheader("SHAPLEY values interpretation")
    st.text("""
    - Red value means high value for features
    - High value for SHAP means more payment default risk""")
    st.image('summary_plot_lgbm_feats.png', width=600)
