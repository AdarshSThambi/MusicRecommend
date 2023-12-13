import pickle
from google_images_download import google_images_download
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate
import streamlit as st

with open("features_tsne.pkl", 'rb') as file:
    features_tsne = pickle.load(file)

with open("data.pkl", 'rb') as file:
    data = pickle.load(file)

# plt.scatter(features_tsne[:, 0], features_tsne[:, 1])
# plt.show()
# print(tabulate(pd.DataFrame(features_tsne).head(),headers='keys'))

tracks = data[list(data.columns[:3]) + ['track_genre']]

with open("tracks.pkl", 'wb') as file:
    pickle.dump(tracks, file)


# print(tracks.head())

def get_similarities(query_index):
    similarities = cosine_similarity(features_tsne[query_index:query_index + 1], features_tsne)
    tr1 = tracks
    tr1["similarity"] = similarities[0]
    return tr1.sort_values(by="similarity", ascending=False)


def recommender(song):
    ind = tracks[tracks.track_name == song].index[0]
    track_similarities = get_similarities(ind)
    return track_similarities[['track_name', 'album_name', 'artists', 'track_genre']]


df = recommender('Photograph')
# print(df[df['track_genre'] == 'happy'].head())
# print(df.head())
# print(tracks.shape)
# print(df['track_genre'].value_counts())
df1 = pd.DataFrame()
df1['Song'] = tracks['track_name'] + ' ## ' + tracks['artists']
# print(df1)

