df = pd.read_excel('Arquivo.xlxs', index=False) #Leitura de xlsx
df = pd.read_csv('Arquivo.csv') #Leitura csv

df.drop(df.columns[[0]], axis=1, inplace=True #Exclusão coluna
df.drop(df.index[0:6], inplace=True) #Exclusão linha
df.rename(columns={df.columns[0]:"coluna_01"}, inplace=True) #Renomear coluna
df.dop_duplicates() #Remover duplicações
df.dropna() #Remoção NaN
df['coluna01'].astype(int) #Trocar para int
df.sort_values('coluna_01') #Ordenar
df.sort_values(by=['coluna_02'], ascending=False) #Ordenar em ordem decrescente
df['coluna_01'] = pd.to_datetime(df['coluna_01'], format='%d/%m/%Y') #Passar para datetime
df = pd.concat([df01, df02], axis=1) #Concatenação entre DataFrames
df.info() #Infos do DataFrame
df.shape() #Observações e variáveis
df['coluna_01'].sum() #Somatório
df['coluna_01'].mean() #Média
df = df.loc[df['coluna_01'] == 1] #Acessar valores no DataFrame
df = df.groupby('coluna_01'['coluna_03'].sum()/60
df.to_excel('Arquivo_Pronto.xlsx', index=False) #Transformar Dataframe em .xlsx
df = pd.merge(df1, df2, on="coluna_01", how="left") #Combinação de dois DataFrames

#Gráfico de barras
fig = px.bar(df,
             x='coluna_01',
             y='coluna_02',
             color='coluna_03',
             color_discrete_sequence=px.colors.qualitative.***,
             labels={'coluna_01':'Coluna 01', 'coluna_02':'Coluna 02'},
             height=400)
fig.update_xaxes(title='Título de X')
fig.update_yaxes(title='Título de Y')
fig.update_layout(title_text='Gráfico de Barras')

##Modelo de regressão e correlação
correlacao = df.corr()
import statsmodels.api as sm
y = df.coluna_01
x = sm.add_constant(df.coluna_02) #criação de 2 variáveis para a passar a função
y.head()
x.head()
regressao = sm.OLS(y,x).fit()
print(regressao.summary())
df['y_previsto']=regressao.predict()

##Gráfico de dispersão:
fig = px.scatter(df,
             x='coluna_01',
             y='coluna_02',
             trendline='ols') #linha de tendência
fig.update_layout(title_text="Gráfico de Dispersão",
                  xaxis_title="Título de X",
                  yaxis_title="Título de Y")
##Dash:
app = dash.Dash(__nam   e__, external_stylesheets=[dbc.themes.TEMA])
app.layout = dbc.Container([
    dbc.Row([
        dbc.col([
            html.H2("", style={"margin-top":"10px"}),
            html.P(""),
            html.Div(children=[html.Strong('Arquivo 001'), ' está completo.'], style={"margin-bottom":"10px"}), #negrito
            ]),
          ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="grafico", figure=fig)
        ], md=6, style={"margin-top":"10px"})
    ]),
])
app.run_server(port=9090, host='198.160.50.200')
         
##Funções:
def atribuir_definicao(row):
    if row['nome'] in ['A', 'B', 'C']:
        return 'Letras'
    elif row['nome'] in ['1', '2', '3']:
        return 'Números'
    else:
        return None
df['definicao'] = df.apply(atribuir_definicao, axis=1) #Atribuir a função no df    
