import requests
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
response = requests.get(bitcoin_api_url)
response_json = response.json()
type(response_json)
response_json[0]

# curl -X POST https://maker.ifttt.com/trigger/test_alert/with/key/ds0i-CGcZspuqcEm_AyRzA