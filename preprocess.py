import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from category_encoders import TargetEncoder, CountEncoder
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv("dataset.csv")

data.drop(["track_id", "Unnamed: 0"], axis=1, inplace=True)

data.loc[data["explicit"] == False, "explicit"] = 0
data.loc[data["explicit"] == True, "explicit"] = 1

features = data.columns[3:]

with open("data.pkl", 'wb') as file:
    pickle.dump(data, file)

encoder = LabelEncoder()
data["track_genre"] = encoder.fit_transform(data["track_genre"])

for x in data.keys()[3:]:
    data[x] = pd.to_numeric(data[x])

scaler = StandardScaler()
features = data[data.columns[3:]]
scaled_features = scaler.fit_transform(features)

features_df = pd.DataFrame(scaled_features, columns=data.columns[3:])

with open("features_df.pkl", 'wb') as file:
    pickle.dump(features_df, file)
