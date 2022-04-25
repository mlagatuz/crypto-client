'''
Created on Apr 21, 2022

@author: mlagatuz

#resource = '/v2/accounts/' + account_id + '/transactions' 
#resource = '/v2/accounts/' + account_id

'''
import json, os
from crypto_client import CryptoClient

EXCHANGE = 'KC'
api_key = os.getenv(f'{EXCHANGE}_API_KEY')
api_secret = os.getenv(f'{EXCHANGE}_API_SECRET')
api_dict = {
            'CB':'2021-03-20',
            'CBP':None,
            'KC':'2'
            }
api_version = api_dict[EXCHANGE]
api_passphrase = os.getenv(f'{EXCHANGE}_API_PASSPHRASE') if (EXCHANGE == 'CBP' or EXCHANGE == 'KC') else None

url_dict = {
            'CB':'https://api.coinbase.com',
            'CBP':'https://api.exchange.coinbase.com',
            'KC':'https://api.kucoin.com'
            }
base_url = url_dict[EXCHANGE]

client = CryptoClient(api_key, api_secret, base_url, EXCHANGE, api_version, api_passphrase)

account_id = os.getenv(f'{EXCHANGE}_BTC_ACCOUNT_ID')
accounts_path_dict = {
                    'CB':'/v2/accounts/',
                    'CBP':'/accounts/',
                    'KC':f'/api/v1/accounts'}
relative_path = accounts_path_dict[EXCHANGE] + account_id
body = ''
method = 'GET'

res = client.req(method, relative_path, body)
res_json = res.json()
btc_account_as_json_string = json.dumps(res_json, indent=4)
print(btc_account_as_json_string)
