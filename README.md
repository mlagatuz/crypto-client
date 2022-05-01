# crypto-client

This is my learning journey wth Python, API's and crypto exchanges.

I've created a client that's able to access my crypto transactions on various exchanges (currently Coinbase, Coinbase Pro, and KuCoin).  

# Documentation

I find Coinbase's API documentation to be quite **messy**, not as intuitive, and **all over the place**! On the contrary, Twitter's documentation is great and leads to an easy onramp for learning. KuCoin follows suit and is on par with details and navigational ease.

I've aggregated the documentation to the [References Section](#references) to help those who are learning API's usage and development, Python, authentication, etc ... this really is for myself, serving as notes during my learning journey!

# Development Environment

My Integrated Development Environment (IDE) of choice is **Eclipse** and I'm using the **PyDev** module for my Python Development.

Run --> Run Configurations --> Select your Python run configuration --> Environment 

Here you can add your environment variables, as if you're running on the command line (terminal)

# Notes

I noticed the API Secret Keys are in different formats between Coinbase and Coinbase Pro

```
abcabcabcabcabcxxxxxxxxxxxxxxx # API Secret Coinbase
```
```
xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxxxxxxxxxxxxxxxxxxxxxxxxxxxx== # API Secret Coinbase Pro
```

It appears the secret key for CB has already been base-64 decoded, whereas with CBP, you'll first need to base-64 decode the key

```
hmac_key = base64.b64decode(self.api_secret) if self.exchange == 'CBP' else self.api_secret.encode('utf-8')
if (self.exchange == 'CBP' or self.exchange  == 'KC'):
	digest = hmac.new(hmac_key, message.encode('utf-8'), digestmod=hashlib.sha256).digest()
	signature = base64.b64encode(digest).decode('utf-8')
else:
	signature = hmac.new(hmac_key, message.encode('utf-8'), hashlib.sha256).hexdigest()
```

# References

**Coinbase**

[Coinbase Developers Reference] (https://developers.coinbase.com/)

[Coinbase API Reference] (https://developers.coinbase.com/api/v2)

**Coinbase Pro**

[Coinbase Pro Developers Reference] (https://docs.cloud.coinbase.com/exchange/docs/welcome)

[Coinbase Pro API Reference] (https://docs.cloud.coinbase.com/exchange/reference/exchangerestapi_getaccounts)

**KuCoin**

[KuCoin API Reference] (https://docs.kucoin.com/#general)

[KuCoin Authentication] (https://docs.kucoin.com/#authentication)
