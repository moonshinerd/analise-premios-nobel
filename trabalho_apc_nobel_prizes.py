# -*- coding: utf-8 -*-
"""Trabalho APC - Nobel Prizes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cx-LPe3Z9DqWXXaN7EHCMJKo30lGDU3N

#Grupo B - Prêmios Nobel

##Membros

|Matrícula|Nome Completo|
|:---|:---|
|000000000|Arthur Souto Santos|
|000000000|Ciro de Oliveira Braga|
|000000000|Gabriela Xavier Rodrigues|
|000000000|Marcos Vieira Marinho|
|000000000|Maria Helena Carvalho|
|000000000|Manuella Magalhães Valadares|
|000000000|Pamela Grazielle dos Santos|
|000000000|Víctor Hugo Lima Schmidt|

##Objetivo

O objetivo desse trabalho é analisar informações sobre os indivíduos e instituições que ganharam os prêmios do Nobel ao longo do tempo. Isso pode incluir informações como a nacionalidade, gênero e área de estudo dos vencedores, bem como as tendências e padrões nos prêmios ao longo do tempo. Essas informações podem ser usadas para entender melhor a história e a evolução das áreas de estudo premiadas.

##Bases de Dados

|Nome|Descrição|Colunas| Amostras|
|:---|:---|--:|--:|
|[EDA on Nobel dataset](https://drive.google.com/file/d/1209NxTfZPPJqb2VaiWuj0QEeM4FG7euE/view?usp=share_link)|Dados dos prêmios Nobel de 1901 até 2016|18|911|
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
url = 'https://drive.google.com/file/d/1209NxTfZPPJqb2VaiWuj0QEeM4FG7euE/view?usp=share_link'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path, sep=',')
df = df.values.tolist()
print(df)

"""##Gráficos

1. Quantidade de prêmios Nobel por ano
2. Número de condecorados de acordo com o país de origem
3. Ganhadores do Prêmio Nobel por Idade
4. Gênero dos Ganhadores por Categoria

###Quantidade de prêmios Nobel por ano
O objetivo desse gráfico é mostrar a variação na quantidade de prêmios concedidos em diferentes anos. Isso pode ajudar a identificar tendências ou padrões na atribuição dos prêmios ao longo do tempo.
"""

year = []
for i in df:
  year.append(i[0])
qtd_nobel_ano = [] 
anos= [] 
for i in range(len(year)): 
  if year[i] not in anos:
    anos.append(year[i])
    qtd_nobel_ano.append(1)
  else:
    qtd_nobel_ano[anos.index(year[i])] += 1
fig8 = px.bar(x = anos, y = qtd_nobel_ano, labels= {
    'x': 'Ano ',
    'y': 'Nobel '
    })
fig8 = fig8.update_layout(title={
    'text' : 'Quantidade de premios Nobel por ano',
    'y': 0.9,
    'x': 0.5
})
fig8.show()

"""###Número de condecorados de acordo com o país de origem
Esse gráfico tem como objetivo mostrar a distribuição dos prêmios entre diferentes países e identificar quais países têm uma maior proporção de ganhadores. Ele pode ser usado para comparar a distribuição de prêmios entre diferentes regiões ou para analisar a influência de eventos políticos ou econômicos em diferentes países. Ele também pode ser usado para identificar tendências e padrões na distribuição de prêmios entre países.
"""

BC = []
for i in df:
  BC.append(i[10])
total = len(BC)
nome_paises = []
qtd_nobel_paises = []
for y in range(total):
  if isinstance(BC[y], float):
    BC[y] = str(BC[y])
  if "(" in BC[y]:      #Exemplo: Prussia (Germany)
    BC[y] = BC[y][:BC[y].index('(')-1]
  if BC[y] not in nome_paises:
    nome_paises.append(BC[y])
    qtd_nobel_paises.append(1)
  else:
    indice = nome_paises.index(BC[y])
    qtd_nobel_paises[indice] += 1
nome_paises[nome_paises.index('nan')] = 'Sem informação/Organização'
nome_paises[nome_paises.index('W&uuml;rttemberg')] = 'Württemberg'
paises = px.pie(values= qtd_nobel_paises, names= nome_paises)
paises = paises.update_layout(title={
    'text' : 'Prêmios Nobel por País de Origem',
    'y': 0.95,
    'x': 0.425
})
paises = paises.update_traces(textposition = 'inside', textinfo = 'percent+value+label')
paises.show()

"""###Ganhadores do Prêmio Nobel por Idade
O objetivo desse gráfico é mostrar a distribuição da idade dos ganhadores ao longo do tempo e identificar se existe alguma tendência ou padrão na idade dos ganhadores. Ele também pode ser usado para identificar se há uma idade específica em que as pessoas tendem a ganhar o prêmio e quais idades são as mais representativas.
"""

ano = []
dataNasc = []
for a in df:
  ano.append(a[0])
  dataNasc.append(a[8])
idade_organizando = []
for c in range(len(dataNasc)):
  if isinstance(dataNasc[c], float) == False :
    if int(dataNasc[c][5:7]) == 12 and int(dataNasc[c][8:10]) > 10: #data que ocorre o nobel: 10 de Dezembro // 1852-12-22  
      idade_organizando.append(int(ano[c]) - int(dataNasc[c][0:4]) - 1)
    else:
      idade_organizando.append(int(ano[c]) - int(dataNasc[c][0:4]))
idade_organizando = sorted(idade_organizando)
index = 0
idades = []
contador = 0
idades_contador = []
for idade_bruta in range(idade_organizando[-1]+1):
    idades.append(idade_bruta)
    while index < len(idade_organizando) and idade_organizando[index] == idade_bruta:
        contador += 1 
        index += 1
    idades_contador.append(contador)
    contador = 0
fig2 = px.bar(x = idades, y = idades_contador, labels= {
    'x': 'Idade',
    'y': 'Ganhadores'
    })
fig2 = fig2.update_layout(title={
    'text' : 'Ganhadores do Prêmio Nobel por Idade',
    'y': 0.9,
    'x': 0.5
})
fig2.show()

"""###Gênero dos Ganhadores por Categoria
Esse gráfico serve para mostrar a distribuição dos prêmios entre diferentes gêneros e categorias e identificar se existe alguma desproporção ou tendência na premiação. Ele também pode ser usado para identificar tendências e padrões na distribuição de prêmios entre diferentes gêneros e categorias.
"""

sexo = []
categoria = []
for a in df:
  sexo.append(a[11])
  categoria.append(a[1])
homem = [0, 0, 0, 0, 0, 0, 0] 
mulher = [0, 0, 0, 0, 0, 0, 0]
cat = ['Total','Chemistry', 'Literature', 'Medicine', 'Peace', 'Physics', 'Economics']
for i in range(len(sexo)):
  if isinstance(sexo[i], float): 
    continue
  if sexo[i] == 'Male':
    homem[0] += 1
    homem[cat.index(categoria[i])] += 1 
  else:
    mulher[0] += 1
    mulher[cat.index(categoria[i])] += 1     
categorias = ['Quimica', 'Literatura', 'Medicina', 'Paz', 'Fisica', 'Economia']
fig4 = px.bar()
fig4.add_trace(go.Bar(x=homem[1:7], y=categorias, name='Homem', orientation='h'))  
fig4.add_trace(go.Bar(x=mulher[1:7], y=categorias, name='Mulher', orientation='h'))
fig4.update_layout(barmode='stack') 
fig4.update_layout(title={
    'text' : 'Gênero dos Ganhadores por Categoria',
    'y': 0.91,
    'x': 0.5
})
fig5 = px.pie(values= [mulher[0], homem[0]], names= ['Mulheres', 'Homens'])
fig5 = fig5.update_traces(textposition = 'outside', textinfo = 'percent+value+label')
fig4.show()
fig5.show()

"""##Dashboard

"""
import pandas as pd
from jupyter_dash import JupyterDash
from dash import dcc, html, Dash, Input, Output
import plotly.express as px
import plotly.io as pio
import statistics

periodo = ['Geral','1901-1909','1910-1919','1920-1929', '1930-1939','1940-1949', '1950-1959','1960-1969', '1970-1979', '1980-1989','1990-1999', '2000-2009', '2010-2016']
anos1= ['Todos os anos'] 
for i in range(len(year)): 
  if year[i] not in anos1:
    anos1.append(year[i])
categorias_dash1 = ['Total', 'Condecoradas ao longo dos anos'] + categorias
app = JupyterDash(__name__)
app.layout = html.Div(
    children=[
        html.H1(children='Analise Prêmios Nobel',style={'textAlign': 'center'}),
        html.H2(children='O objetivo desse trabalho é analisar informações sobre os indivíduos e instituições que ganharam os prêmios do Nobel ao longo do tempo.',style={'textAlign': 'center'}),
        html.H1(children='Gráfico 1:'),
        html.H3(children='Selecione um ano para acessar as categorias que ganharam o prêmio Nobel em um ano específico:'),
        dcc.Dropdown(
            anos1,
            value= 'Todos os anos',
            id= 'lista-de-anos'
        ),
        html.H3(id='texto-anos'),
        dcc.Graph(
            id='grafico-1',
        ),
        html.H1(children=('Gráfico 2:')),
        html.H3(children='Arraste o circulo para acompanhar o desenvolver dos paises dos ganhadores através dos anos'),
        dcc.Slider(1901, 2016, value = 1901, id='escolha_ano', marks=None, tooltip={"placement": "bottom", "always_visible": True}),
        dcc.Graph(
                    id = 'graph_paises',
                ),
        html.H1(children=('Gráfico 3:')),
        html.H3(children=('Escolha um período para analisarmos a média de idade dos ganhadores nele:')),
        dcc.Dropdown(
            periodo,
            id='idade',
            value= 'Geral'
        ),
        html.H3(id='texto-idades'),
        dcc.Graph(
            id= 'ganhadores-idade'
        ),
        html.H1(children=('Gráfico 4:')),
        html.H3(children=('Selecione uma categoria para analisa-la individualmente ou, se achar melhor verifique o gráfico de crescimento da presença de mulheres na premiação')),
        dcc.Dropdown(
            categorias_dash1,
            value = 'Total',
            id='escolha_categorias',
        ),
        dcc.Graph(
                    id = 'genero_ganhadores',
        )
    ],
    style={'font-family' : 'Sans-serif', 'margin-left' : 'calc((100% - 1020px) / 2', 'margin-right' : 'calc((100% - 1020px) / 2'}
    )

#Atualizando o gráfico1
categorias_dash = []
anos_dash = []
for i in df:
  anos_dash.append(i[0])
  categorias_dash.append(i[1])
@app.callback(
    Output('grafico-1', 'figure'),
    Input('lista-de-anos', 'value')
)
def update_output(value):
  if value == 'Todos os anos':
    dash = fig8
  else:
    conta_categorias = [0,0,0,0,0,0]
    cat = ['Chemistry', 'Literature', 'Medicine', 'Peace', 'Physics', 'Economics']
    cat2 = ['Quimica', 'Literatura', 'Medicina', 'Paz', 'Fisica', 'Economia']
    for i in range(len(anos_dash)):
      if anos_dash[i] == value:
        conta_categorias[cat.index(categorias_dash[i])] += 1
    dash = px.bar(x = cat2, y = conta_categorias, color= ['Quimica', 'Literatura', 'Medicina', 'Paz', 'Fisica', 'Economia'], labels={'x':'Categorias','y':'Quantidade','color':'Categorias'})
    dash = dash.update_layout(title={'text' : 'Categorias Vencedoras por Ano', 'y': 0.9, 'x': 0.5})
  return dash

#Atualizando texto do grafico 1
@app.callback(
    Output('texto-anos', 'children'),
    Input('lista-de-anos', 'value')
)
def update_output(value):
  if value == 'Todos os anos':
    texto = 'Você está vendo o gráfico para todos os anos.'
  else:
    texto = f'Você está vendo a quantidade de prêmios para cada categoria no ano de {value}.'
  return texto
  
#Atualizando o gráfico 2
@app.callback(
    Output('graph_paises', 'figure'),
    Input('escolha_ano', 'value')
)
def update_output(value):
  ano_maximo = int(value)
  nome_paises = []
  qtd_nobel_paises = []
  for y in range(total):
    if int(df[y][0]) > ano_maximo:
      break
    if isinstance(BC[y], float):
      BC[y] = str(BC[y])
    if "(" in BC[y]:      #Exemplo: Prussia (Germany)
      BC[y] = BC[y][:BC[y].index('(')-1]
    if BC[y] not in nome_paises:
      nome_paises.append(BC[y])
      qtd_nobel_paises.append(1)
    else:
      indice = nome_paises.index(BC[y])
      qtd_nobel_paises[indice] += 1
  if 'nan' in nome_paises:
    nome_paises[nome_paises.index('nan')] = 'Sem informação/Organização'
  if 'W&uuml;rttemberg' in nome_paises:
    nome_paises[nome_paises.index('W&uuml;rttemberg')] = 'Württemberg'
  dash1 = px.pie(values= qtd_nobel_paises, names= nome_paises)
  dash1 = dash1.update_layout(title={
      'text' : 'Prêmios Nobel por País de Origem Através dos Anos',
      'y': 0.95,
      'x': 0.48
  })
  dash1 = dash1.update_traces(textposition = 'inside', textinfo = 'percent+value+label')
  return dash1

#Atualizando o gráfico 3
@app.callback(
    Output('ganhadores-idade', 'figure'),
    Input("idade", "value"), 
)
def update_output(value):
  if value == 'Geral':
    ganhadores_idade = fig2
  else:
    ano_inicial = int(value[0:4])
    ano_final = int(value[5:9])
    periodo_ano = []
    while ano_inicial <= ano_final:
      periodo_ano.append(ano_inicial)
      ano_inicial += 1
    ano = []
    dataNasc = []
    for a in df:
      ano.append(a[0])
      dataNasc.append(a[8])
    idade_organizando = []
    anos_organizados = []
    for c in range(len(dataNasc)):
      if isinstance(dataNasc[c], float) == False :
        if int(dataNasc[c][5:7]) == 12 and int(dataNasc[c][8:10]) > 10: #data que ocorre o nobel: 10 de Dezembro // 1852-12-22  
          idade_organizando.append(int(ano[c]) - int(dataNasc[c][0:4]) - 1)
          anos_organizados.append(ano[c])
        else:
          idade_organizando.append(int(ano[c]) - int(dataNasc[c][0:4]))
          anos_organizados.append(ano[c])
    media_idade = []
    for i in range(len(periodo_ano)):
      mediador = []
      for j in range(len(anos_organizados)):
        if periodo_ano[i] == anos_organizados[j]:
          mediador.append(idade_organizando[j])
      if len(mediador) == 0:
        media_idade.append(0)
      else:
        media_idade.append(int(statistics.mean(mediador)))
    periodo_ano = list(map(str,periodo_ano))
    ganhadores_idade = px.bar(x = periodo_ano, y= media_idade, labels={'x':'Anos','y':'Média de idade'})
    ganhadores_idade = ganhadores_idade.update_layout(title={'text' : 'Média de Idade dos Ganhadores por ano', 'y': 0.9, 'x': 0.5})
  return ganhadores_idade

#Atualizando Texto do gráfico 3
@app.callback(
    Output('texto-idades', 'children'),
    Input('idade', 'value')
)
def update_output(value):
  if value == 'Geral':
    texto = 'Você está vendo o gráfico Geral.'
  else:
    texto = f'Você está vendo a média de idade dos ganhadores no período {value}.'
  return texto

#Atualizando o Gráfico 4
@app.callback(
  Output('genero_ganhadores', 'figure'),
  Input('escolha_categorias', 'value') 
)
def uptade_output(value):
  if value == 'Total':
    dash3 = fig4
  elif value == 'Condecoradas ao longo dos anos':
    ano3 = []
    contador_mulheres = []
    contador = 0
    percorre = df[0][0]
    for i in df:
      if i[0] != percorre:
        contador_mulheres.append(contador)
      if i[0] not in ano3:
        ano3.append(i[0])
        percorre = i[0]
      if i[11] == 'Female':
        contador += 1
    contador_mulheres.append(contador)
    dash3 = px.line(df, x=ano3, y=contador_mulheres, labels={'x':'Anos','y':'Condecoradas'})
  else:
    dash3 = px.pie(values= [mulher[categorias.index(value) + 1], homem[categorias.index(value) + 1]], names= ['Mulheres', 'Homens'])
    dash3 = dash3.update_traces(textposition = 'outside', textinfo = 'percent+value+label')
    dash3 = dash3.update_layout(title={'text' : value, 'y': 0.95, 'x': 0.2})
  return dash3

app.run_server(mode = "external")
