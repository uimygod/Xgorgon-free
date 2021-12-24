import requests

url = 'https://xgtrial.herokuapp.com/trial/xgorgon'

data = {'INPUT_TIKTOK_URL_HERE'}

r = requests.post(url, data=data)

print(r.json())
