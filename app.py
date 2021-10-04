import streamlit as st
import numpy as np 
from model import predict_duration





st.set_page_config(page_title="Higgs Boson",layout="wide")
st.title("Higgs Boson Prediction")

with st.form('prediction form'):

    st.header("Enter the Deciding Factors:")


    # DER_mass_MMC = st.slider("DER_mass_MMC",0,1, value=0, format="%d")
    DER_mass_MMC = st.slider("DER_mass_MMC",0.0,1.0,key=1)
   
    DER_mass_transverse_met_lep = st.slider("DER_mass_transverse_met_lep ",0.0,1.0,key=2)
    DER_mass_vis = st.slider("DER_mass_vis",0.0,1.0,key=3)
    DER_pt_h= st.slider("DER_pt_h ",0.0,1.0,key=4)
    DER_deltaeta_jet_jet = st.slider("DER_deltaeta_jet_jet ",0.0,1.0,key=5)
    DER_deltar_tau_lep = st.slider("DER_deltar_tau_lep ", 0.0,1.0,key=6)
    DER_pt_tot = st.slider("DER_pt_tot ",0.0,1.0,key=7)
    DER_sum_pt = st.slider("DER_sum_pt ",0.0,1.0,key=8)
    DER_pt_ratio_lep_tau = st.slider("DER_pt_ratio_lep_tau ",0.0,1.0,key=9)
    DER_met_phi_centrality = st.slider("DER_met_phi_centrality ",0.0,1.0,key=10)
    PRI_tau_pt= st.slider("PRI_tau_pt ",0.0,1.0,key=11)
    PRI_lep_pt = st.slider("PRI_lep_pt ",0.0,1.0,key=12)
    PRI_met_sumet = st.slider("PRI_met_sumet ",0.0,1.0,key=13)
    PRI_jet_num = st.slider("PRI_jet_num ",0.0,1.0,key=14)
    PRI_jet_leading_pt = st.slider("PRI_jet_leading_pt ",0.0,1.0,key=15)
    Weight = st.slider("Weight",0.0,1.0,key=16)
    



    submit_val = st.form_submit_button("Predict")

if submit_val:

    attribute = np.array([DER_mass_MMC, DER_mass_transverse_met_lep, DER_mass_vis, DER_pt_h, DER_deltaeta_jet_jet, DER_deltar_tau_lep, DER_pt_tot, DER_sum_pt, DER_pt_ratio_lep_tau, DER_met_phi_centrality, PRI_tau_pt, PRI_lep_pt , PRI_met_sumet, PRI_jet_num, PRI_jet_leading_pt, Weight]).reshape(1,-1)
    st.header('  s for signal process which produces Higgs bosons and b for a background process which does not')

    if attribute.shape == (1,16):
        
        print("Attribute Valid")

        value = predict_duration(attributes = attribute)
        st.header("Here are the Results")
        st.success(f"The  prediction is {value}")
    else:
        st.header("Something went wrong")