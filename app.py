import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Configurar a autenticação
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Criar uma instância da API
api = tweepy.API(auth)

# Postar um tweet
try:
    api.update_status("Olivia.")
    print("Tweet enviado com sucesso!")
except tweepy.TweepyException as e:
    print(f"Erro ao twittar: {e}")
