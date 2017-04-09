import tweepy
from textblob import TextBlob
import time

consumer_key = 'h7jSmBCMLWz9wZ2FI314bq25U'
consumer_secret = 'S36Fq8t5jZ8g9FK8h4A54sXQUCrsQVMDJecPnuj4rTRTlH8MFm'

access_token = '802485986319970305-VE7nSTtblGOYq5JW9pDWxgegBSTqPqK'
access_token_secret = 'AOwZ0c3ygr5ykFeDvr0rLqpu8LMbTu3nxGa87baOLUPnm'

while True:
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	public_tweets = api.search('Demonetisation')

	for tweet in public_tweets:
		print(tweet.text)
		analysis = TextBlob(tweet.text)
		print(analysis.sentiment)
		print()

	time.sleep(30)