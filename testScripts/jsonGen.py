import json
import datetime
from random import randint
import time


exampleData = {
    'time': '',
    'parkingLot': 4,
    'coordinates': '32.771685, -117.067002',
    'open': 154,
    'total': 580,
    'loadFactor': ''
}

def update_add(inc):
    exampleData['open'] = exampleData['open'] + inc
    log()

def update_minus(dec):
    exampleData['open'] = exampleData['open'] - dec
    log()

def random_sim():
    for x in range(0,30):
        time.sleep(10)
        update_add(randint(0, 20))
        update_minus(randint(0, 20))

def log():
    ctime = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    loadF = round(exampleData['open']/exampleData['total'], 2)
    exampleData['time'] = ctime
    exampleData['loadFactor'] = loadF
    json_str = json.dumps(exampleData)
    print(json_str)

print('Ready?')

random_sim()

