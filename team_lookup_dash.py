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
                    value='frc401',
                    multi=False)
                    ]
    ),
    html.Br(),
    html.Div(id='team_nickname', children=[]),
    html.Br(),
    html.Div(id='state_prov', children=[]),
    html.Br(),
    dcc.Graph(id='pie', figure={}),
    html.Br(),
    html.Iframe(id='robot_image', src='https://i.imgur.com/B2xXkOJh.jpg', width='300', height='200')
    # html.Div(children=[
    # html.Blockquote(className="imgur-embed-pub", lang='en', id="I8B4P5Z", contextMenu='false', children=[
    #     html.A(href="//imgur.com/I8B4P5Z")
    # ]),
    # html.Script(src="//s.imgur.com/min/embed.js", charSet="utf-8")
    # ])
])

# <blockquote class="imgur-embed-pub" lang="en" data-id="I8B4P5Z" data-context="false" >
# <a href="//imgur.com/I8B4P5Z"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8">
# </script>

#callbacks
@app.callback(
    [Output(component_id='team_nickname', component_property='children'),
     Output(component_id='state_prov', component_property='children'),
     Output(component_id='pie', component_property='figure')],
    #  Output(component_id='robot_image', component_property='src')],
     Input(component_id='select_team', component_property='value')
)
def update_graph(select_team):
   
    nickname = [team_lookup_dict[select_team]['profile']['nickname']]
    state_prov = [team_lookup_dict[select_team]['profile']['state_prov']]

    pie = px.pie(
        lookup.endgame_pie_chart_df(select_team), 
        template='plotly', 
        names='level', 
        values='climbs')

    robot_image = lookup.robot_image(select_team, 2022)
    print(robot_image)
    return nickname, state_prov, pie, robot_image


if __name__ == '__main__':
    app.run_server(debug=True)

