# app17.py
# minimal app using CYBORG dash-bootstrap-component theme

import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container(
    dbc.Alert("Hello CYBORG!", color="success"),
    className="p-5",
)

if __name__ == "__main__":
    app.run_server()