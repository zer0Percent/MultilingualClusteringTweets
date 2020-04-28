#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:09:41 2019

@author: Álvaro Domínguez Calvo
"""
import re

ID_TWEET      = 0
CORPUS_TWEET  = 1
LANG_TWEET    = 2

LISTVOCALS = ["a", "e", "i", "o", "u", "y"]


DICT_ACCENTS = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
}

LIST_PRONOUNS = ["I", "you", "he", "she", "it", "we", "they", "here", "there", "that", "who",
                 "where", "which"]
DICT_VERBS = {
    "m" : "am",
    "s" : "is",
    "re": "are",
    "ve": "have",
    "ll": "will",
    "d" : "would",
}

DICT_NEGATIVES = {
    "arent" : ["are", "not"],
    "isnt"  : ["is", "not"],
    "didnt" : ["did", "not"],
    "wasnt" : ["was", "not"],
    "werent": ["were", "not"],
    "wouldnt": ["would", "not"],
    "shouldnt": ["should","not"],
    "mightnt" : ["might", "not"],
    "hadnt" : ["had", "not"],
    "hasnt" : ["has", "not"],
    "havent": ["have", "not"],
    "dont"  : ["do", "not"],
    "doesnt" : ["does", "not"],
    "wont"  : ["will", "not"],
    "shant" : ["shall", "not"],
    "cant"  : ["can", "not"],
    "couldnt" : ["could", "not"],
    "aint"   : ["aint"]    
}
NEGATIVE_CONTRACTION = "t"
COMILLA_UNO = "'" 
COMILLA_DOS = "’"
COMILLA_TRES = "´"
COMILLA_CUATRO = "ˈ"
COMILLA_CINCO = "´"
COMILLA_SEIS = "`"


REGULAR_ACCENTS = "á|é|í|ó|ú"

class TweetCleaner:
    

    def __init__(self, tweetsToNormalize):
        

        
        for tweet in tweetsToNormalize:
            

            corpusTokenized = tweet.getCorpusTokenized()

            corpusUrless = self.__cleanURLs(corpusTokenized)
            

            corpusNumerless = self.__deleteNumbers(corpusUrless)
                
            corpusSingleQuotless = self.__cleanQuoteTokens(corpusNumerless)
            corpusQuotless       = self.__cleanQuotes(corpusSingleQuotless) 
            
            #commonCleanCriteria = corpusQuotless
            

            #corpusContractless = self.__cleanContractions(commonCleanCriteria)

#            corpusMentionless, hashTags, mentions = self.__deleteMentionHashtag(corpusContractless)
            
            #TODO 
            corpusCleaned= self.__correctDuplicatedVocals(corpusQuotless)

            tweet.setCorpusTokenized(corpusCleaned) 
     
    
    """" Al hacer esto, vamos a devolver el tf-idf vectorizer y ya lo tenemos pesado """
    #TODO: Funciones para limpiar el vocabulario
    def raw_tweets(self, tweets_to_normalize):
        
        print("todo")
        
    # returns a vocabulary without weird CHARS and links
    def deleted_WL(self, tweets_to_normalize):

        print("todo")
        
    # returns a vocabulary without rare CHARS, links and tokens \ df(token) < fixedNumber
    def deleted_WLDF(self, tweets_to_normalize):
        
        print("todo")
    
    # returns a vocabulary without weird chars, links and hashtags/mentions
    def deleted_WLDFMT(self, tweet_to_normalize):

        print("todo")        
        

        

    
    def __correctDuplicatedVocals(self, corpusTokenized):
        
        corpusClean = []
        for token in corpusTokenized:
            
            corpusClean.append(self.__duplicateVocalDetector(token))
            
        return corpusClean
    
    def __duplicateVocalDetector(self, token):
        
        newToken = token
        for vocal in LISTVOCALS:
            
            pattern = "^"+ vocal + "(" + vocal + ")" + "+"
            duplicated = re.findall(pattern, token)
            if(duplicated):
                
                newToken = vocal
                break;
            
        return newToken
            
    def __deleteNumbers(self, corpusTokenized):
        
        corpusClean = []
        
        for token in corpusTokenized:
            
            finder = re.findall("[0-9]", token)
            
            if(not finder):
                
                corpusClean.append(token)
                
        return corpusClean
                

    def __deleteMentionHashtag(self, corpusTokenized):
        
        corpusClean = []
        
        setHashTags = set()
        setMentions = set()
        for token in corpusTokenized:

            firstChar = token[0]
            
            if (firstChar != "@"): 
                
                corpusClean.append(token)
                if(firstChar == "#"):
                   
                   setHashTags.add(token)
            
            else:
            
                   
                if(firstChar == "@"):
                    
                    setMentions.add(token)

        return corpusClean, setHashTags, setMentions
    

    

    def __cleanURLs(self, corpusTweet):
        
        corpusUrless = []
        lenCorpus  = len(corpusTweet)
        indexToken = 0
        
        while(indexToken < lenCorpus):
            
            token = corpusTweet[indexToken]

            findHttp = re.findall("http", token)
            if(len(findHttp) == 0):
                

                self.__appendToken(corpusUrless, token)
                
            else:

                indexToken = indexToken + 3
            
            
            indexToken += 1
            
        return corpusUrless 
    
    
    def __cleanEmptyChar(self, corpusTweet):
        
        corpusCleaned = []
        
        for token in corpusTweet:
            
            if(token != "" and token != ''):
                
                corpusCleaned.append(token)
                
        return corpusCleaned

    
    #TODO diagrama
    def __cleanQuotes(self, corpusTweet):
        
        corpusQuotless = []

        for token in corpusTweet:
            
            tokenQuotless = self.__cleanSingleQuote(token)
            
            if (tokenQuotless != ""):
                
                #self.__addToken(tokenQuotless, corpusQuotless)
                self.__appendToken(corpusQuotless, tokenQuotless)
            
        corpusTweet = corpusQuotless
#        print(corpusTweet)
        return corpusTweet
    
     #TODO diagram sec       
    def __cleanSingleQuote(self, tokenQuoted):
        
        cleanedFirstQuote = self.__cleanFirstQuote(tokenQuoted)
        cleanedLastQuote  = self.__cleanLastQuote(cleanedFirstQuote)
        
        tokenCleaned = cleanedLastQuote
                
        return tokenCleaned
    
    """ Develve el token sin comilla de inicio. Si no tiene, lo devuelve
    el token dado por parámetro
    'hola -> hola
    """
    #TODO diagrama
    def __cleanFirstQuote(self, tokenQuoted):
        
        tokenFirstQuotless = tokenQuoted
        
        lenQuoted = len(tokenFirstQuotless)
        firstQuote = tokenQuoted[0]

        while(firstQuote == COMILLA_UNO or firstQuote == COMILLA_DOS or
                                                          firstQuote == COMILLA_TRES or
                                                          firstQuote == COMILLA_CUATRO or
                                                          firstQuote == COMILLA_CINCO or
                                                          firstQuote == COMILLA_SEIS):

            tokenFirstQuotless = tokenFirstQuotless[1:lenQuoted]
            lenQuoted = len(tokenFirstQuotless)
            
            firstQuote = tokenFirstQuotless[0]
        
        return tokenFirstQuotless
    
    #TODO diagrama
    def __cleanLastQuote(self, tokenQuoted):
        
        tokenLastQuotless = tokenQuoted
        
        lenQuoted = len(tokenLastQuotless)
        lastQuote = tokenQuoted[lenQuoted - 1]
        
        while(lastQuote == COMILLA_UNO or lastQuote == COMILLA_DOS or
                                                      lastQuote == COMILLA_TRES or
                                                      lastQuote == COMILLA_CUATRO or
                                                      lastQuote == COMILLA_CINCO or
                                                      lastQuote == COMILLA_SEIS):
            
            
            tokenLastQuotless = tokenLastQuotless[0: (lenQuoted - 1)]
            lenQuoted = len(tokenLastQuotless)
            lastQuote = tokenLastQuotless[lenQuoted - 1]
        
        return tokenLastQuotless
    
    #TODO diagrama
    def __cleanQuoteTokens(self, corpusTweet):
        
        corpusQuotless = []
        
        for token in corpusTweet:
            
            if(not self.__isOnlyQuotes(token)):
                
                #self.__addToken(token, corpusQuotless)
                self.__appendToken(corpusQuotless, token)
                
        corpusTweet = corpusQuotless
        
        return corpusTweet
    
    def __isOnlyQuotes(self, token):
        
        isOnlyQuotes = True
        indexChar = 0
        
        while(indexChar < len(token)  and isOnlyQuotes):
            
            charToken = token[indexChar]
            
            if(charToken != COMILLA_UNO and charToken != COMILLA_DOS and charToken != 
               COMILLA_TRES and charToken != COMILLA_CUATRO and charToken != COMILLA_CINCO and
               charToken != COMILLA_SEIS):
            
                isOnlyQuotes  = False
                
            else:
            
                indexChar += 1
                
        return isOnlyQuotes


    
    """Funciones dependientes del lenguaje"""

#TODO diagram sec
    def __cleanContractions(self, corpusTweet):
        
        corpusContractless = []
        
        for token in corpusTweet:
            
            tokenContractless = []

            detectComilla = self.__detectContraction(token)
            """ Si el token no tiene comillas, es el token en sí """
            if(detectComilla == []):
                tokenContractless = [token]
            
            """ Si el token tiene la comilla UNO, se devuelve la contracción con COMILLA_UNO """
            if(detectComilla == [COMILLA_UNO]):
                tokenContractless = self.__cleanContraction(token, COMILLA_UNO)
            
            """ Si el token tiene la comilla  DOS, se devuelve la contracción con COMILLA_DOS"""
            if(detectComilla == [COMILLA_DOS]):
                tokenContractless = self.__cleanContraction(token, COMILLA_DOS)
                
            if(detectComilla == [COMILLA_TRES]):
                tokenContractless = self.__cleanContraction(token, COMILLA_TRES)
                
            if(detectComilla == [COMILLA_CUATRO]):
                tokenContractless = self.__cleanContraction(token, COMILLA_CUATRO)
                
            if(detectComilla == [COMILLA_CINCO]):
                 tokenContractless = self.__cleanContraction(token, COMILLA_CINCO)
                 
            if (detectComilla == [COMILLA_SEIS]):
                tokenContractless = self.__cleanContraction(token, COMILLA_SEIS)
                
            for unContracted in tokenContractless:
                
                self.__appendToken(corpusContractless, unContracted)
                #corpusContractless.append(unContracted)
        
        
        corpusTweet = corpusContractless
        
        return corpusTweet
    """ Dado un token, eliminar la contracción (you're ’ -> [you , re] 
    Si no tiene contracción, devolver la cadena tal cual"""
    
    #TODO diagram sec
    def __cleanContraction(self, tokenContracted, tokenComilla):
        
        tokenContractless = tokenContracted
        
        splitContract = tokenContractless.split(tokenComilla)
        
        if(len(splitContract) == 2):

            leftWord = splitContract[0]
            rightWord = splitContract[1]

            if (rightWord == NEGATIVE_CONTRACTION):
                """ [x,'t] """
                tokenUncontracted = tokenContracted.replace(tokenComilla, "")
                tokenContractless = DICT_NEGATIVES.get(tokenUncontracted)
                
                if(tokenContractless is None):
                    
                    tokenContractless = tokenUncontracted
                    
                    
            else:
                
                if (rightWord in DICT_VERBS):
                
                    extendedVerb = DICT_VERBS.get(rightWord)
                    
                    if(leftWord not in LIST_PRONOUNS and rightWord == "s"):
                        
                        #Se trata del genitivo sajón
                        """ [Paco, s] """
                        tokenContractless = [leftWord]
                        
                    else:
                        
                        tokenContractless = [leftWord, extendedVerb]
                else:
                    
                    tokenContractless = [rightWord]
        else:
            tokenContractless = splitContract
        
        return tokenContractless
    
    """ Devuelve lista vacía si no encuentra contracción alguna """     
    #TODO diagrama
    def __detectContraction(self, token):
        
        comilla = []
        comillaUno = list(set(re.findall(COMILLA_UNO, token)))
        comillaDos = list(set(re.findall(COMILLA_DOS, token)))
        comillaTres = list(set(re.findall(COMILLA_TRES, token)))
        comillaCuatro = list(set(re.findall(COMILLA_CUATRO, token)))
        comillaCinco = list(set(re.findall(COMILLA_CINCO, token)))
        comillaSeis = list(set(re.findall(COMILLA_SEIS, token)))
        
        if (comillaUno == ["'"]):
            comilla = comillaUno
        
        if(comillaDos == ["’"]):
            comilla = comillaDos
        
        if(comillaTres == ["´"]):
            comilla = comillaTres
            
        if(comillaCuatro == ["ˈ"]):
            comilla = comillaCuatro
            
        if(comillaCinco == ["´"]):
            comilla = comillaCinco
            
        if(comillaSeis == ["`"]):
            comilla == comillaSeis
            
        return comilla
    
    
    
    def __appendToken(self, corpus, token):
        
        if (len(token) != 0):
            
            corpus.append(token)