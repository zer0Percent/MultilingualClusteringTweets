#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:14:22 2019

@author: Álvaro Domínguez Calvo
"""

import TweetManipulator.TweetTokenizer as twTok
import TweetManipulator.TweetCleaner as twCle
import TweetManipulator.TweetLemmatizer as twLem
#import TweetManipulator.TweetTraductor as twTrad

KEY_1 = "trnsl.1.1.20190416T153214Z.0200c1cc626155a2.2794fe9f1a34c4bbf93a679f2269247eb28c9879"


class TweetNormalizer:

    #def __init__(self, dictEntity, keyYandex):
        
        #self.__keyYandex = keyYandex
        
        #self.__preprocessEntities(dictEntity)
        
    def __init__(self, tweets_entity):
        
        self.preprocess_tweets(tweets_entity)

    def __preprocessEntities(self, dictEntity):
        
        for entity in dictEntity.keys():

            entityTrain = dictEntity.get(entity)
            
            twTok.TweetTokenizer(entityTrain)
            #twTrad.TweetTraductor(entityTrain, self.__keyYandex)
            twCle.TweetCleaner(entityTrain) 
            twLem.TweetLemmatizer(entityTrain)
            
    def preprocess_tweets(self, tweets_entity):
        
            twTok.TweetTokenizer(tweets_entity)
            #twTrad.TweetTraductor(entityTrain, self.__keyYandex)
            twCle.TweetCleaner(tweets_entity) 
            twLem.TweetLemmatizer(tweets_entity)



        
