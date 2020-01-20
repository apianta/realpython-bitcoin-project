import requests
import time
from datetime import datetime

def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    # convert the price to a floating point number
    return float(response_json[0]['price_usd'])

def post_ifttt_webhook(event, value):
    # The payload that will be sent to IFTTT service
    data = {'value1' : value}
    # inserts our desired event
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    # Sends a HTTP POST request to the webhook URL
    requests.post(ifttt_event_url, json = data)

def main():
    pass

if __name__ == '__main__':
    main()