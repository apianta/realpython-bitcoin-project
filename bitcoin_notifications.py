import requests
import time
from datetime import datetime

BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/ds0i-CGcZspuqcEm_AyRzA'

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

BITCOIN_PRICE_THRESHOLD = 10000  # Set this to whatever you like

def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        # format the date into a string: '24.02.2018 15:09'
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)

    return '<br>'.join(rows)

def main():
     bitcoin_history = []
     while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        # Send an emergency notification
        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)

        # Send a Telegram notification
        # Once we have 5 items in our bitcoin_history send an update
        if len(bitcoin_history) == 5:
            post_ifttt_webhook('bitcoin_price_update',
                               format_bitcoin_history(bitcoin_history))
            # Reset the history
            bitcoin_history = []

        # Sleep for 5 minutes
        # (For testing purposes you can set it to a lower number)
        time.sleep(24 * 60)

if __name__ == '__main__':
    main()
