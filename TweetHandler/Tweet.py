#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Un tweet almacenará la siguiente información:
    
    ---> ID
    ---> Entity
    ---> LANG
    ---> Corpus (string)

    
"""


class Tweet:
    
    def __init__(self, id_tweet, author, entity_code, lang, timestamp, corpus):
        ## id, author, entity lang , timestamp, corpus
        
        self.__id = id_tweet
        self.__author = author
        self.__entity_code = entity_code
        self.__lang = lang
        self.__timestamp = timestamp
        self.__corpus = corpus

        self.__corpusTokenized = []
        self.__hashtags = set()
        self.__mentions = set()
        

    def getCorpus(self):
        
        return self.__corpus
    
    def setCorpus(self, corpus):
        
        self.__corpusTweet = corpus
    
        
    def setCorpusTokenized(self, tokenized):
        
        self.__corpusTokenized = tokenized
        
        
    def getCorpusTokenized(self):
        
        return self.__corpusTokenized
    
        
    def getId(self):
        
        return self.__id

    
    def getEntity(self):
        
        return self.__entity_code
    
    def getLang(self):
        
        return self.__lang
    
    def set_hashtags(self, hashtags):
        self.__hashtags = hashtags
        
    def set_mentions(self, mentions):
        self.__mentions = mentions
    
    def get_hashtags(self):
        return self.__hashtags
    def get_mentions(self):
        return self.__mentions

