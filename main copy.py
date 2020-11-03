import requests
import json
import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

conf = [] 
tamp = []
mor = []
n_pos= []
for i in dati:
  conf.append(i["totale_casi"])
  tamp.append(i["tamponi"])
  mor.append(i["deceduti"])
  n_pos.append(i["nuovi_positivi"])


nuovi_morti = np.array([mor]) 
n_m = np.diff(nuovi_morti)
nuovi_m = n_m.reshape(len(conf), 1)

nuovi_tamponi = np.array([tamp]) 
n_t = np.diff(nuovi_tamponi)
nuovi_t= n_t.reshape(len(conf), 1)

dates = pd.date_range('20200224', periods = len(mor))
df = pd.DataFrame(index = dates)
df['tamponi'] = tamp
df['confermati'] = conf
df['deceduti'] = mor
df['nuovi morti'] = nuovi_m
df['nuovi tamponi'] = nuovi_t  


ter = []
fir = np.array([n_pos])
sec = np.divide(nuovi_t, n_pos)


#llll = np.dot(media, 100)

#ter = [i * 100 for i in n_pos]

#perc = np.array([ter])
df['prova'] = sec[0]
print(df)