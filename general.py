import pandas as pd
import shap
import requests
import plotly.graph_objects as go
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def general(df_analyse):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.subheader("General Information")
    note_pie = df_analyse['TARGET'].value_counts()
    st.text("payment Default")
    fig = go.Figure(data=[go.Pie(labels=['payment OK', 'payment default'],
                                 values=note_pie,
                                 pull=[0, 0.3])])
    st.plotly_chart(fig)

    colonne = df_analyse.columns
    colonne_num = df_analyse.select_dtypes(['float64','int64']).columns


    graph_colonne = st.selectbox(label='affichage : ', options=colonne_num, index=3)
    graph_groupby = st.selectbox(label='regroupement par : ', options=colonne, index=0)

    options_agg = st.radio('valeur affiche:', ['Max', 'Mean', 'Count'], index=1)

    df_agg = df_analyse.groupby(graph_groupby)
    if options_agg=='Max':
        aggr = df_agg[graph_colonne].max()
    elif options_agg=='Mean':
        aggr = df_agg[graph_colonne].mean()
    elif options_agg=='Count':
        aggr = df_agg[graph_colonne].count()

    layout = go.Layout(
        title=graph_colonne + " regroupe par  " + graph_groupby,
        xaxis=dict(title=graph_groupby),
        yaxis=dict(title=graph_colonne),
        hovermode='closest'
    )

    fig = go.Figure(go.Bar(x=aggr.index.values, y=aggr.values), layout=layout)
    st.plotly_chart(fig)

    st.subheader("SHAPLEY values interpretation")
    st.text("""
    - Red value means high value for features
    - High value for SHAP means more payment default risk""")
    st.image('summary_plot_lgbm.png', width=600)
