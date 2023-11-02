from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

#Definindo aplicativo do flask
app = Dash(__name__)

# Suponha que você tenha um quadro de dados "longo"
# Veja https://plotly.com/python/px-arguments/ para mais informações
df = pd.DataFrame({
    "Frutas": ["Maçãs", "Laranjas", "Bananas", "Maçãs", "Laranjas", "Bananas"],
    "Quantidade": [4, 1, 2, 2, 4, 5],
    "Cidades": ["BH", "BH", "BH", "CONTAGEM", "CONTAGEM", "CONTAGEM"]
})
#criando o grafico
fig = px.bar(df, x="Frutas", y="Quantidade", color="Cidades", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Faturamento das lojas'),
    html.H2(children='Gráfico com o faturamento de todas os produtos separados por loja'),
    html.Div(children='''
        Obs: Este gráfico mostra a quantidade de produtos vendidos não o faturamento.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
#app flask exibe na tela
if __name__ == '__main__':
    app.run(debug=True)