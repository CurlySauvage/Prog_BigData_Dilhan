
import dash_core_components as dcc
from dash import html
import plotly.express as px



from datasVehicules import processTotal, fusionDF

"""Valiables Page 1 Tipo   recrerrr un DF en ajoutant les données pour pivot """
fileV2017 = 'Datas/VEHICULOS_PARQUE_MOVIL_2017.csv'
fileV2018 = 'Datas/VEHICULOS_PARQUE_MOVIL_2018.csv'
fileV2019 = 'Datas/VEHICULOS_PARQUE_MOVIL_2019.csv'
fileV2020 = 'Datas/VEHICULOS_PARQUE_MOVIL_2020.csv'
fileV2021 = 'Datas/VEHICULOS_PARQUE_MOVIL_2021.csv'

dfV17 = processTotal(fileV2017,"2017")
dfV18 = processTotal(fileV2018,"2018")
dfV19 = processTotal(fileV2019,"2019")
dfV20 = processTotal(fileV2020,"2020")
dfV21 = processTotal(fileV2021,"2021")

dataframeTotal = fusionDF(dfV17, dfV18, dfV19, dfV20, dfV21)
print(dataframeTotal)


# Not used cuz in test , Blocked by concat atm need to concat without losing row values
groupEnergie=dataframeTotal.groupby(["Energie", "Date"])['Num']
dataEnergie = groupEnergie.size().reset_index(name='counts')
# repartion par type d'utilisation
groupUso21=dfV21.groupby(["Uso", "Date","Energie"])['Num']
dataUso21 = groupUso21.size().reset_index(name='counts')
# group by vehicule count
groupVeh21=dfV21.groupby(["Vehicule"])['Num']
dataVeh21 = groupVeh21.size().reset_index(name='counts')

groupVehEn21=dfV21.groupby(["Vehicule", "Energie"])['Num']
dataVehEn21 = groupVehEn21.size().reset_index(name='counts')






figureConsoTotal = px.bar(dataEnergie,x= "Energie", y= "counts", color="Date", barmode="group")
figureEnergieByVeh21 = px.bar(dataVehEn21,x= "Vehicule", y= "counts",color="Energie",  barmode="group")


figureEnergieByVehTotal = px.bar(dataEnergie,x= "Energie", y= "counts", color="Energie",  barmode="group")


#figureConsoUso = px.bar(dataUso21,x= "Energie", y= "counts", color="Date", barmode="group")
pieUso21 = px.pie(dataUso21, values='counts', names='Uso', title="Répartition movil par utilisation")
pieVeh21 = px.pie(dataVeh21, values='counts', names='Vehicule', title="Répartition par vehicule")





def pageTypeConso():
    return html.Div(children=[
    html.H1(children='El parque movil de la Ayu.. de Madrid'),
    html.Div(children='''
    Cette page regroupe les analyses sur le parc automobile de madrid
    
    '''),

    html.Div(children=[
        html.H5("Nombre de vehicule par type de consomation d'énergie"),
        dcc.Graph(
        id='test-graph',
        figure=figureConsoTotal
        ),
    ]),

        html.H2(children='Sobre el Ano 2021'),

        html.Div([
            html.Div([
                dcc.Graph(id='test-graph22',
                          figure=pieUso21)
            ], className="six columns"),
            html.Div([
                dcc.Graph(id='test-graph22',
                          figure=pieVeh21)
            ], className="six columns"),

        ], className="row"),

        html.Div(children=[
            dcc.Graph(
                id='test-graph',
                figure=figureEnergieByVeh21
            ),
        ]),
    ])



