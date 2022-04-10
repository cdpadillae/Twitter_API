import tweepy
import configparser

#Read credential

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#Authentication

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Posting a tweet

status = "Me: I'm not going to use twitter anymore. \n Also me: Let's tweet from the console."
api.update_status(status=status)


