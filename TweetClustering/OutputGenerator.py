#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:05:20 2019

@author: Álvaro Domínguez Calvo
"""

class OutputGenerator:
    
    
    def __init__(self, container,
                 listClusteringModel,
                 pathFolderData, nameOut):
        
        self.__generateOutPut(container, listClusteringModel, pathFolderData, nameOut)
        
    

    def __generateOutPut(self, container, listClusteringModel, pathFolderData, nameOut):
        
        for clusteringModel in listClusteringModel:
            
            
            algorithm = clusteringModel.getAlgorithm()
            numClusters = clusteringModel.getNumClusters()
            trainedModel = clusteringModel.getModel()
            
            topicDetection = algorithm + "-" + str(numClusters) + "_"  + nameOut
            sysPath = pathFolderData + "/" + topicDetection + ".sys"
            
            stratified = container.getStratified()
            
            """ C0, C1, C2; C3, C4, C5, C6; C7, C8 C9  """
            
            fileTest = open(sysPath, "w")
            self.__writeFileTest(stratified, trainedModel, fileTest)
            fileTest.close()
        
    
    def __writeFileTest(self, entityStratified, trainedModel, fileTest):
        
        startAt = 0
        for entity in entityStratified.keys():
            
            tweetsEntity = entityStratified.get(entity)
            modelEntity = trainedModel.get(entity)

            if(modelEntity != None):
                
                
                labelCluster = modelEntity.clusteredTweets()
                numClustersModel = modelEntity.getNumTopics()
                
                self.__writeEntityTest(startAt, tweetsEntity, labelCluster, fileTest)
                
                startAt = startAt + numClustersModel
            
    
    def __writeEntityTest(self, startAt, tweetsEntity, labelCluster, fileTest):
        
        numTweets = len(tweetsEntity)

        index = 0
        
        while(index < numTweets):
            
            tweet = tweetsEntity[index]
            
            entityTweet = tweet.getEntity()
            idTweet = tweet.getId()
            
            cluster = labelCluster[index]
            numCluster = startAt + cluster
            
            lineTest = entityTweet + "\t" + idTweet + "\t" + "cluster_" + str(numCluster) + "\n"
            fileTest.write(lineTest)
            
            index += 1
            
