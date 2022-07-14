"""
Interacting with lists as a two-dimensional table
"""
import pprint as pp

STOCKS= [["date","open","high","low","close","volume", "symbol"],
["1/3/2022",39.69,41.22,38.79,40.91,24232729,"AABA"],
["1/4/2022",41.22,41.9,40.77,40.97,20553479,"AABA"],
["1/5/2022",40.93,41.73,40.85,41.53,12829610,"AABA"],
["1/6/2006",42.88,43.57,42.8,43.21,29422828,"AABA"],
["1/7/2006",43.1,43.66,42.82,43.42,16268338,"AABA"],
["1/10/2022",42.96,43.34,42.34,42.98,16288580,"AABA"],
["1/11/2022",42.19,42.31,41.72,41.87,26192772,"AABA"],
["1/12/2022",41.92,41.99,40.76,40.89,18921686,"AABA"],
["1/13/2022",41,41.08,39.62,39.9,30966185,"AABA"],
["1/14/2022",39.09,40.39,38.96,40.11,42429911,"AABA"]
]

OPEN_COLUMN = 1
VOLUME_COLUMN = 5
opens =  []
volumes = []
for i in range(1,len(STOCKS)):
    row = STOCKS[i]
    opens.append(row[OPEN_COLUMN])
    volumes.append(STOCKS[i][VOLUME_COLUMN])

print ("OPENS:", opens)
print ("VOLUMES", volumes)

TWENTY_MILLION = 20000000 # 20 million
data = []
for i in range(1, len(STOCKS)):
    if STOCKS[i][VOLUME_COLUMN] > TWENTY_MILLION:
        data.append(STOCKS[i])

print(data)
pp.pprint(data)  # make the data look pretty

data = [ STOCKS[i]  for i in range(1, len(STOCKS)) if STOCKS[i][VOLUME_COLUMN] > TWENTY_MILLION ]

pp.pprint(data)
