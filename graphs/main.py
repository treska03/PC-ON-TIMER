import datetime
import sqlite3

import numpy as np
import pandas as pd
import plotly.graph_objects as go

conn = sqlite3.connect('./PC-TIMER-DB.sql') 
          
sql_query = pd.read_sql_query ('''
                               SELECT
                               date, time_spent
                               FROM Days
                               ''', conn)

df = pd.DataFrame(sql_query, columns = ['date', 'time_spent'])

df["date"] = pd.to_datetime(df["date"], dayfirst=True)
df['Time spent'] = df['time_spent'].apply(lambda x:str(datetime.timedelta(seconds=x)))
df['Time spent'] = pd.to_datetime(df['Time spent'])

df = df.drop("time_spent", axis=1)

dfall = df.resample("M", on="date").mean().copy()
dfyearly = dfall.tail(12).copy()
dfweekly = df.tail(7).copy()
dfmonthly = df.tail(30).copy()

del df

dfs = {'Week':dfweekly, 'Month': dfmonthly, 'Year' : dfyearly, "All" : dfall}

for dframe in list(dfs.values()):
    dframe['StfTime'] = dframe['Time spent'].apply(lambda x: x.strftime("%H:%M"))

frames = len(dfs) # number of dataframes organized in  dict
columns = len(dfs['Week'].columns) - 1 # number of columns i df, minus 1 for Date
scenarios = [list(s) for s in [e==1 for e in np.eye(frames)]]
visibility = [list(np.repeat(e, columns)) for e in scenarios]
lowest_value = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
highest_value = dfweekly["Time spent"].max().ceil("H")
buttons = []
fig = go.Figure()

for i, (period, df) in enumerate(dfs.items()):
    for column in df.columns[1:]:
        fig.add_bar(
            name = column,
            x = df['date'],
            y = df[column], 
            customdata=df[['StfTime']], 
            text=df['StfTime'],
            showlegend=False,
            visible=True if period=='Week' else False # 'Week' values are shown from the start
                       )
        
        #Change display data to more friendly format
        fig.update_traces(textfont=dict(size=20), hovertemplate='<b>Time ON</b>: %{customdata[0]}</br>')
        
        #Change range for better scalling
        this_value =df["Time spent"].max().ceil("H")
        if highest_value <= this_value:
            highest_value = this_value
            fig.update_yaxes(range=[lowest_value, highest_value])

                
    # one button per dataframe to trigger the visibility
    # of all columns / traces for each dataframe
    button =  dict(label=period,
                   method = 'restyle',
                   args = ['visible',visibility[i]])
    buttons.append(button)

fig.update_yaxes(dtick=60*60*1000, tickformat='%H:%M')
fig.update_xaxes(type='date', dtick='D1')
#fig.layout.xaxis.tickformat = '%b' for dfyearly and dfall

fig.update_layout(updatemenus=[dict(type="dropdown",
                                    direction="down",
                                    buttons = buttons)])
fig.show()

#TODO FIX AVG LINE
