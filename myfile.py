import pickle
from bing_image_downloader import downloader
from PIL import Image
import pandas as pd
from main import recommender

import streamlit as st

st.title("Music Recommender 101")
"---"
with open("features_tsne.pkl", "rb") as file:
    f = pickle.load(file)

with open('data.pkl', "rb") as file:
    data = pickle.load(file)

with open('songs_artists.pkl', "rb") as file:
    songs = pickle.load(file)

with open('tracks.pkl', "rb") as file:
    tracks = pickle.load(file)

st.subheader("Select a song you like:")

c1, c2 = st.columns(2)

track_name = tracks.track_name.unique()

song = c1.selectbox('Select a song', placeholder='Type song name', options=track_name)

artists = tracks[tracks["track_name"] == song]["artists"]
artist = c2.selectbox('Select an artist:', placeholder="Choose an Artist", options=artists)

query_string = song + " " + artist
output_dir = 'dataset'
downloader.download(query_string, limit=1, output_dir=output_dir, adult_filter_off=True, force_replace=False,
                    timeout=20, verbose=True)
# album = artists[artists["artists"] == artist]["album_name"][0:1]
# st.dataframe(artists)
# genre = artists[artists["artists"] == artist]["track_genre"][0:1]
im1 = Image.open('/'.join([output_dir, query_string, 'Image_1.jpg']))
i1, i2, i3 = st.columns(3)
with i2.container(border=True):
    st.image(im1)
    st.markdown(
        "<h6 style='text-align: center; color: black;'>" + song + "<h6>" + "<center><text style='text-align: center; color: grey;'>" + artist + "<text></center>",
        unsafe_allow_html=True)

# i2.subheader(song + '\n' + album + '\n' + artist + '\n' + genre)
"---"

# st.write('You selected:', song)
# df = recommender(song)
df1 = tracks[tracks["track_name"] == song]
df2 = df1[df1["artists"] == artist]
# st.dataframe(tracks[tracks["track_name"] == song], column_config={1: 'Song Name'}, use_container_width=True,
#              hide_index=True)
# st.dataframe(df2[:1], column_config={1: 'Song Name'}, use_container_width=True,
#              hide_index=True)
# artis
recom_df = recommender(song)
# df2 = df[df["artists"] == artist][["track_name","album_name","artists"]].drop_duplicates()
# df2["genre"] = df["track_genre"]
with st.container(border=True):
    r1, r2 = st.columns(2)
    "---"

    st.markdown("<h4 style='text-align: center; color: black;'>You may also like: </h4>", unsafe_allow_html=True)

    number = st.number_input("Number of similar songs", step=5, value=20, min_value=0)

    art_tog = r1.toggle('Artist Filter')
    if art_tog:
        art_filter = r1.selectbox('From this artist', options=recom_df['artists'], disabled=False)
        recom_df = recom_df[recom_df['artists'] == art_filter]
    else:
        art_filter = r1.selectbox('From this artist', options=recom_df['artists'], disabled=True)

    gen_tog = r2.toggle('Genre Filter')
    if gen_tog:
        gen_filter = r2.selectbox('In this genre', options=recom_df['track_genre'], disabled=False)
        recom_df = recom_df[recom_df['track_genre'] == gen_filter]
    else:
        gen_filter = r2.selectbox('In this genre', options=recom_df['track_genre'], disabled=True)
    st.dataframe(recom_df.head(number), column_config={1: 'Song Name'}, use_container_width=True,
                 hide_index=True)

image = Image.open("cover.jpg")
with st.sidebar:
    st.image(image, use_column_width="always")
