import requests
import config
import charges

# Authentication
url = 'https://api.commerce.coinbase.com/checkouts'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8',
'X-CC-Api-Key': config.api_key,'X-CC-Version': '2018-03-22'}
r = requests.get(url, headers=headers)

print(r.text)
print(r)
print("Successfully authed\n")

# Posting a charge
url = 'https://api.commerce.coinbase.com/charges'
payload = charges.payload
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8',
'X-CC-Api-Key': config.api_key,'X-CC-Version': '2018-03-22'}
r = requests.post(url, data=payload, headers=headers)

print(r.text)
print(r)
print("Posted a charge!")
