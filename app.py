import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET # Import variables from config.py

# Configuring OAuth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Creating API object
api = tweepy.API(auth)

# Posting a tweet
try:
    api.update_status("Olivia.")
    print("Tweet sent.")
except tweepy.TweepyException as e:
    print(f"Error: {e}")
