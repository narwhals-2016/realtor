from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

"""
how auth and client objects are made:

auth = Oauth1Authenticator(
    consumer_key=YOUR_CONSUMER_KEY,
    consumer_secret=YOUR_CONSUMER_SECRET,
    token=YOUR_TOKEN,
    token_secret=YOUR_TOKEN_SECRET
)

client = Client(auth)
"""
# read API keys
with io.open('yelp_config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)