from turtle import color
import numpy as np
from fcmeans import FCM
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score

    
results = pd.read_csv('./formula-1-race-data/results.csv')
races = pd.read_csv('./formula-1-race-data/races.csv')
circuits = pd.read_csv('./formula-1-race-data/circuits.csv')
constructors = pd.read_csv('./formula-1-race-data/constructors.csv')
drivers = pd.read_csv('./formula-1-race-data/drivers.csv')

#df_pit_stops = pd.read_csv('./venv/formula-1-race-data/pit_stops.csv')
lapTimes = pd.read_csv('./formula-1-race-data/lap_times.csv')

circuits = circuits.rename(columns={'name':'circuitName','location':'circuitLocation','country':'circuitCountry','url':'circuitUrl'})
drivers = drivers.rename(columns={'number':'driverNumber','nationality':'driverNationality','url':'driverUrl'})
drivers['driverName'] = drivers['forename']+' '+drivers['surname']
constructors = constructors.rename(columns={'name':'constructorName','nationality':'constructorNationality','url':'constructorUrl'})

races = races.rename(columns={'year':'raceYear','name':'raceName','date':'raceDate','time':'raceTime','url':'raceUrl','round':'raceRound'})
lapTimes = lapTimes.rename(columns={'time':'lapTime','position':'lapPosition','milliseconds':'lapMilliseconds'})
lapTimes['lapSeconds'] = lapTimes['lapMilliseconds'].apply(lambda x: x/1000)

resultsAnalysis = pd.merge(results,races,left_on='raceId',right_on='raceId',how='left')
resultsAnalysis = pd.merge(resultsAnalysis,circuits,left_on='circuitId',right_index=True,how='left')
resultsAnalysis = pd.merge(resultsAnalysis,constructors,left_on='constructorId',right_index=True,how='left')
resultsAnalysis = pd.merge(resultsAnalysis,drivers,left_on='driverId',right_index=True,how='left')
lapTimesAnalysis = pd.merge(lapTimes,races,left_on='raceId',right_on='raceId',how='left')
lapTimesAnalysis = pd.merge(lapTimesAnalysis,resultsAnalysis,left_on=['raceId','driverId','raceYear','raceRound','circuitId','raceName','raceUrl'],right_on=['raceId','driverId','raceYear','raceRound','circuitId','raceName','raceUrl'],how='left')