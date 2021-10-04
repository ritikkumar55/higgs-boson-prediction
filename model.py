import joblib
import os
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier

curr_path = os.path.dirname(os.path.realpath(__file__))

feat_cols = ['DER_mass_MMC', 'DER_mass_transverse_met_lep', 'DER_mass_vis','DER_pt_h', 'DER_deltaeta_jet_jet', 'DER_deltar_tau_lep', 'DER_pt_tot','DER_sum_pt', 'DER_pt_ratio_lep_tau', 'DER_met_phi_centrality','PRI_tau_pt', 'PRI_lep_pt', 'PRI_met_sumet', 'PRI_jet_num','PRI_jet_leading_pt', 'Weight']

dt_final = joblib.load(curr_path + "/perfect_model.joblib")

print(dt_final)

def predict_duration(attributes: np.ndarray):

    pred = dt_final.predict(attributes)

    print("Duration Predicted")

    return 's' if pred == [1.] else 'b'

    # return pred