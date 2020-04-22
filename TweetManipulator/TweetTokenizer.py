#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:55:26 2019

@author: Álvaro Domínguez Calvo
"""

import re

LISTA_SIMBOLOS = [".", ",", ";", "\"", "«", "»","”", "“","…", "?", "¿", "!", "¡", "*",
                  "^", "(", ")" ,"[", "]", "%", "{", "}", 
                  "<", ">", "=", "~", "$", "&", ":", "ː", "/", "|","♡", "♥", "▶", "❤", "★",
                  "►","▸",  "•", "-", "—", "–",  "҂", ".", "·", "☺", "♫", "+" 
                  ] 

LISTA_ESCAPE = ["\\n","\n", "\t", "\\", "\u200b", "\u200f", "\ue40e",
                  "\ue105", "\ue106","\ue107", "\ue407", "\ue404", "\ue418", "\ue413",
                  "\ue414", "\ue113", "\uf402kǻ", "\uf47d",
                  "\ue322", "\ue328", "\ue412",
                  "\ue022","\ue023","\ue057", "\ue056","\ue32b", "\ue40d", "\ue00e", 
                  "\ue411", "\ue51a",
                   "\ue00e","\ue106", "\ue057", "\ue420", "\ue03f", "\ue403",
                  "\u3000", "\ue32a", "\ue32d", "\ue32c",
                  "\x91", "\xad","\x93", "\x80", "\x84", "\x99", "\x92", "\x94", "\x96", "\x84"
                  ,"\x98"]

class TweetTokenizer:
    
    def __init__(self, tweetsToTokenize):
        

        for tweet in tweetsToTokenize:
            

            tweetDirtyCorpus = tweet.getCorpus()
            
            lowerCorpus = tweetDirtyCorpus.lower()
            corpusScapeless = self.__cleanScapes(lowerCorpus)

            corpusPunctless = self.__cleanPunctuations(corpusScapeless)


            corpusTokenized = re.split("\\s", corpusPunctless)


            corpusWhiteless = self.__cleanEmptyString(corpusTokenized)
            corpusNonLowHyphen = self.__cleanLowerHyphen(corpusWhiteless)
            cleanTokenAmp = self.__cleanAmps(corpusNonLowHyphen)

            cleanCorpus = cleanTokenAmp


            tweet.setCorpusTokenized(cleanCorpus)
            
            
          
  
    #TODO diagramas
    def __cleanPunctuations(self, tweetCorpus):
        
        
        for puntuacion in LISTA_SIMBOLOS:
            
            tweetCorpus = tweetCorpus.replace(puntuacion, " ")
            
        
        return tweetCorpus
    
    #TODO diagrama
    def __cleanScapes(self, tweetCorpus):
        
        for escape in LISTA_ESCAPE:
            
            tweetCorpus = tweetCorpus.replace(escape, " ")

        return tweetCorpus  
    
    
    
    #TODO diagrama hecho
    def __cleanEmptyString(self, tweetTokenized):
        
        tweetEmptyness = []
        for token in tweetTokenized:
            
            if(token != ""):
                
                tweetEmptyness.append(token)
                
        tweetTokenized = tweetEmptyness
        return tweetTokenized
    
    def __cleanLowerHyphen(self, tweetTokenized):
        
        tweetHypheness = []
        
        for token in tweetTokenized:
            charMention = token[0]
            
            if(charMention != '@'):
                    
                tokenLowerHypheness = token.replace("_", u"")
                tweetHypheness.append(tokenLowerHypheness)
                
            else:
                
                tweetHypheness.append(token)
                
        tweetTokenized = tweetHypheness
        
        return tweetTokenized
    
    
    def __cleanAmps(self, tweetTokenized):
        
        tweetAmpness = []
        
        for token in tweetTokenized:
            
            if (token != "amp" and token != ""):
                    
                tweetAmpness.append(token)
                
        tweetTokenized = tweetAmpness
        
        return tweetTokenized
    
    
