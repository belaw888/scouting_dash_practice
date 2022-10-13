# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import frc_schedule_generator as sched

app = Dash(__name__)

dict = sched.get_qm_schedule('2022vabrb')
print()
print(dict)
df = pd.DataFrame.from_dict(dict)
match_keys = df.columns.values
match_labels = df.loc['match_labels']
# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
# df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Other/Dash_Introduction/intro_bees.csv")

# df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
# df.reset_index(inplace=True)
# print(df[:5])

# list = df.tolist()
# print('flag')
# print(list)


#Another Solution
# bee_killers = ["Disease", "Other", "Pesticides", "Pests_excl_Varroa", "Unknown", "Varroa_mites"]
# print(match_keys[0])
app.layout = html.Div([

    html.H1("District Champs Schedule", style={'text-align': 'center'}),
    
    html.Div(style={'width': "40%"}, 
            children=[
                dcc.Dropdown(id="select_match",
                    options=[{"label": x, "value": x} for x in match_keys],
                    value=match_keys[0],
                    placeholder='select a match',
                    multi=False)
                    ]
    ),
    #Another Method
    #  dcc.Dropdown(id="slct_impact",
    #              options=[{"label": x, "value":x} for x in bee_killers],
    #              value="Pesticides",
    #              multi=False,
    #              style={'width': "40%"}
    #              ),
    html.Br(),
    html.Div(id='match_num_container', children=[]),
    html.Br(),
    html.Div(className='flex-grid', children=[
        html.Div(className='col', id='red_alliance_info', children=[
            html.Div(className='col', id='red_1'),
            html.Div(className='col', id='red_2'),
            html.Div(className='col', id='red_3'),
        ]),
        html.Div(className='col', id='blue_alliance_info', children=[
            html.Div(className='col', id='blue_1'),
            html.Div(className='col', id='blue_2'),
            html.Div(className='col', id='blue_3'),
        ]),

    ]),
    html.Br(),
    

    
])

#callbacks
@app.callback(
    [Output(component_id='match_num_container', component_property='children'),
     Output(component_id='blue_1', component_property='children'),
     Output(component_id='blue_2', component_property='children'),
     Output(component_id='blue_3', component_property='children'),
     Output(component_id='red_1', component_property='children'),
     Output(component_id='red_2', component_property='children'),
     Output(component_id='red_3', component_property='children')],
     Input(component_id='select_match', component_property='value')
)
def update_graph(select_match):
    # print(select_match)
    # print(type(select_match))      

    dff = df.copy()
    #dataframe equals subset of rows of itself
    dff = dff.loc[:,select_match]
    dff = pd.DataFrame(dff)
    print(dff)

    # list = dff.values.tolist()
    # print('flag')
    # print(list)
    # dff = dff[dff['State'].isin(states_selected)]

    # dff = dff[(dff['state_code'] == 'TX') 
    # | (dff['state_code'] == 'NM') 
    # | (dff['state_code'] == 'NY')]  
    # dff = dff[(dff['state_code'] == 'TX') | (dff['state_code'] == 'AL')] 

    # fig = px.line(
    #     data_frame=dff, 
    #     x='Year',
    #     y='Pct of Colonies Impacted',
    #     line_group='state_code',
    #     color='State'
    # )
    match_key = select_match
    print(match_key)
    print(type(match_key))
    # print(dff)
    # print(match_key)
    # print(dff.loc[['match_labels', match_key]])
    match_num_container = 'Match Number: {}'.format(dff.loc['match_labels', match_key])
    # print('Match Number: {}'.format(dff.loc[['match_labels', match_key]]))
    # print(dff.loc[[match_key]].loc[['match_labels']])
    # red_container = 'Red Alliance Teams: {}'.format(dff.loc[['r1','r2','r3']])
    # print(red_container)
    # print(dff.loc[['b1']])
    
    #USE F STRINGS
    blue_1 = 'Blue Alliance 1: {}'.format(dff.loc['b1', match_key])
    blue_2 = 'Blue Alliance 2: {}'.format(dff.loc['b2', match_key])
    blue_3 = 'Blue Alliance 3: {}'.format(dff.loc['b3', match_key])
    red_1 = 'Red Alliance 1: {}'.format(dff.loc['r1', match_key])
    red_2 = 'Red Alliance 2: {}'.format(dff.loc['r2', match_key])
    red_3 = 'Red Alliance 3: {}'.format(dff.loc['r3', match_key])

    return match_num_container, blue_1, blue_2, blue_3, red_1, red_2, red_3



if __name__ == '__main__':
    app.run_server(debug=True)

