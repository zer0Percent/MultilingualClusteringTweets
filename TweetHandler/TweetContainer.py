#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:06:39 2019

@author: Álvaro Domínguez Calvo
"""
import os
import TweetHandler.Tweet as tw
import TweetHandler.StratifiedSampling as strat


ID_TWEET          = 0
ENTITY_TWEET      = 1
LANG_TWEET        = 2
CORPUS_TWEET      = 3   


class TweetContainer:
    
    def __init__(self, pathDataSetFolder, numTweets):
        
        pathTweets = pathDataSetFolder + "/" + "tweets"
        self.__dictEntityTweets          = self.__generateTweetContainer(pathTweets)
        
        
        self.__stratified = strat.StratifiedSampling(self.__dictEntityTweets, numTweets)
        
        self.__stratifiedTweets = self.__stratified.getSampledTweets()
        
        
        
        
    def getStratified(self):
        
        return self.__stratifiedTweets
    
    
    def __generateTweetContainer(self, pathTweets):
        

        tweetsEntitied = os.listdir(pathTweets)
        
        dictTweets = dict()
        for entity in tweetsEntitied:

            listTweets = []

            
            pathTextedTweets = pathTweets + "/" + entity
            
            with open(pathTextedTweets, "r") as tweets:
                
                for tweet in tweets:

                    infoTweet = tweet.split("\t")
                    
                    ID     = infoTweet[ID_TWEET].replace(" ", "")
                    ENTITY = infoTweet[ENTITY_TWEET].replace(" ", "")
                    LANG   = infoTweet[LANG_TWEET].replace(" ", "").lower()
                    CORPUS = infoTweet[CORPUS_TWEET]
                    
                    tweet = tw.Tweet(ID, ENTITY, LANG, CORPUS)
                    
                    listTweets.append(tweet)
                    
                    
                tweets.close()
                
            currentEntity = entity.replace(".dat", "")
            dictTweets[currentEntity] = listTweets
                
        return dictTweets
   
    
           
    def getTweetContainer(self):
        
        return self.__dictEntityTweets

    
    def sizeContainer(self):
        
        sizeContainer = 0
        
        for entity in self.__dictEntityTweets.keys():
                
            listTweets = self.__dictEntityTweets.get(entity)
            sizeList = len(listTweets)
                
            sizeContainer += sizeList
                
        return sizeContainer
    
    def sizeStratified(self):
        
        sizeStrat = 0
        
        for entity in self.__stratifiedTweets.keys():
            
            listTweets = self.__stratifiedTweets.get(entity)
            sizeList = len(listTweets)
            
            sizeStrat += sizeList
            
        return sizeStrat
    
        
    def sizeEntityContainer(self, entity):
        
        return len(self.__dictEntityTweets.get(entity))
    
    def sizeEntityStrat(self, entity):
        
        return len(self.__stratifiedTweets.get(entity))
    
       
            
    def __totalTweets(self, isContainer):
        
        spanish = 0
        english = 0
        
        data = None
        if(isContainer):
            
            data = self.__dictEntityTweets
            
        else:
            
            data = self.__stratifiedTweets
            
        
        for entity in data.keys():
            
            tweets = data.get(entity)
            tweetsSpanish, tweetsEnglish = self.__tweetsLang(tweets)
            
            spanish += tweetsSpanish
            english += tweetsEnglish
        
        return spanish, english

#    def __tweetsLang(self, tweets):
#        
#        spanish = 0
#        english = 0
#        
#        for tweet in tweets:
#            
#            lang = tweet.getLang()
#            
#            if(lang == "es"):
#                
#                spanish += 1
#                
#            else:
#                
#                english += 1
#
#        return spanish, english
                 







     