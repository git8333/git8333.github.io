from database import df
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

# Interaction Between Components / Controller

#Simple cache dict
_cache = {}

def callback_reg(app):
    @app.callback(Output('datatable-id','data'),
                [Input('rescue-type-filter', 'value')])
    def dashboard(filter_type):

        # Returned cache if possible
        if filter_type in _cache:
            return _cache[filter_type]
        
        dff = df.copy()

        if filter_type == 'Reset':
            return dff.to_dict('records')
        elif filter_type == 'Dog':
            dff = dff[dff['Animal Type'] == 'Dog']
        elif filter_type == 'Cat':
            dff = dff[dff['Animal Type'] == 'Cat']
        elif filter_type == 'Adoption':
            dff = dff[dff['Outcome Type'] == 'Adoption']

        # Store results before return
        _cache[filter_type] = dff.to_dict('records')

        return dff.to_dict('records')

    @app.callback(
        Output('datatable-id', 'style_data_conditional'),
        [Input('datatable-id', 'selected_columns')]
    )
    def update_styles(selected_columns):
        return [{
            'if': { 'column_id': i },
            'background_color': '#D2F3FF'
        } for i in selected_columns]


    # Bar chart animal outcomes
    @app.callback(
        Output('map-id', "children"),
        [Input('datatable-id', "data")])
    def update_outcome_chart(data):
        dff = pd.DataFrame.from_dict(data)
        df_outcomes = dff.groupby(['Outcome Type']).size().reset_index(name='Count')
        fig = px.bar(df_outcomes, x='Outcome Type', y='Count', title='Animal Outcomes', color='Outcome Type')
        fig.update_layout(paper_bgcolor='#2b2b2b', plot_bgcolor='#2b2b2b', font_color='#2b2b2b')

        return [dcc.Graph(figure=fig)]
    

    # Pie Chart that shows animal breed
    @app.callback(
        Output('graph-id', "children"),
        [Input('datatable-id', "data")])
    def graph(data):
        dff = pd.DataFrame.from_dict(data)
        df_grouped = dff.groupby(['Breed']).size().reset_index(name='Amount')

        # Keep only 10 showing, rest as Other
        df_grouped = df_grouped.sort_values('Amount', ascending = False)
        top10breeds = df_grouped.head(10)
        other_count = df_grouped.iloc[10:]['Amount'].sum()
        if other_count > 0:
            other_row = pd.DataFrame([{'Breed': 'Other', 'Amount': other_count}])
            top10breeds = pd.concat([top10breeds, other_row], ignore_index=True)
        fig = px.pie(top10breeds, values = 'Amount', names='Breed', title='Animal Breed')
        return [
            dcc.Graph(figure=fig)
        ]