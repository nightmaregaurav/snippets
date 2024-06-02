import requests
import json

from requests.structures import CaseInsensitiveDict


url = "https://tms07.nepsetms.com.np/tmsapi/rtApi/ws/marketwatch/157684"

headers = CaseInsensitiveDict()
headers["Content-Type"] = 'application/json'
headers["Connection"] = 'keep-alive'
# all headers here

resp = requests.get(url, headers=headers)
output = json.loads(resp.text)
try:
  market_data = output['payload']['data']
except Exception:
  print("Session Expired, change Cookie, X-XSRF-TOKEN, and Host-Session-Id")
  exit()

for data in market_data:
  symbol = data['security']['symbol']
  ftwh = data['security']['fiftyTwoWeekhigh']
  ftwl = data['security']['fiftyTwoWeekLow']
  
  del(data['security'])
  
  data['symbol'] = symbol
  data['fiftyTwoWeekhigh'] = ftwh
  data['fiftyTwoWeekLow'] = ftwl

# print(market_data)
import pandas as pd

df = pd.DataFrame(market_data)

required_header = ['symbol', 'ltp', 'lastTradedTime', 'change', 'changePercentage']
# main_header = df.columns.values

# table_header = required_header + [item for item in main_header if item not in required_header]

table_header = required_header

print(df[table_header])
