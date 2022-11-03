# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = Dash(__name__)


df = pd.read_csv('[401 Scouting Data] - 2022 CHS District Championships.csv')
df = df.iloc[: , 0:17]

df = df.fillna("")

def climb_value_cleanup(data_frame):
	data_frame['Climb'].replace('4', 15, inplace=True)
	data_frame['Climb'].replace('3', 10, inplace=True)
	data_frame['Climb'].replace('3', 6, inplace=True)
	data_frame['Climb'].replace('1', 4, inplace=True)
	data_frame['Climb'].replace('f', 0, inplace=True)
	data_frame['Climb'].replace('x', 0, inplace=True)
# nums = [401, 1086, 422, 1610]
# df = df[df['Team #'].isin(nums)]
# points_df = df

climb_value_cleanup(df)
#Another Solution
match_data_type = ["Climb", "Upper Cargo Scored.1"]

app.layout = html.Div([

    html.H1("rumble team lookup", style={'text-align': 'center'}),
 
    dcc.Dropdown(id="select_data_type",
                 options=[{"label": x, "value": x} for x in match_data_type],
                 value="Climb",
                 multi=False,
                 style={'width': "40%"}
                 ),

    html.Div(id='data_type_output_container', children=[]),
    html.Br(),

    dcc.Dropdown(df['Team #'].unique(),
                 id='teams_selected',
                 value='401',
                 multi=True),

    html.Div(id='team_output_container', children=[]),
    html.Br(),

    dcc.Graph(id='scoring_graph', figure={})
])

#callbacks
@app.callback(
    [Output(component_id='scoring_graph', component_property='figure'),
     Output(component_id='data_type_output_container', component_property='children'),
     Output(component_id='team_output_container', component_property='children')],
    [Input(component_id='select_data_type', component_property='value'),
     Input(component_id='teams_selected', component_property='value')]
)
def update_graph(select_data_type, teams_selected):

    if type(teams_selected) == str:
        teams_selected = [teams_selected]

    # state_selected_list = states_selected

    dff = df.copy()
    #dataframe equals subset of rows of itself
    # dff = dff[dff[''] == select_data_type]

    # list = dff.values.tolist()
    # print('flag')
    # print(list)
    dff = dff[dff['Team #'].isin(teams_selected)]

    # dff = dff[(dff['state_code'] == 'TX') 
    # | (dff['state_code'] == 'NM') 
    # | (dff['state_code'] == 'NY')]  
    # dff = dff[(dff['state_code'] == 'TX') | (dff['state_code'] == 'AL')] 

    fig = px.line(
        data_frame=dff, 
        x='Match #', 
        y=select_data_type, 
        line_group='Team #',
        color = 'Team #',
        facet_row_spacing=0.005,
        

        markers=True,
    )
    
    # comments_container = comments

    data_type_output_container = 'User Selected Option: {}'.format(select_data_type)
    team_output_container = 'User Selected Option: {}'.format(teams_selected)

    return fig, data_type_output_container, team_output_container



if __name__ == '__main__':
    app.run_server(debug=True)
