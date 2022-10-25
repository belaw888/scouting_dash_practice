import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px
from operator import itemgetter
import time
from tabulate import tabulate

pd.options.display.max_rows = 9

df = pd.read_csv('[401 Scouting Data] - 2022 CHS District Championships.csv')
# ignore everythin after started climb with time remaining
df = df.iloc[: , 0:17]
# df = df.fillna("")
def climb_value_cleanup(data_frame):
	data_frame['Climb'].replace('4', 5, inplace=True)
	data_frame['Climb'].replace('3', 4, inplace=True)
	data_frame['Climb'].replace('2', 3, inplace=True)
	data_frame['Climb'].replace('1', 2, inplace=True)
	data_frame['Climb'].replace('f', 1, inplace=True)
	data_frame['Climb'].replace('x', 0, inplace=True)
nums = [401]
climb_value_cleanup(df)
df = df[df['Team #'].isin(nums)]
# points_df = df

# climb_value_cleanup(df)

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=df['Match #'], y=df['Climb'], name="Climb Points"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df['Match #'], y=df['Upper Cargo Scored.1'], name="Teleop Upper Cargo Scored"),
    secondary_y=True,
)

# Add figure title
fig.update_yaxes(
    type='category',
    categoryarray=[0, 1, 2, 3, 4, 5],
    categoryorder='array',
    showgrid=False,
    patch=dict(
		ticktext=['No Attempt', 'Failed', 'Low', 'Mid', 'High', 'Traversal'],
		tickvals=[0, 1, 2, 3, 4, 5],
		tickmode='array',
		titlefont=dict(size=20)),
    range=[-1,6],
	secondary_y=False
)

fig.update_yaxes(
    showgrid=False,
    patch=dict(
		titlefont=dict(size=20)),
    range=[-5,25],
	secondary_y=True
)

# Set x-axis title
fig.update_xaxes(title_text="Match")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Climb Points</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Teleop Upper Cargo Balls</b>", secondary_y=True)
fig.update_layout(hovermode='x unified')
fig.show()