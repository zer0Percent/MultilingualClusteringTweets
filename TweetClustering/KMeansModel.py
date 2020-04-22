#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:36:03 2019

@author: Álvaro Domínguez Calvo

"""
from sklearn.cluster import KMeans


class KMeansModel:
    

    def __init__(self, numTopics, tweetsEntity, vectorizer):
        

        self.__tweets = self.__getCorpus(tweetsEntity)
        self.__vectorizer = vectorizer
        self.__numTopics = numTopics
        
        self.__vec = self.__vectorizer.fit(self.__tweets)
        self.__tfidfMatrix  = self.__vec.transform(self.__tweets)


        self.__kmeans = KMeans(init = 'k-means++', n_clusters = self.__numTopics)
        self.__kmeans.fit(self.__tfidfMatrix)

        
    
    def getNumTopics(self):
        
        return self.__numTopics
    
    def getFittedModel(self):
        
        return self.__kmeans
    
    def clusteredTweets(self):
        
        return self.__kmeans.labels_


                
    def __getCorpus(self, tweetsEntity):
        
        corpus = []
        
        for tweet in tweetsEntity:
            
            corpusTweet = tweet.getCorpus()
            corpus.append(corpusTweet)
            
            
        return corpus
    
    
    

