import pickle

from sklearn.manifold import TSNE

model = TSNE(n_components=2)

with open("features_df.pkl", 'rb') as file:
    features_df = pickle.load(file)

features_tsne = model.fit_transform(features_df)

with open("features_tsne.pkl", 'wb') as file:
    pickle.dump(features_tsne, file)
