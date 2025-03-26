from dash import Dash, Input, dcc, Output, html
import dash_bootstrap_components as dbc

import monthcalendar

theme = "light-theme"
body = dbc.Container(
    [
        dbc.Row(
            [monthcalendar.Monthcalendar(id="calendar", className=f"{theme}")],
            justify="center", align="center", class_name="h-50"
        ),
        html.Button("Switch widget theme", id="btn", n_clicks=0),
        dcc.Store(id="stored-date")
    ],
    style={"height": "100vh"}
)

app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])
app.layout = html.Div([body])

@app.callback(
    Output("stored-date", "data"),
    Input("calendar", "selectedDate"),
    prevent_initial_call=False
)
def monthcalendar_callback(date):
    print(f"Stored {date = }")
    return date

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