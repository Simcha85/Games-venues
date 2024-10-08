import numpy as np
import pandas as pd
import streamlit as st
import plotly
import plotly.express as px
import warnings


st.title('KAIZER CHIEFS VENUES USED IN SOUTH AFRICA')
st.logo('KC logo black back.jpg')
st.image('fnb.jpg')

df=pd.read_excel('STADIUM info.xlsx')
df

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
st.write(fig)

fig2=px.bar(games_df,x='STADIUM',y='Event_count',color='Result', title='Results for Each Venue')
fig2.update_layout(
    showlegend=True,
    width=800,
    height=600
              )
st.write(fig2)

import streamlit.components.v1 as components
with st.container():
    components.html(games_map,width =2000, height=1000)
