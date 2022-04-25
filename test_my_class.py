'''
Created on Apr 21, 2022

@author: mlagatuz

#resource = '/v2/accounts/' + account_id + '/transactions' 
#resource = '/v2/accounts/' + account_id

'''
import json, os
from crypto_client import CryptoClient

EXCHANGE = 'CBP'
api_key = os.getenv(f'{EXCHANGE}_API_KEY')
api_secret = os.getenv(f'{EXCHANGE}_API_SECRET')
api_version = '2021-03-20' if EXCHANGE == 'CB' else None
api_passphrase = os.getenv('CBP_API_PASSPHRASE') if EXCHANGE == 'CBP' else None

base_url = 'https://api.exchange.coinbase.com' if EXCHANGE == 'CBP' else 'https://api.coinbase.com'
client = CryptoClient(api_key, api_secret, base_url, EXCHANGE, api_version, api_passphrase)

account_id = os.getenv(f'{EXCHANGE}_BTC_ACCOUNT_ID')
relative_path = '/accounts/' + account_id if EXCHANGE == 'CBP' else '/v2/accounts/' + account_id
body = ''
method = 'GET'

res = client.req(method, relative_path, body)
res_json = res.json()
btc_account_as_json_string = json.dumps(res_json, indent=4)
print(btc_account_as_json_string)
