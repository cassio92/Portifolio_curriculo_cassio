import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import plotly.offilne as py

dados_eixo_x = ['2018','2019','2020','2021','2022','2023']
dados_eixo_y = [125645,255698,213779,546987,356478,687963]

fig = px.pie(names=dados_eixo_x, values=dados_eixo_y, width=300, height=300)
fig.show()

