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
    API client access to various exchanges
    Coinbase (CB), Coinbase Pro (CBP), KuCoin (KC)
    
    Full API documentation found in the README markdown
    '''

    def __init__(self, api_key, api_secret, base_url, exchange, api_version, api_passphrase):
        '''
        api_secret: <insert differences between CB and CBP/KC>
        api_passphrase: required for CBP/KC, NOT required for CB
        '''
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.exchange = exchange.upper()
        self.api_version = api_version
        self.api_passphrase = api_passphrase
        
    def req(self, method, relative_path, body):
        '''
        Builds required headers for authentication
        '''
        # current unix timestamp (seconds for CB/CBP, milliseconds for KC)
        access_timestamp = str(int(time.time() * 1000)) if self.exchange == 'KC' else str(int(time.time()))
        message = '{}{}{}{}'.format(access_timestamp, method, relative_path, body)
        
        hmac_key = base64.b64decode(self.api_secret) if self.exchange == 'CBP' else self.api_secret.encode('utf-8')
        if (self.exchange == 'CBP' or self.exchange  == 'KC'):
            digest = hmac.new(hmac_key, message.encode('utf-8'), digestmod=hashlib.sha256).digest()
            signature = base64.b64encode(digest).decode('utf-8')
        else:
            signature = hmac.new(hmac_key, message.encode('utf-8'), hashlib.sha256).hexdigest()
        
        if self.exchange == 'KC':
            encrypted_passphrase = base64.b64encode(hmac.new(self.api_secret.encode('utf-8'),
                                                             self.api_passphrase.encode('utf-8'),
                                                             digestmod=hashlib.sha256).digest())
        
        header_prefix = 'CB' if self.exchange == 'CBP' else self.exchange
        header_access = 'ACCESS' if (self.exchange == 'CB' or self.exchange == 'CBP') else 'API'
        header_api_version = 'VERSION' if (self.exchange == 'CB' or self.exchange == 'CBP') else 'API-KEY-VERSION'
        headers = {
            'Content-Type': 'application/json',
            f'{header_prefix}-{header_access}-KEY': self.api_key,
            f'{header_prefix}-{header_access}-PASSPHRASE': encrypted_passphrase if self.exchange == 'KC' else self.api_passphrase,
            f'{header_prefix}-{header_access}-SIGN': signature,
            f'{header_prefix}-{header_access}-TIMESTAMP': access_timestamp,
            f'{header_prefix}-{header_api_version}': self.api_version
        }
        
        url = '{}{}'.format(self.base_url, relative_path)
        res = requests.get(url, headers=headers)
        return res