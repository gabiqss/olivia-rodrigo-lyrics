import os
import sys
# Adiciona o diretório do script ao PATH
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.extend([current_dir, parent_dir])
print("sys.path:", sys.path)
print("current_dir:", current_dir)
from config import CONSUMER_KEY, CONSUMER_SECRET, PIN
from requests_oauthlib import OAuth1Session
import json
import time
import random
from lyrics import lyrics

consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET

lyrics = lyrics

intervalo_entre_postagens = 2 * 60 * 60
historico_indices = []

# Código para obter os tokens de acesso
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print("There may have been an issue with the consumer_key or consumer_secret you entered.")

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)
print("Got OAuth token secret: %s" % resource_owner_secret)

# Obter autorização
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Obter o token de acesso
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens.get("oauth_token")
access_token_secret = oauth_tokens.get("oauth_token_secret")

while True:
    # Seleciona aleatoriamente um índice da lista de letras
    while True:
        indice_selecionado = random.randint(0, len(lyrics) - 1)
        # Verifica se o índice não está no histórico dos últimos 5 índices
        if indice_selecionado not in historico_indices:
            break

    # Adiciona o índice selecionado ao histórico
    historico_indices.append(indice_selecionado)
    # Mantém apenas os últimos 50 índices no histórico
    historico_indices = historico_indices[-50:]

    texto_do_tweet = lyrics[indice_selecionado]

    # Código para fazer a postagem
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    payload = {"text": texto_do_tweet}
    response = oauth.post("https://api.twitter.com/2/tweets", json=payload)

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print(f"Tweet enviado com sucesso: {texto_do_tweet}")

    # Aguarda o intervalo antes de fazer a próxima postagem
    time.sleep(intervalo_entre_postagens)
