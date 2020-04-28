#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 21:46:39 2020

@author: alvaro-dev
"""

""" Tweet loader """


from TweetHandler import Tweet as tw

import os

class TweetLoader:
    
    def __init__(self):
        
        self.__tweets = dict()
        
        
    def get_tweets_entity(self, entity):
    
        return self.__tweets[entity]
    
    def get_tweets_language_entity(self, entity, lang):
        
        tweets_lang = []
        
        tweets_entity = self.__tweets[entity]

        for tweet in tweets_entity:

            if(tweet.getLang().lower() == lang):
                
                tweets_lang.append(tweet)
                
        return tweets_lang
        
    def load_tweets(self, path_dataset):
        
        entities = os.listdir(path_dataset)
        
        for entity in entities:
            
            path_file_entity = path_dataset + "/" + entity
            tweets = []

            with open(path_file_entity, 'r') as tweets_file:
                
                for tweet in tweets_file:
                    
                    info_tweet = tweet.split('\t')
                    
                    ## id, author, entity lang , timestamp, corpus
                    id_tweet = info_tweet[0]
                    author = info_tweet[1]
                    entity_code = info_tweet[2]
                    lang = info_tweet[3]
                    timestamp = info_tweet[4]
                    corpus = info_tweet[5]
                    
                    tweets.append(tw.Tweet(id_tweet, author, entity_code, lang, timestamp, corpus))
                
            self.__tweets[entity] = tweets
            
                    


        