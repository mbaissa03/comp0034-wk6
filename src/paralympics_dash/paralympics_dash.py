# Imports for Dash and Dash.html
# Imports for Dash and Dash.html
from dash import Dash, html,Input, Output, callback
import dash_bootstrap_components as dbc

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]
# Pass the stylesheet variable to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets,meta_tags=meta_tags)
row_one = dbc.Row([
    dbc.Col([html.H1("Paralympics Data Analytics"),
    html.P(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida. Fusce efficitur posuere metus posuere malesuada. ")]),
])

row_two = dbc.Row([
    dbc.Col(children=[dbc.Select(
    options=[
        {"label": "Events", "value": "events"},  # The value is in the format of the column heading in the data
        {"label": "Sports", "value": "sports"},
        {"label": "Countries", "value": "countries"},
        {"label": "Athletes", "value": "participants"},
    ],
    value="events",  # The default selection
    id="dropdown-input",  # id uniquely identifies the element, will be needed later for callbacks
),], width=2),
    dbc.Col(children=[html.Div(
    [
        dbc.Label("Select the Paralympic Games type"),
        dbc.Checklist(
            options=[
                {"label": "Summer", "value": "summer"},
                {"label": "Winter", "value": "winter"},
            ],
            value=["summer"],  # Values is a list as you can select 1 AND 2
            id="checklist-input",
        ),
    ]
)
], width={"size": 2, "offset": 4}),  # 4 'empty' columns between this and the previous column
])

row_three = dbc.Row([
    dbc.Col(children=[html.Img(src=app.get_asset_url('map-placeholder.png'), className="img-fluid")], width=6),
    dbc.Col(children=[dbc.Card(
    [
        dbc.CardImg(src="assets/logos/1960_Rome.png", top=True),
        dbc.CardBody(
            [
                html.H4("TownName 2026", className="card-title"),
                html.P(
                    "Highlights of the paralympic event will go here. This will be a sentence or two.",
                    className="card-text",
                ),
                html.P(
                    "Number of athletes: XX",
                    className="card-text",
                ),
                html.P(
                    "Number of events: XX",
                    className="card-text",
                ),
                html.P(
                    "Number of countries: XX",
                    className="card-text",
                ),
            ]
        ),
    ],
    # style={"width": "18rem"},
)], width=6),
])

app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
    
])
# Add an HTML layout to the Dash app
#app.layout = dbc.Container([
    #dbc.Row([
        #dbc.Col(html.H1("Hello World"))
             
    #html.P('random text', className='my-class', id='my-p-element'),
    #html.Img(src=app.get_asset_url('bar-chart-placeholder.png'))

    #html.Img(
            #src=app.get_asset_url('bar-chart-placeholder.png'),
            #id="click-div"),
    #html.P(id="click-output"),
    #])

#])

#@callback(
    #Output("click-output", "children"),
    #Input("click-div", "n_clicks")
    #)
#def click_counter(n_clicks):
    #return f"The graph above has been clicked this many times: {n_clicks}"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)