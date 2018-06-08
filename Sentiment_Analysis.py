#!/usr/bin/python3
import json
import csv

def get_tweets(line):
        tweet_array =line.split(",")
        tweet_text = tweet_array[1]
        return tweet_text

def get_words(tweet):
        words = tweet.split(" ")
        return words

def maximum(p,neg,nu,count):
        mv = max(p,neg,nu)
        if(mv==p):
                sentiment = "positive"
        elif(mv==neg):
                sentiment = "negative"
        else:
                sentiment = "neutral"
        tup = (sentiment,mv)
        return tup

with open('tweets.csv') as csvfile:
        reader = csv.reader(csvfile)
        dict = open("tweet_with_score.json")
        dict_obj = dict.read()
        data = json.loads(dict_obj)
        with open('analysis.csv','a') as analysis:
                writer = csv.writer(analysis)
                writer.writerow(['Tweet','Sentiment','Sentiment Score'])
                for row in reader:
                        p=0
                        neg=0
                        nu=0
                        count=0

                        tweet = row[3]
						words =  get_words(tweet)
                        for word in words:
                                if word in data:
                                        obj = data[word]
                                        p = p + obj['positive']
                                        neg = neg + obj['negative']
                                        nu = nu + obj['neutral']
                                        count = count + 1
                        if(count!=0):
                                p = p/count
                                neg = neg/count
                                nu = nu/count
                                sentiment = maximum(p,neg,nu,count)
                                writer.writerow([tweet,sentiment[0],sentiment[1]])
