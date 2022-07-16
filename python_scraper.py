import pandas as pd
import requests
import yaml

def get_tweets(bearer_token, url):
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

def main():
    config = get_config()
    bearer_token = config['twitter api']['bearer token']
    url = create_twitter_url()
    res_json = get_tweets(bearer_token, url)

    return
    

if __name__ == '__main__':
    main()