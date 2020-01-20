import requests
# Make sure that your key is in the URL
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/with/key/ds0i-CGcZspuqcEm_AyRzA'
requests.post(ifttt_webhook_url)