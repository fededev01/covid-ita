import requests
import json
import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt 

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

conf = [] 
tamp = []
mor = []
for i in dati:
  conf.append(i["totale-casi"])
  tamp.append(i["tamponi"])
  mor.append(i["deceduti"])

#cambiare nome variabili
cinq = np.array([mor])
sei = mor[1: len(mor)]
sei.append(mor[-1])
set = np.array([sei])
nuovi_morti = set - cinq

otto = np.array([tamp])
nove = tamp[1: len(tamp)]
nove.append(tamp[-1])
dieci = np.array([nove])
nuovi_tamponi = dieci - otto
#fine variabili da cambiare

nuovi_m = nuovi_morti.reshape(len(mor), 1)
nuovi_t = nuovi_tamponi.reshape(len(mor), 1)

dates = pd.date_range('4', periods = len(tamp))
df = pd.DataFrame(index = dates)
df['tamponi'] = tamp
df['confermati'] = conf
df['deceduti'] = mor
df['nuovi morti'] = nuovi_m
df['nuovi tamponi'] = nuovi_t    