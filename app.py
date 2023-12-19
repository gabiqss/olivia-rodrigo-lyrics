import tweepy
from config import *
import random
from lyrics import lyrics

# lista de letras
lyrics = lyrics

def lambda_handler(event, context):

    # seleciona um índice aleatório
    indice_selecionado = random.randint(0, len(lyrics) - 1)
    
    # autenticação com twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    client = tweepy.API(auth)
    
    # texto do tweet
    texto_do_tweet = lyrics[indice_selecionado]
    
    # postar!
    client.update_status(status=texto_do_tweet)
