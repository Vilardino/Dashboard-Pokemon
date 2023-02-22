# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

figf = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

categories = ['processing cost','mechanical properties','chemical stability',
              'thermal stability', 'device integration']

fig = go.Figure()

#gera status pokemon em rede

dfp = pd.read_csv('pokemon.csv')

ordem = ['pokedex_number','name', 'hp','attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'base_total',
        'type1', 'type2', 'height_m', 'weight_kg',  'abilities',
       'base_egg_steps', 'base_happiness', 'capture_rate',
       'classfication', 'experience_growth',
       'japanese_name',  'percentage_male', 'against_bug', 'against_dark', 'against_dragon',
       'against_electric', 'against_fairy', 'against_fight', 'against_fire',
       'against_flying', 'against_ghost', 'against_grass', 'against_ground',
       'against_ice', 'against_normal', 'against_poison', 'against_psychic',
       'against_rock', 'against_steel', 'against_water',
       'is_legendary']

df = dfp[ordem]
maximo = (dfp.loc[:,['hp','attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].max()).max()
minimo = (dfp.loc[:,['hp','attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].min()).min()


pokemon_list = ['Lucario', 'Pikachu'] #variaveis a serem mudadas para comparar status #######################################

df1 = df.loc[df['name'].isin(pokemon_list)]

for i in pokemon_list:
  df_filtered = df.loc[df['name'] == i]
  r = [int(df_filtered['hp']), int(df_filtered['attack']), int(df_filtered['defense']), int(df_filtered['sp_attack']), int(df_filtered['sp_defense']), int(df_filtered['speed'])]
  fig.add_trace(go.Scatterpolar(
      r=r,
      theta=['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed'],
      fill='toself',
      name= i
  ))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[minimo-20, maximo+20]
        )),
    showlegend=True
)






app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=figf
    ),

    dcc.Graph(figure=fig)

])

if __name__ == '__main__':
    app.run_server(debug=True)