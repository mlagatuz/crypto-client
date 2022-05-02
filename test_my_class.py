'''
Created on Apr 21, 2022

@author: mlagatuz

'''
import json, os
from crypto_client import CryptoClient

EXCHANGES = {'Coinbase': 'CB', 
             'Coinbase Pro':'CBP',
             'KuCoin':'KC',
             'Sandbox Coinbase Pro':'SB_CBP'}

CURRENT_EXCHANGE = EXCHANGES['Coinbase']
api_key = os.getenv(f'{CURRENT_EXCHANGE}_API_KEY')
api_secret = os.getenv(f'{CURRENT_EXCHANGE}_API_SECRET')
api_dict = {
            'CB':'2021-03-20',
            'CBP':None,
            'KC':'2',
            'SB_CBP':None
            }
api_version = api_dict[CURRENT_EXCHANGE]
api_passphrase = os.getenv(f'{CURRENT_EXCHANGE}_API_PASSPHRASE') if (CURRENT_EXCHANGE == 'CBP' or CURRENT_EXCHANGE == 'KC' or CURRENT_EXCHANGE == 'SB_CBP') else None

url_dict = {
            'CB':'https://api.coinbase.com',
            'CBP':'https://api.exchange.coinbase.com',
            'KC':'https://api.kucoin.com',
            'SB_CBP':'https://api-public.sandbox.exchange.coinbase.com'
            }
base_url = url_dict[CURRENT_EXCHANGE]
client = CryptoClient(api_key, api_secret, base_url, CURRENT_EXCHANGE, api_version, api_passphrase)

account_id = os.getenv(f'{CURRENT_EXCHANGE}_BTC_ACCOUNT_ID')
account_resourse_path = {
                    'CB':'/v2/accounts',
                    'CBP':'/accounts/',
                    'KC':f'/api/v1/accounts',
                    'SB_CBP': '/accounts'}
relative_path = account_resourse_path[CURRENT_EXCHANGE] + '/'+ account_id
#relative_path = account_resourse_path[CURRENT_EXCHANGE]
body = ''
method = 'GET'

url = '{}{}'.format(base_url, relative_path)

res = client.req(method, relative_path, body)
#res = client.get_accounts()

#res = client.get_account(account_id)
res_json = res.json()
res_as_json_string = json.dumps(res_json, indent=4)
print(res_as_json_string)