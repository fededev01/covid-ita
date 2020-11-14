import requests
import json
import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

conf, tamp, mor, n_pos = [], [], [], [] 
for i in dati:
  conf.append(i["totale_casi"])
  tamp.append(i["tamponi"])
  mor.append(i["deceduti"])
  n_pos.append(i["nuovi_positivi"])

del conf[-1]
del n_pos[-1]
nuovi_morti = np.array([mor]) 
del mor[-1]
n_m = np.diff(nuovi_morti)
nuovi_m = n_m.reshape(len(conf), 1)

nuovi_tamponi = np.array([tamp]) 
del tamp[-1]
n_t = np.diff(nuovi_tamponi)
nuovi_t= n_t.reshape(len(conf), 1)

dates = pd.date_range('20200224', periods = len(mor))
df = pd.DataFrame(index = dates)
df['tamponi tot'] = tamp
df['casi tot'] = conf
df['morti tot'] = mor
df['nuovi positivi'] = n_pos
df['nuovi morti'] = nuovi_m
df['nuovi tamponi'] = nuovi_t 
 
fir = [i*100 for i in n_pos]
sec= nuovi_t

print(sec[0])
"""
ter = []
while len(fir)>1:
  ter.append(fir[0]/sec[0])
  del fir[0]
  del sec[0]
  if len(fir)==1:
    break

df['rapp pos/tamp'] = ter
print(df)
"""