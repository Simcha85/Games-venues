import numpy as np
import pandas as pd
import streamlit as st

#had to remove plotly.express as it was causing an error in the deployment

st.set_page_config(layout="wide")

#these functions are for the buttons in the Navigation bar
def stats(df):
    st.header('Data Statistics')
    st.write(df['Home'].value_counts())

def headers(df):
    st.header('Data Header')
    st.write(df.tail())

def games_played(used_fig):
    st.header('Games Played at Each Venue')
    st.components.v1.html(used_fig,height=600)

def results(result_fig):
    st.header('Results At Venues')
    st.components.v1.html(result_fig,height=600)

st.title('KAIZER CHIEFS VENUES USED IN SOUTH AFRICA')
#st.logo('KC_logo.jpg',link="https:/kaizerchiefs.com") was causing error in deployment
#st.image('fnb.jpg')
st.write('This app is to show which venues Kaizer Chiefs has used in South Africa between 2017-2024, along with the result outcome for each venue. The statistics show how many home games the Club has played along with how many times they have played against each team away.')

st.sidebar.title('Navigation')

options=st.sidebar.radio('Pages', options=['Data Statistics','Data Header', 'Venue Count','Result Tally'])


df=pd.read_excel('Stadium_info_vsc.xlsx')
del df['Unnamed: 0']

st.dataframe(df)

def get_kc_map():
    HtmlFile=open('games_map.html','r',encoding='utf-8')
    games_map=HtmlFile.read()
    return games_map

games_map=get_kc_map()

games_df=df[['STADIUM','Result','Latitude','Longitude']]

stadiumdf=games_df.groupby('STADIUM').value_counts()

def assign_marker_color(Result):
    if Result=='Win':
        return 'green'
    if Result=='Loss':
        return 'red'
    else:
        return 'blue'
games_df.loc[:,'Outcome']=games_df.loc[:,'Result'].apply(assign_marker_color)

used = '/workspaces/Games-venues/used.html'
resultsh = '/workspaces/Games-venues/results.html'

with open(used,'r') as f:
    used_fig=f.read()
with open(resultsh,'r') as i:
    result_fig=i.read()

if options=='Data Statistics':
    stats(df)
if options=='Venue Count':
    games_played(used_fig)
if options=='Result Tally':
    results(result_fig)
elif options=='Data Header':
    headers(df)


import streamlit.components.v1 as components
with st.container():
    components.html(games_map,width =2000, height=1000)
