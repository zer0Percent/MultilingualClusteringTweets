#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from yandex_translate import YandexTranslate
import re
import time


ID_TWEET      = 0
CORPUS_TWEET  = 1
LANG_TWEET    = 2

LANG_1 = "es"
LANG_2 = "en"



class TweetTraductor:
    

    def __init__(self, tweetsNormalized, keyYandex):
        
        self.__TRANSLATOR = YandexTranslate(keyYandex)


        tweetCounter = 0
        for tweet in tweetsNormalized:
            
            corpusTokenized = tweet.getCorpusTokenized()
            langTweet = tweet.getLang()

            
            corpusTranslated = None
            if(langTweet != LANG_2):
                tweetZipped = self.__zipTweet(corpusTokenized)
                
                try:
                    
                    corpusTranslated = self.__translateCorpus(tweetZipped, LANG_2).lower()
                    
                except:
                    print("Intentando traducir el token de nuevo. Espera de 7 minutos")
                    time.sleep(420)
                    corpusTranslated = self.__translateCorpus(tweetZipped, LANG_2).lower()
                tweetCounter += 1
                #Dormimos el proceso durante X segundos cada Y tweets
                tweetUnzipped = self.__unZipTweet(corpusTranslated)
                corpusTranslated = tweetUnzipped
                
                if(tweetCounter > 50):
                    #print("Cincuenta tweets traducidos")
                    time.sleep(1)
                    tweetCounter = 0
                    

                
            else:
                
                corpusTranslated = corpusTokenized
                
            
            tweet.setCorpusTokenized(corpusTranslated)

            
    
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
    
    def __unZipTweet(self, zippedTweet):
        
        unZip = []
        
        if(zippedTweet != ""):
            
            unZip = re.split("\s", zippedTweet)
            
        return unZip


    def __translateCorpus(self, corpusNormalized, lang):

        corpusTranslated = ""
        if (corpusNormalized != ""):

                corpusTranslated = self.__TRANSLATOR.translate(corpusNormalized, lang)['text'][0]
                
        return corpusTranslated
                
