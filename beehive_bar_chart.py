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


app.layout = html.Div([

    html.H1("Beehive Data", style={'text-align': 'center'}),
    
    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),

    dcc.Graph(id='bee_map', figure={})
])

#callbacks
@app.callback(
    Output(component_id='bee_map', component_property='figure'),
    Input(component_id='slct_year', component_property='value')
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    dff = df.copy()
    #dataframe equals subset of itself
    dff = dff[dff['Year'] == option_slctd]
    dff = dff[dff['Affected by'] == 'Varroa_mites']

    fig = px.bar(
        data_frame=dff, 
        x='state_code',
        y='Pct of Colonies Impacted'
    )

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)

