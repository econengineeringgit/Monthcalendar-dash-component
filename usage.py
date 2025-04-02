import dash
from dash import Dash, Input, Output, dcc, html
import dash_bootstrap_components as dbc
import monthcalendar
from datetime import datetime
import re

theme = "light-theme"
body = dbc.Container(
    [
        dbc.Row(
            [monthcalendar.Monthcalendar(id="calendar", className=f"{theme}", selectedDate=datetime.now().isoformat())],
            justify="center", align="center", class_name="h-50"
        ),
        html.Button("Switch widget theme", id="btn", n_clicks=0),
        dcc.Input(id="date-input", type="text", placeholder="Enter date (YYYY-MM-DD)"),
        dcc.Store(id="stored-date")
    ],
    style={"height": "100vh"}
)

app = Dash(__name__)
app.layout = html.Div([body])

@app.callback(
    Output("calendar", "selectedDate"),
    Input("date-input", "value"),
    prevent_initial_call=True
)
def update_date(input_date):
    print(f"{input_date = }")
    if re.search(r"(\d{4}-\d{2}-\d{2})", input_date) is None:
        print("Yo")
        return dash.no_update 
    if input_date:
        try:
            # Validate and format the input date
            return f"{input_date}T00:00:00.000Z"
        except ValueError:
            pass
    return None

@app.callback(
    Output("calendar", "className"),
    Input("btn", "n_clicks"),
    prevent_initial_call=True
)
def btn_on_click(_):
    global theme
    theme = "dark-theme" if theme == "light-theme" else "light-theme"
    return theme

if __name__ == '__main__':
    app.run(debug=True)