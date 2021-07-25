import streamlit as st

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

    st.dataframe(df[df.SK_ID_CURR.isin(list_client_selec)][list_colonne])