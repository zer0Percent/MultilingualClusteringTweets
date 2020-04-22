#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:19:28 2019

@author: Álvaro Domínguez Calvo
"""

from nltk.stem import WordNetLemmatizer





lemmatizer = WordNetLemmatizer()

class TweetLemmatizer:
    
    def __init__(self, tweetsTranslated):
        
        for tweet in tweetsTranslated:
            
          
          corpusTokenized = tweet.getCorpusTokenized()

          
          corpusLemmatized = self.__lemmatizeCorpus(corpusTokenized)
          
          corpusZipped = self.__zipTweet(corpusLemmatized)
          
          tweet.setCorpus(corpusZipped)
          tweet.setCorpusTokenized(corpusLemmatized)


    def __zipTweet(self, tweetTokenized):
    
        corpusTweet = ""
        tokenCounter = 1
        
        lenTweet = len(tweetTokenized)
        
        for token in tweetTokenized:
            
        
            if(tokenCounter == lenTweet):
                    
                corpusTweet = corpusTweet + token
                    
            else:
                    
                corpusTweet = corpusTweet + token + " "
                
            tokenCounter += 1
            
        return corpusTweet


    def __lemmatizeCorpus(self, corpus):
        
        corpusLemmatized = []
            
        for token in corpus:
              
              tokenLemmatized = lemmatizer.lemmatize(token)
              corpusLemmatized.append(tokenLemmatized)

        return corpusLemmatized
    