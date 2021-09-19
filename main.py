import time
import requests

todate = int(time.time())
fromdate = int(todate - 48 * 60 * 60)
params = {'fromdate': fromdate,
          'todate': todate,
          'order': 'desc',
          'sort': 'activity',
          'tagged': 'Python',
          'site': 'stackoverflow'
          }
url = 'https://api.stackexchange.com/2.3/questions'
response = requests.get(url, params=params)
for item in response.json().get('items'):
    print(item.get('title'))




