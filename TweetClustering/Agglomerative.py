#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:55:33 2019

@author: Álvaro Domínguez Calvo
"""

from sklearn.cluster import AgglomerativeClustering


class Agglomerative:
    
    
    def __init__(self, numClusters, tweetsEntity, vectorizer):
        
        self.__tweets = self.__getCorpus(tweetsEntity)
        self.__numClusters= numClusters
        self.__vectorizer = vectorizer
        
        self.__vec = self.__vectorizer.fit(self.__tweets)
        self.__tfidfMatrix  = self.__vec.transform(self.__tweets)
        
        
        self.__agglomerated = AgglomerativeClustering(n_clusters=self.__numClusters,
                                               affinity='euclidean', linkage='ward')
        self.__agglomerated.fit(self.__tfidfMatrix.toarray())

        
        
        
        
        
    def getNumTopics(self):
        
        return self.__numClusters
    
    def getFittedModel(self):
        
        return self.__agglomerated
    
    def clusteredTweets(self):
        
        return self.__agglomerated.labels_
    
    
    def __getCorpus(self, tweetsEntity):
        
        corpus = []
        
        for tweet in tweetsEntity:
            
            corpusTweet = tweet.getCorpus()
            corpus.append(corpusTweet)
            
            
        return corpus