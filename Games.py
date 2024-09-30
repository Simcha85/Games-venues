import folium.plugins
import numpy as np
import pandas as pd
import folium
import streamlit as st
from folium.plugins import MarkerCluster
import warnings

sa_map=folium.Map(location=[-30.5595,22.9375], zoom_start=5)


df=pd.read_excel('STADIUM info.xlsx')
df

games_df=df[['STADIUM','Result','Latitude','Longitude']]
games_df.head()

st.title("Venues used by Kaizer Chiefs in South Africa")

def assign_marker_color(Result):
    if Result=='Win':
        return 'green'
    if Result=='Loss':
        return 'red'
    else:
        return 'blue'
games_df['marker_color']=games_df['Result'].apply(assign_marker_color)
games_df.head()

marker_cluster= MarkerCluster()

sa_map.add_child(marker_cluster)

for index, record in games_df.iterrows():
    marker=folium.Marker([record['Latitude'],record['Longitude']],
                         icon=folium.Icon(color='white', icon_color=record['marker_color']))
    marker_cluster.add_child(marker)
sa_map.add_child(marker_cluster)

sa_map.save('sa_maptest.html')

import streamlit.components.v1 as components

def get_kc_map():
    HtmlFile=open('sa_maptest.html','r',encoding='utf-8')
    games_map=HtmlFile.read()
    return games_map

games_map=get_kc_map()


with st.container():
    components.html(games_map,width =2000, height=1000)

