from dash import dcc
from dash import html
from dash import dash_table as dt
from database import df


# Dashboard Layout / View


layout = html.Div(style={'backgroundColor': '#2b2b2b', 'color': 'white', 'padding': '20px'}, children=[
    html.Center(children=[
        html.B(html.H1('Animal Dashboard')),
    ]),
    html.Hr(),
    
    # Each filter
    dcc.RadioItems(
    id='rescue-type-filter',
    style={'color': 'white'},
    options=[
        {'label': 'Reset', 'value': 'Reset'},
        {'label': 'Dogs', 'value': 'Dog'},
        {'label': 'Cats', 'value': 'Cat'},
        {'label': 'Adoptions Only', 'value': 'Adoption'},
    ],
    value='Reset',
    labelStyle={'display': 'inline-block'}
),
    html.Hr(),
    dt.DataTable(
        id='datatable-id',
        style_header={'backgroundColor': '#3a3a3a', 'color': 'white'},
        style_data={'backgroundColor': '#2b2b2b', 'color': 'white'},
        style_filter={'backgroundColor': '#3a3a3a', 'color': 'white'},
 
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),

        # Features for the interactive data table to make it user-friendly for the client
        editable=False,
        filter_action="native",
        sort_action="native",
        column_selectable=False,
        row_selectable=False,
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_size=12,
        page_current=0,
    ),
    html.Br(),
    html.Hr(),
    
#This sets up the dashboard so that your chart and your geolocation chart are side-by-side
    html.Div(className='row',
         style={'display' : 'flex'},
             children=[
        html.Div(
            id='graph-id',
            className='col s12 m6',

            ),
        html.Div(
            id='map-id',
            className='col s12 m6',
            )
        ])
])