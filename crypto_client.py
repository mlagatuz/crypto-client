'''
Created on Apr 21, 2022

@author: mlagatuz

I wrote this class for myself to learn concepts:

- How classes are implemented in Python
- HTTP requests/responses
- message authentication (HMAC)
- API access to my own crypto accounts
'''
import time, hmac, hashlib, requests, base64

class CryptoClient(object):
    '''
    API client to access Coinbase (CB) and Coinbase Pro (CBP)
    
    Full API documentation found in the README markdown
    '''

    def __init__(self, api_key, api_secret, base_url, exchange, api_version, api_passphrase):
        '''
        api_secret: <insert differences between CB and CBP>
        api_passphrase: required for CBP, NOT required for CB
        '''
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.exchange = exchange.lower()
        self.api_version = api_version
        self.api_passphrase = api_passphrase
        
    def req(self, method, relative_path, body):
        '''
        Builds required headers for authentication
        '''
        # current unix timestamp (seconds)
        access_timestamp = str(time.time()) if self.exchange == 'cbp' else str(int(time.time()))
        message = '{}{}{}{}'.format(access_timestamp, method, relative_path, body)
        
        hmac_key = base64.b64decode(self.api_secret) if self.exchange == 'cbp' else self.api_secret.encode('utf-8')
        if self.exchange == 'cbp':
            digest = hmac.new(hmac_key, message.encode('utf-8'), digestmod=hashlib.sha256).digest()
            signature = base64.b64encode(digest).decode('utf-8')
        else:
            signature = hmac.new(hmac_key, message.encode('utf-8'), hashlib.sha256).hexdigest()
        
        headers = {
            'Content-Type': 'application/json',
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.api_passphrase,
            'CB-ACCESS-SIGN': signature,
            'CB-ACCESS-TIMESTAMP': access_timestamp,
            'CB-VERSION': self.api_version
        }
        
        url = '{}{}'.format(self.base_url, relative_path)
        res = requests.get(url, headers=headers)
        return res