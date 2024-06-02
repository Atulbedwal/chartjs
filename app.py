import os
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# Load the preprocessed data
df = pd.read_csv('preprocessed_data.csv')

# Create visualizations
category_counts = df['category'].value_counts().reset_index()
category_counts.columns = ['category', 'count']
fig_alert_categories = px.bar(category_counts, 
                              x='category', y='count', 
                              labels={'category': 'Category', 'count': 'Count'},
                              title='Alert Categories Distribution')

fig_alerts_over_time = px.line(df, x='timestamp', y=df.index, 
                               labels={'timestamp': 'Time', 'index': 'Alerts'},
                               title='Alerts Over Time')

top_source_ips = df['src_ip'].value_counts().reset_index().head(10)
top_source_ips.columns = ['src_ip', 'count']
fig_top_source_ips = px.bar(top_source_ips, 
                            x='src_ip', y='count', 
                            labels={'src_ip': 'Source IP', 'count': 'Count'},
                            title='Top Source IP Addresses')

top_dest_ports = df['dest_port'].value_counts().reset_index().head(10)
top_dest_ports.columns = ['dest_port', 'count']
fig_top_dest_ports = px.bar(top_dest_ports, 
                            x='dest_port', y='count', 
                            labels={'dest_port': 'Destination Port', 'count': 'Count'},
                            title='Top Destination Ports')

# Create a Dash application
app = Dash(__name__)

# Set dark theme
app.layout = html.Div(style={'backgroundColor': '#111111', 'color': '#7FDBFF'}, children=[
    html.H1(children='Network Alerts Dashboard', style={'textAlign': 'center'}),
    
    # Alert Categories Distribution
    html.Div([
        dcc.Graph(
            id='alert-categories',
            figure=fig_alert_categories
        )
    ]),
    
    # Alerts Over Time
    html.Div([
        dcc.Graph(
            id='alerts-over-time',
            figure=fig_alerts_over_time
        )
    ]),
    
    # Top Source IP Addresses
    html.Div([
        dcc.Graph(
            id='top-source-ips',
            figure=fig_top_source_ips
        )
    ]),
    
    # Top Destination Ports
    html.Div([
        dcc.Graph(
            id='top-dest-ports',
            figure=fig_top_dest_ports
        )
    ]),
])

# Run the application
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
