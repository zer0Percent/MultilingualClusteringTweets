#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:05:49 2019

@author: Álvaro Domínguez Calvo
"""

import random

class StratifiedSampling:
    
    def __init__(self, dictEntity, numTweets):
        
        totalTweets = self.__getTotalTweets(dictEntity)
        
        ctePropor = self.__getConstant(totalTweets, numTweets)
        self.__dictStratified = self.__stratifyTweets(dictEntity, ctePropor)
        
        
    def __getConstant(self, totalTweets, numTweets):
        
        return totalTweets/numTweets
    
    def getSampledTweets(self):
        
        return self.__dictStratified
    
    def __stratifyTweets(self, dictEntity, ctePropor):
        
        
        dictNumTweets = self.__tweetsPerEntity(dictEntity, ctePropor)
        
        dictStratified = dict()
        
        for entity, numTweets in dictNumTweets.items():
            
            listTweets = dictEntity.get(entity)
            dictStratified[entity] = self.__firstTweetsOf(listTweets, numTweets)
            
        return dictStratified
            
        
        
    def __tweetsPerEntity(self, dictEntity, ctePropor):
        
        tweetsPerEntity = dict()
        
        for tweet, listTweets in dictEntity.items():
            
            tweetsPerEntity[tweet] = round(len(listTweets)/ctePropor)
            
        return tweetsPerEntity
    
    def __getTotalTweets(self, dictEntity):
        
        totalTweets = 0
        for tweets in dictEntity.values():
            
            totalTweets += len(tweets)
            
        return totalTweets
    

    def __firstTweetsOf(self, listTweets, numTweets):
        
        
        counterRandom = 0
        #Generar una lista de numTweets números aleatorios
        randomSet = set()
        
        while(counterRandom < numTweets):
            
            randomNumber = random.randint(0, len(listTweets) - 1)
            
            if(randomNumber not in randomSet):
                
                randomSet.add(randomNumber)
                
                counterRandom += 1
        
        listRandom = list(randomSet)
        counter = 0
        
        firstTweets = []
        while(counter < numTweets):
            
            randomized = listRandom[counter]
            tweet = listTweets[randomized]
            firstTweets.append(tweet)
            counter += 1
            
            
        return firstTweets
            
            
        