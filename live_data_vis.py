import json
import time
import pandas as pd
import plotly.express as px
from operator import itemgetter
import time
from tabulate import tabulate

pd.options.display.max_rows = 9

df = pd.read_csv('[401 Scouting Data] - 2022 CHS District Championships.csv')
# ignore everythin after started climb with time remaining
df = df.iloc[: , 0:17]
# print(df.columns)
df = df.fillna("")
# df = df[df['Team #'] == 401]
# newdf = df[df['Team #'] == 1086]
# print(df)
# print(tabulate(df))
# y = ['f', 'x', 1, 2, 3, 4]
def climb_value_cleanup(data_frame):
	data_frame['Climb'].replace('4', 15, inplace=True)
	data_frame['Climb'].replace('3', 10, inplace=True)
	data_frame['Climb'].replace('2', 6, inplace=True)
	data_frame['Climb'].replace('1', 4, inplace=True)
	data_frame['Climb'].replace('f', 0, inplace=True)
	data_frame['Climb'].replace('x', 0, inplace=True)
nums = [401, 1086, 422, 1610]
df = df[df['Team #'].isin(nums)]
points_df = df

climb_value_cleanup(df)
# print(df.columns)

# points_df = points_df['Upper Cargo Scored.1'] 

# print(tabulate(df))
fig = px.line(df, 
              x='Match #', 
              y='Climb', 
              line_group='Team #',
              color = 'Team #',
            #   width=1000,
            #   height=500,
              facet_row_spacing=0.005,
              markers=True,
            #   line_shape='spline'
              )

fig2 = px.line(points_df, 
              x='Match #', 
              y='Upper Cargo Scored.1', 
              line_group='Team #',
              color = 'Team #',
            #   width=1000,
            #   height=500,
              facet_row_spacing=0.005,
              markers=True,
            #   line_shape='spline'
              )
# fig.update_yaxes(type='category')

# fig.update_layout(autotypenumbers='convert types')
fig.show()
fig2.show()