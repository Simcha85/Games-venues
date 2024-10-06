import numpy as np
import pandas as pd
import folium
import streamlit as st
import matplotlib as plt
import plotly.express as px
import warnings

sa_map=folium.Map(location=[-30.5595,22.9375], zoom_start=5)

st.title('KAIZER CHIEFS VENUES USED IN SOUTH AFRICA')

df=pd.read_excel('STADIUM info.xlsx')
df

games_df=df[['STADIUM','Result','Latitude','Longitude']]

stadiumdf=games_df.groupby('STADIUM').value_counts()

def assign_marker_color(Result):
    if Result=='Win':
        return 'green'
    if Result=='Loss':
        return 'red'
    else:
        return 'blue'
games_df.loc[:,'marker_color']=games_df.loc[:,'Result'].apply(assign_marker_color)
games_df.head()



label=games_df['STADIUM']
lats=games_df['Latitude']
long=games_df['Longitude']

for lat,lng,label in zip(lats,long,label):
    folium.Marker([lat,lng],popup=label).add_to(sa_map)
                                                
sa_map.save('sa_maptest.html')

import streamlit.components.v1 as components

def get_kc_map():
    HtmlFile=open('sa_maptest.html','r',encoding='utf-8')
    games_map=HtmlFile.read()
    return games_map

games_map=get_kc_map()

def count_result(Result):
    if Result =='Win':
        return 1
    if Result =='Draw':
        return 1
    else:
        return 1
games_df.loc[:,'Event_count']=games_df.loc[:,"Result"].apply(count_result)

line_data=games_df['STADIUM'].value_counts()
fig=px.line(line_data, markers=True, title='Number of Games played in each Stadium')
fig.update_layout(
    showlegend=True,
    width=800,
    height=600
)
st.write(fig)

fig2=px.bar(games_df,x='STADIUM',y='Event_count',color='Result', title='Results for Each Venue')
fig2.update_layout(
    showlegend=True,
    width=800,
    height=600
              )
st.write(fig2)

with st.container():
    components.html(games_map,width =2000, height=1000)