import tweepy
import os
from pprint import pprint
from os import environ  # To get the environment variables


class Trends:
    
    def set_tweep_connection(self):
        auth = tweepy.OAuthHandler(environ["TWITTER_CONSUMER_KEY"],
                                   environ["TWITTER_CONSUMER_SECRET"])
    
        auth.set_access_token(environ["TWITTER_ACCESS_TOKEN"],
                          environ["TWITTER_ACCESS_TOKEN_SECRET"])
        
        return tweepy.API(auth)
    
    def get_location_trends(self, api, clat, clong):
        '''
            Variables:
            api (object) = tweepy api connection with twitter.
            clat (float) = latitude of location we are searching for.
            clong (float) = longitude of location we are searching for.
            Return Value:
            Returns nearest location details and its most current top 5 trends in Twitter.
            '''
        
        closest_locations = api.trends_closest(clat, clong)
        
        # Get the first closest location in Twitter based on clat, clong. Tweepy already sorts by closest first.
        for i in range(1):
            twitter_location = closest_locations[i]
        
        return_value = {"NearestLocation": twitter_location}
        
        # if twitter_location['placeType']['name'] == 'Country':
        #     loc = twitter_location['country']
        #     print(f"Twitter found the nearest location in {twitter_location['country']}.")
        # else:
        #     loc = f"{twitter_location['name']}, {twitter_location['country']}"
        #     print(f"Twitter found the nearest location in {twitter_location['name']}, {twitter_location['country']}.")
        
        # Get the top 10 trends according to twitter_location, sorted by tweet_volume (max first).
        top_trends = api.trends_place(twitter_location['woeid'])[0]['trends']
        top_trends = sorted(top_trends, key=lambda dict: dict['tweet_volume'] or 0, reverse=True)
        
        t = top_trends[:5]
        top5 = list()
        for i, val in enumerate(t, start=1):
            tup = i, val
            top5.append(tup)
        
        #return_value["Top5Trends"] = top5
        return top5

if __name__ == '__main__':
    # Get trends for nearest location in Twitter.
    my_trend = Trends()
    my_api = my_trend.set_tweep_connection()
    print(my_trend.get_location_trends(my_api, 37.1833, -3.6))
