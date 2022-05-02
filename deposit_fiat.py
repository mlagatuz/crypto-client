'''
Created on May 1, 2022

@author: mlagatuz
'''
import json, os, requests, time, hmac, base64, hashlib

api_key = '<INSERT_API_KEY>'
api_secret = '<INSERT_API_SECRET>'
api_passphrase = '<INSERT_API_PASSPHRASE>'

base_url = 'https://api-public.sandbox.exchange.coinbase.com'
print(f'base_url: {base_url}')

#relative_path = '/accounts'
#relative_path = '/payment-methods'
relative_path = '/deposits/payment-method'

#body = ''
payload = {
    'profile_id': '<INSERT_PROFILE_ID>',
    'amount': '10',
    'payment_method_id': '<INSERT_PAYMENT_METHOD_ID>',
    'currency': 'USD'
}
body = json.dumps(payload)
#method = 'GET'
method = 'POST'

access_timestamp = str(int(time.time()))
message = '{}{}{}{}'.format(access_timestamp, method, relative_path, body)
print(f'message: {message}')
        
hmac_key = base64.b64decode(api_secret)
digest = hmac.new(hmac_key, message.encode('utf-8'), digestmod=hashlib.sha256).digest()
signature = base64.b64encode(digest).decode('utf-8')

headers = {
    'Content-Type': 'application/json',
    'CB-ACCESS-KEY': api_key,
    'CB-ACCESS-PASSPHRASE': api_passphrase,
    'CB-ACCESS-SIGN': signature,
    'CB-ACCESS-TIMESTAMP': access_timestamp,
}

url = '{}{}'.format(base_url, relative_path)
print(f'url: {url}')
#res = requests.get(url, headers=headers)
res = requests.post(url, body, headers=headers)
print(f'{res}')
#print(f'res.json: {res.json()}')

res_json = res.json()
res_as_json_string = json.dumps(res_json, indent=4)
print(res_as_json_string)
