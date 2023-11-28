import tweepy
from config import BEARER_TOKEN

# Configurar a API do Twitter usando OAuth 2.0 (Bearer Token)
auth = tweepy.AppAuthHandler(BEARER_TOKEN, True)
api = tweepy.API(auth)

# Criar um tweet usando a API v2
tweet_text = "Olivia."
tweet_params = {"status": tweet_text}
response = api.request("POST", "tweets", params=tweet_params)
print(response.json())
