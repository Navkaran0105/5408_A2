import tweepy
import time
import json
import csv

#API Details
consumer_key = "mpJ1S0PWPPcIx1XVn4aYPjWis"
consumer_secret= "cy8NO2TqPucdfhAttiQapa2GJOFnLamTaEegjzakH9C6lps42D"
access_key ="1000023816251281408-tribGTbICH7Oj0Vxe0WrWY2KIqXFBl"
access_secret ="qDLXrgE2DBjEnjAQMv8WMYQoEVivOTB84lEsmko3w0iR4"

conn = tweepy.OAuthHandler(consumer_key, consumer_secret)
conn.set_access_token(access_key, access_secret)
api = tweepy.API(conn)

queries =["#HanSolo", "\"Nova Scotia\"","@Windows","#realDonaldTrump"]
def get_tweets(query):
        api=tweepy.API(conn)
        try:
                tweets = api.search(query,count=100)
        except tweepy.error.TweepError as e:
                tweets= json.loads(e.response.text)

        return tweets

with open('tweets.csv','w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['id','user','created_at','text'])
        for query in queries:
                tw = get_tweets(query)
                for tweet in tw:
                        writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text])