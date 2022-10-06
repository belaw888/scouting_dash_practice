# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)


app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Other/Dash_Introduction/intro_bees.csv")

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:5])

# list = df.tolist()
# print('flag')
# print(list)


#Another Solution
# bee_killers = ["Disease", "Other", "Pesticides", "Pests_excl_Varroa", "Unknown", "Varroa_mites"]

app.layout = html.Div([

    html.H1("Beehive Data", style={'text-align': 'center'}),
    
    dcc.Dropdown(df['Affected by'].unique(), 
                 id="slct_affected_by",
                 value='Disease'
                 ),
    #Another Method
    #  dcc.Dropdown(id="slct_impact",
    #              options=[{"label": x, "value":x} for x in bee_killers],
    #              value="Pesticides",
    #              multi=False,
    #              style={'width': "40%"}
    #              ),

    html.Div(id='affected_by_output_container', children=[]),
    html.Br(),

    dcc.Dropdown(df['State'].unique(),
                 id='states_selected',
                 value='Virginia',
                 multi=True),

    html.Div(id='state_output_container', children=[]),
    html.Br(),

    dcc.Graph(id='bee_graph', figure={})
])

#callbacks
@app.callback(
    [Output(component_id='bee_graph', component_property='figure'),
     Output(component_id='affected_by_output_container', component_property='children'),
     Output(component_id='state_output_container', component_property='children')],
    [Input(component_id='slct_affected_by', component_property='value'),
     Input(component_id='states_selected', component_property='value')]
)
def update_graph(affected_by_slctd, states_selected):
    print(affected_by_slctd)
    print(type(affected_by_slctd))      
    print(states_selected)
    print(type(states_selected))

    if type(states_selected) == str:
        states_selected = [states_selected]

    # state_selected_list = states_selected

    dff = df.copy()
    #dataframe equals subset of rows of itself
    dff = dff[dff['Affected by'] == affected_by_slctd]

    # list = dff.values.tolist()
    # print('flag')
    # print(list)
    dff = dff[dff['State'].isin(states_selected)]

    # dff = dff[(dff['state_code'] == 'TX') 
    # | (dff['state_code'] == 'NM') 
    # | (dff['state_code'] == 'NY')]  
    # dff = dff[(dff['state_code'] == 'TX') | (dff['state_code'] == 'AL')] 

    fig = px.line(
        data_frame=dff, 
        x='Year',
        y='Pct of Colonies Impacted',
        line_group='state_code',
        color='State'
    )

    affect_container = 'User Selected Option: {}'.format(affected_by_slctd)
    state_container = 'User Selected Option: {}'.format(states_selected)

    return fig, affect_container, state_container



if __name__ == '__main__':
    app.run_server(debug=True)

