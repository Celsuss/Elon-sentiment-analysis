import pandas as pd
import numpy as np
import requests
import yaml

def get_tweets_from_url(bearer_token, url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    return response.json()

def create_twitter_url():
    handle = "elonmusk"
    max_results = 100
    mrf = "max_results={}".format(max_results)
    q = "query=from:{}".format(handle)
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(
        mrf, q
    )
    return url

def get_config():
    with open('config.yaml', 'r') as ymlfile:
        return yaml.load(ymlfile)

def filter_tweets(tweets):
    tweets = [tweet['text'] for tweet in tweets if tweet['text'][0] != '@']
    return tweets

def get_tweets(bearer_token):
    url = create_twitter_url()
    res_json = get_tweets_from_url(bearer_token, url)
    tweets = filter_tweets(res_json['data'])
    return tweets

def main():
    config = get_config()
    bearer_token = config['twitter api']['bearer token']
    tweets = get_tweets(bearer_token)

    return
    

if __name__ == '__main__':
    main()