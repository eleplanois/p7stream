import streamlit as st
import plotly.graph_objs as go

def run(df):
    st.write("""
    # Pret a depenser
    
    ## ANALYSE EXPLORATOIRE
    """)
    list_client_id = sorted(list(df.SK_ID_CURR))
    list_client_selec = st.multiselect("selection clients", list_client_id)

    colonne = list(df.columns)
    colonne = sorted(colonne)
    list_colonne =  st.multiselect("selection variables", colonne,
                                   default=['SK_ID_CURR','EXT_SOURCE_1','EXT_SOURCE_2','EXT_SOURCE_3','INSTAL_DPD_MEAN',
                                            'AMT_CREDIT', 'PAYMENT_RATE','CODE_GENDER','DAYS_BIRTH',
                                            'AMT_ANNUITY'])

    df_isin = df[df.SK_ID_CURR.isin(list_client_selec)]
    df_notin = df[~df.SK_ID_CURR.isin(list_client_selec)]

    st.dataframe(df_isin[list_colonne])

    graph_colonne_X = st.selectbox(label='abscisse X : ', options=colonne, index=66)
    graph_colonne_Y = st.selectbox(label='ordonne Y : ', options=colonne, index=65)

    data1 = go.Scatter(
        x=df_isin[graph_colonne_X],
        y=df_isin[graph_colonne_Y],
        mode='markers',
        text=df_isin['SK_ID_CURR'])

    data2 = go.Scatter(
        x=df_notin[graph_colonne_X],
        y=df_notin[graph_colonne_Y],
        mode='markers',
        text=df_notin['SK_ID_CURR'])
    data = [data1, data2]

    layout = go.Layout(
        title=graph_colonne_Y + "suivant" + graph_colonne_X,
        xaxis=dict(title=graph_colonne_X),
        yaxis=dict(title=graph_colonne_Y),
        hovermode='closest'
    )
    plotly_fig = go.Figure(data=data, layout=layout)

    st.plotly_chart(plotly_fig, use_container_width=True)
