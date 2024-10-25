import numpy as np
import pandas as pd
import streamlit as st
import plotly_express as px
import warnings

def stats(df):
    st.header('Data Statistics')
    st.write(df['Home'].value_counts())

def headers(df):
    st.header('Data Header')
    st.write(df.tail())

def games_played(games_df):
    st.header('Games Played at Each Venue')
    st.plotly_chart(fig)

def results(games_df):
    st.header('Results At Venues')
    st.plotly_chart(fig2)

st.title('KAIZER CHIEFS VENUES USED IN SOUTH AFRICA')
st.logo('KC logo black back.jpg')
st.image('fnb.jpg')

st.sidebar.title('Navigation')

options=st.sidebar.radio('Pages', options=['Data Statistics','Data Header', 'Venue Count','Result Tally'])


df=pd.read_excel('STADIUM info.xlsx')


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

def count_result(Result):
    if Result =='Win':
        return 1
    if Result =='Draw':
        return 1
    else:
        return 1
games_df.loc[:,'Event_count']=games_df.loc[:,"Result"].apply(count_result)


line_data=games_df['STADIUM'].value_counts()
fig=px.line(line_data,markers=True, title='Number of Games played in each Stadium')
fig.update_layout(
    showlegend=True,
    width=800,
    height=600
)


fig2=px.bar(games_df,x='STADIUM',y='Event_count',color='Result', title='Results for Each Venue')
fig2.update_layout(
    showlegend=True,
    width=800,
    height=600
              )


fig3=px.bar(df, x='Home',y='Away',color='Result')
fig3.update_layout(
    showlegend=True,
    width=800,
    height=600
)

if options=='Data Statistics':
    stats(df)
if options=='Venue Count':
    games_played(games_df)
if options=='Result Tally':
    results(games_df)
elif options=='Data Header':
    headers(df)

import streamlit.components.v1 as components
with st.container():
    components.html(games_map,width =2000, height=1000)
