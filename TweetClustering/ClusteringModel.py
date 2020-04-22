#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:05:44 2019

@author: Álvaro Domínguez Calvo
"""


import TweetClustering.KMeansModel as kModel
import TweetClustering.Agglomerative as aglom


from sklearn.feature_extraction.text import TfidfVectorizer

CLUSTER_1 = "kmeans"
CLUSTER_2 = "agglomerative"
class ClusteringModel:
    
    def __init__(self, container, numClusters, algorithm):
        
        stratified = container.getStratified()
        
        self.__algorithm = algorithm
        self.__numClusters = numClusters
        self.__dictModel = self.__generateModel(stratified, numClusters, algorithm)
        
        
    def getModel(self):
        
        return self.__dictModel
        
        
    def getAlgorithm(self):
        
        return self.__algorithm
        

    def getNumClusters(self):
        
        return self.__numClusters
        
    def __generateModel(self, strat, numClusters, algorithm):
        
        dictModel = dict()
        
        for entity, tweets in strat.items():
            
#            patronHash =       r'(?u)(?<![@])#?\b\w\w+\b'
#            patronHashArroba = r'(?u)@?#?\b\w\w+\b'
            patronHashtagMention = r'[a-zA-Z.0-9+#+@\-/]*[a-zA-Z0-9+#+@\-/]'
            patronNoHashtagMention = r'[a-zA-Z.0-9\-/]*[a-zA-Z0-9\-/]'
            vectorizer = TfidfVectorizer(analyzer="word",
                                 token_pattern = patronNoHashtagMention, #binary = True,                                
                                 smooth_idf = False, norm = None)

            if(algorithm == CLUSTER_1):
                
                modelK = kModel.KMeansModel(numClusters, tweets, vectorizer)
                dictModel[entity] = modelK 
                
            if(algorithm == CLUSTER_2):
                
                modelK = aglom.Agglomerative(numClusters, tweets, vectorizer)
                dictModel[entity] = modelK 
            
        return dictModel
        
