# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import frc_team_data_lookup as lookup

app = Dash(__name__)

event_key = '2022varr'
teams = lookup.get_event_teams_list(event_key)
team_lookup_dict = lookup.event_team_lookup_dict(event_key)

app.layout = html.Div([

    html.H1("2022 Rumble in the Roads Team Lookup", style={'text-align': 'center'}),
    
    html.Div(style={'width': "40%"}, 
            children=[
                dcc.Dropdown(id="select_team",
                    options=[{"label": x, "value": x} for x in teams],
                    value=teams[0],
                    multi=False)
                    ]
    ),
    html.Br(),
    html.Div(id='team_nickname', children=[]),
    html.Div(id='state_prov', children=[]),
    html.Br(),
    
])

#callbacks
@app.callback(
    [Output(component_id='team_nickname', component_property='children'),
     Output(component_id='state_prov', component_property='children')],
     Input(component_id='select_team', component_property='value')
)
def update_graph(select_team):
   
    nickname = [team_lookup_dict[select_team]['profile']['nickname']]
    state_prov = [team_lookup_dict[select_team]['profile']['state_prov']]

    return nickname, state_prov


if __name__ == '__main__':
    app.run_server(debug=True)

