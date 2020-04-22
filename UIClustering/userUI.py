#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path as checker
import TweetManipulator.TweetNormalizer as twNorm
import TweetHandler.TweetContainer as twCont
import TweetClustering.ClusteringModel as cluMod
import TweetClustering.OutputGenerator as outGen

from yandex_translate import YandexTranslate

from os import system




import pickle as pk
OPTION_1 = "1"
OPTION_2 = "2"
OPTION_3 = "3"
OPTION_4 = "4"
OPTION_5 = "5"
OPTION_6 = "6"
OPTION_7 = "7"
OPTION_8 = "8"

OP_A = "a"
OP_B = "b"
OP_C = "c"
OP_D = "d"
OP_E = "e"


INVALID = "Opción no válida. Inténtelo de nuevo. \n"

HYPHENS = "-----------"


OPTION_YES = "s"
OPTION_NO  = "n"
dobleReturn = "\n \n"
dobleTab    = "\t \t "


WAIT_PLEASE = "Por favor, espere... \n"


OPTIONS = (
      "1 -Preprocesar tweets" + dobleReturn + 
      
      "2 -Generar clusters" + dobleReturn +
            
      "3 -Generar archivo de salida " + dobleReturn +
      
      "4 -Cargar archivos " + dobleReturn +  
      
      "5 -Limpiar datos almacenados " + dobleReturn + 
      
      "6 -Modificar o introducir claves de acceso a API's" + dobleReturn +
      
      "7 -Menú de ayuda" + dobleReturn + 
      
      "8 -Salir del asistente" + dobleReturn)


OPTIONS_CHAR = (
        "a) Cargar tweets procesados" + dobleReturn +
        "b) Cargar archivo con clusters generados"                   + dobleReturn + 
        "c) Salir"
        )

ALGORITMO = (
        "a) K-Medias" + dobleReturn +
        "b) Aglomerativo jerárquico"                   + dobleReturn + 
        "c) Salir"
        )

HELP = (
        "a) Sobre la estructura de directorios" + dobleReturn +
        "b) Sobre las rutas a introducir" + dobleReturn +
        "c) Sobre las claves de acceso a las API's" + dobleReturn +  
        "d) Salir" + dobleReturn
        )
API = (
       "a) Traductor Yandex" + dobleReturn +
       "b) Salir"
       )
class UIClustering:

     
    def __init__(self):
         
         
         self.__keepExecuting = True
         self.__keepExecutingOption = True
         
         
         self.__containerTraining = None
         
         self.__yandexKey = None
         
         self.__trainedModel = None
         self.__launchUI()
         
    
    
    def __pickleFile(self, toPickle, path):
        
        file = open(path, "wb")
        pk.dump(toPickle, file)
        file.close()
        
    def __readPickle(self, path):
    
        fileOpen = open(path, "rb")
        pickled = pk.load(fileOpen)
        fileOpen.close()
    
        return pickled
    
    def __clearContainers(self):
        
        self.__containerTraining = None
        
    def __clearModel(self):
        
        self.__trainedModel = None
        
    def __clearKeys(self):
        
        self.__yandexKey = None

    def __printOption(self, option):
        
        if(option == OPTION_1):
            print(dobleTab + HYPHENS + " Opción: " + OPTION_1 + " " + HYPHENS + "\n" + 
                      dobleTab + "\t" + " PREPROCESAR TWEETS " + dobleReturn)
            
        if(option == OPTION_2):
            print(dobleTab + HYPHENS + " Opción: " + OPTION_2 + " " + HYPHENS + "\n" + 
                      dobleTab + "\t" + " GENERAR CLUSTERS"  + dobleReturn)    
            
            
        if(option == OPTION_3): 
            print(dobleTab + HYPHENS + " Opción: " + OPTION_4 + " " + HYPHENS + "\n" + 
                      dobleTab + "\t" + " GENERAR ARCHIVO DE SALIDA " + dobleReturn)   
            
        if(option == OPTION_4):
            print(dobleTab + HYPHENS + " Opción: " + OPTION_5 + " " + HYPHENS + "\n" + 
                      dobleTab + "\t" + " Cargar archivos " + dobleReturn)        

        
        if(option == OPTION_5):
            print(dobleTab + HYPHENS + " Opción: " + OPTION_5 + " " + HYPHENS + "\n" + 
                      dobleTab + "\t" + " LIMPIAR VARIABLES " + dobleReturn)
            
            
        if(option == OPTION_6):
            print(dobleTab + HYPHENS + " Opción: " + OPTION_6 + " " + HYPHENS + "\n" + 
                      dobleTab + "\t" + " Claves de acceso a API's " + dobleReturn)   
            
        if(option == OPTION_7):        
            print(dobleTab + HYPHENS + " Opción: " + OPTION_6 + " " + HYPHENS + "\n" + 
                      dobleTab + "\t" + " MENÚ DE AYUDA " + dobleReturn)   
            
        
            
            
    def __launchUI(self):
        
        self.__printMensaje("ASISTENTE PARA PREPROCESAR Y AGRUPAR TWEETS MULTILINGÜES ")
        
        while(self.__keepExecuting):
            
            chosenProperly = False
            chosenOption = input("\n"+ "Elija  una de las siguientes opciones: \n" + OPTIONS)
            

            if(chosenOption == OPTION_1):
                
                if(self.__yandexKey != None):
                    
                    system("clear")
                    self.__printOption(chosenOption)
                    
                    self.__printOptionOne()
                    
                else:
                    
                    system("clear")
                    self.__printMensaje("No ha introducido ninguna clave de acceso para la herramienta de traducción. \n Introduzca una con la opción \" Modificar o introducir claves de acceso a API's\"")

                    
                chosenProperly = True
            
            if(chosenOption == OPTION_2):
                
                system("clear")
                self.__printOption(chosenOption)
                while(self.__keepExecutingOption):
                    
                    print("Elija el algoritmo de agrupamiento. \n" + ALGORITMO + "\n")
                    chosenChar = input()
                    chosenChar = chosenChar.lower()
                    
                    self.__printOptionTwo(chosenChar)
                
                self.__keepExecutingOption = True
                chosenProperly = True
            
            if(chosenOption == OPTION_3):
                
                system("clear")
                self.__printOption(chosenOption)
                
                
                self.__printOptionThree()
                
                chosenProperly = True


            if(chosenOption == OPTION_4):
                
                system("clear")
                self.__printOption(chosenOption)
                while(self.__keepExecutingOption):

                    print("¿Qué quieres hacer? \n" + OPTIONS_CHAR + "\n")
                    
                    chosenChar = input()
                    chosenChar = chosenChar.lower()
                    

                    self.__cargaArchivos(chosenChar)


                system("clear")
                self.__keepExecutingOption = True
                chosenProperly = True
                
            if(chosenOption == OPTION_5):
                
                system("clear")
                self.__printOption(chosenOption)
                self.__printOptionFive()
                                        
                chosenProperly = True
                
                
            if(chosenOption == OPTION_6):
                
                system("clear")
                self.__printOption(chosenOption)
                
                while(self.__keepExecutingOption):
                    
                    print("¿De qué API deseas cargar la clave?: \n" + API + "\n")
                    
                    chosenChar = input()
                    chosenChar = chosenChar.lower()
                    
                    self.__printOptionSix(chosenChar)
                    
                system("clear")
                self.__keepExecutingOption = True
                chosenProperly = True
                    
            if(chosenOption == OPTION_7):
                
                system("clear")
                self.__printOption(chosenOption)
                
                while(self.__keepExecutingOption):
                    print("¿De qué necesitas ayuda?: \n" + HELP)
                    
                    chosenChar = input()
                    chosenChar = chosenChar.lower()
                    
                    self.__printOptionSeven(chosenChar)
                    
                system("clear")
                self.__keepExecutingOption = True
                chosenProperly = True
                
            if(chosenOption == OPTION_8):
                
                self.__printOption(chosenOption)
                self.__keepExecuting = False
                
                
                chosenProperly = True
                
            if(not chosenProperly):
                
                system("clear")  
                self.__printMensaje(INVALID)
              
                
    def __askClosing(self):
        
        while(True):
            sureClose = input("¿Desea cerrar el programa? (S/N): " )
            
            sureClose = sureClose.lower()
            if(sureClose == OPTION_YES):
                
                self.__keepExecuting = False
#                get_ipython().magic('clear')
                system("clear")
                break
                
            if(sureClose == OPTION_NO):
#                get_ipython().magic('clear')
                system("clear")
                break
                
            if(sureClose != OPTION_YES and sureClose != OPTION_NO):
                system("clear")
                self.__printMensaje(INVALID)
            
    # OP4 Cargar archivos    
    def __cargaArchivos(self, chosenChar):
        tweetsAlreadyCharged = "Tienes unos tweets procesados ya cargados. " + "¿Quieres cargar nuevos igualmente?"
        modelAlreadyCharged  = "Tienes unos clusters por entidad ya cargados. " + "¿Quieres cargar unos nuevos igualmente?"
        
        pathArchive = "Introduzca la ruta en la que se encuentren {}"
        
        if(chosenChar == OP_A):
                    
            if(self.__containerTraining != None):
                        
                while(True):
                    opcion = input(tweetsAlreadyCharged + " (S/N): ")
                    opcion = opcion.lower()
                            
                    if(opcion == OPTION_YES):
                        
                        while(True):     
                            pathProcesedTraining = input(pathArchive.format("los tweets procesados: "))
                            print("\n")
                            if(checker.isfile(pathProcesedTraining)):
                                
                                self.__containerTraining = self.__readPickle(pathProcesedTraining)
                                system("clear")
                                self.__printMensaje("Tweets procesados cargados")
                                break
                            
                            else:
                                system("clear")
                                self.__printMensaje("La ruta especificada no corresponde con un archivo. Inténtelo de nuevo. ")
                            
                        break 
                    if(opcion == OPTION_NO):
                        
                        system("clear")
                        self.__printMensaje("Operación abortada")
#                        self.__keepExecutingOption = False
                        break
                    if(opcion != OPTION_YES and opcion !=OPTION_NO):
                        
                        system("clear")
                        self.__printMensaje(INVALID)
            else:
                        
                while(True):
                    
                        pathProcesedTraining = input(pathArchive.format("los tweets procesados: "))
                        
                        if(checker.isfile(pathProcesedTraining)):
                            
                            self.__containerTraining = self.__readPickle(pathProcesedTraining)
                            system("clear")
                            self.__printMensaje("Tweets procesados cargados")
                            break
                        
                        else:
                            system("clear")
                            self.__printMensaje("La ruta especificada no corresponde con un archivo. Inténtelo de nuevo. ")
               
                    
        #CARGAR CLUSTERS GENERADOS
        if(chosenChar == OP_B):
                    
            if(self.__trainedModel != None):
                
                while(True):
                    opcion = input(modelAlreadyCharged + " (S/N): ")
                    opcion = opcion.lower()
                    
                    if(opcion == OPTION_YES):
                      
                        while(True):
                            pathModelTrained = input(pathArchive.format("los clusters generados por entidad: "))
                            
                            if(checker.isfile(pathModelTrained)):
                                
                                self.__trainedModel = self.__readPickle(pathModelTrained)
                                system("clear")
                                self.__printMensaje("Clusters cargados")
                                break
                            
                            else:
                                system("clear")
                                self.__printMensaje("La ruta especificada no corresponde con un archivo. Inténtelo de nuevo. ")
                    
                        break
                    if(opcion == OPTION_NO):
                        
                        system("clear")
                        self.__printMensaje("Operación abortada")
#                        self.__keepExecutingOption = False
                        break
                    
                    if(opcion != OPTION_YES and opcion !=OPTION_NO):
                        
                        system("clear")
                        self.__printMensaje(INVALID)

                
            else:

                
                while(True):
                    pathModelTrained = input(pathArchive.format("los clusters generados por entidad: "))
                            
                    if(checker.isfile(pathModelTrained)):
                                
                        self.__trainedModel = self.__readPickle(pathModelTrained)
                        system("clear")
                        self.__printMensaje("Clusters cargados")
                        break
                            
                    else:
                        system("clear")
                        self.__printMensaje("La ruta especificada no corresponde con un archivo. Inténtelo de nuevo. ")
                

                
                #salir    
        if(chosenChar == OP_C):
            
            self.__keepExecutingOption = False
            
        if(chosenChar != OP_A and chosenChar != OP_B and chosenChar != OP_C):
            
            system("clear")
            self.__printMensaje(INVALID)
    
    #OP1: Preprocesar tweets
    def __printOptionOne(self):
        

        
        #Si la ruta existe, hacer. Si no, print ("No existe la carpeta")
        #Si la ruta es una carpeta (NO es un archivo) Y 
        tweetsQuieres = "¿Cuántos tweets quieres preprocesar?" + dobleTab
        mensajeDone = "¡Tweets de procesados!"
        
        pathFolderTraining = ""

        
        numTweetsTraining = 0


        while(True):
            pathFolderDataSet = input("Introduzca la ruta de la carpeta en la que se encuentren los tweets \n almacenados por entidad: ")
                
            if(checker.isdir(pathFolderDataSet)):
                    
                pathFolderTraining = pathFolderDataSet
                
                pathProcesedTraining = pathFolderTraining + "/" + "tweetsProcessed"
                break
                
            else:
                
                system("clear")                    
                self.__printMensaje("La carpeta no existe o no corresponde con una carpeta. "+ 
                          "Inténtelo de nuevo")
         
        while(True):
                        
            strNumTweetsTraining = input(tweetsQuieres)
#            strNumTweetsTest     = input(tweetsQuieres.format("las pruebas") + "\n")

                    
            if(self.__isGoodNumber(strNumTweetsTraining)):
                            
                numTweetsTraining    = int(strNumTweetsTraining)   
                break
                        
            else:
                
                system("clear")
                self.__printMensaje("El número introducido está en un formato erróneo. Inténtelo de nuevo. \n")
                        
        self.__containerTraining = twCont.TweetContainer(pathFolderTraining, numTweetsTraining)
                                
                                
        procesando = "PROCESANDO TWEETS..."
                         
        self.__printMensaje(procesando)
        stratTraining = self.__containerTraining.getStratified()
        twNorm.TweetNormalizer(stratTraining, self.__yandexKey)
        self.__printMensaje(mensajeDone)
        self.__pickleFile(self.__containerTraining, pathProcesedTraining)

                                
        
        self.__printMensaje("Tweets procesados almacenados en: " + 
                            pathProcesedTraining)
                    
    
    #OP2 generar clusters
    def __printOptionTwo(self, chosenChar):
        
        algoritmo = ""
        
        if(chosenChar == OP_A):
            
            algoritmo = "kmeans"
            
            if(self.__containerTraining != None):
            

                while(True): 
    
                    pathModelSaving = input("Indica la ruta de la carpeta en la que quieres guardar los clusters generados: ")
                    if(not checker.isdir(pathModelSaving)):
                        
                        system("clear")
                        self.__printMensaje("La carpeta especificada no existe. Creela e inténtelo de nuevo. ")
                        
                    else:
                        
                        break
                    
                nameModel = input("Indica el nombre del archivo en donde se almacenarán los clusters: ")
                
                
                while(True):
                    
    #                strNumClusters = input("Introduce el número de clusters a generar por entidad: ")
                    print("Introduce el rango de clusters a generar por entidad: \n")
                    inferiorL = input("Límite inferior: ")
                    superiorL = input("Límite superior: ")
                    
                    if(self.__isGoodNumber(inferiorL) and self.__isGoodNumber(superiorL)):
                        
    
                        limitInf = int(inferiorL)
                        limitSup = int(superiorL)
                        
                        if(limitInf <= limitSup):
                            
                            self.__printMensaje("Generando clusters... Espere")
                            
                            try: 
                                
                                listClusteringModel = []
                                for clusters in range(limitInf, limitSup + 1): 
                                    model = cluMod.ClusteringModel(self.__containerTraining, clusters, algoritmo)
                                    listClusteringModel.append(model)
        #                        dictModel = model.getModel()
                                self.__trainedModel = listClusteringModel
                                        
                                fullPathModelSaving = pathModelSaving + "/" + nameModel
                                self.__pickleFile(self.__trainedModel, fullPathModelSaving)
                                
                                break
                            
                            except:
                                
                                    system("clear")    
                                    self.__printMensaje("El número de clusters introducidos es mayor que el número de tweets de alguna entidad. "+
                                                            "Inténtelo de nuevo con otro número de clusters.")                            
                        else:
                            
                            system("clear")
                            if(limitInf > limitSup):
                                self.__printMensaje("El límite inferior debe ser menor que el límite superior. Inténtelo de nuevo.")
                                
                            if(limitSup < limitInf):
                                self.__printMensaje("El límite superior debe ser mayor que límite inferior. Inténtelo de nuevo.")

                    else:
                        
                        system("clear")
                        self.__printMensaje("Número de clusters introducido en formato erróneo. Inténtelo de nuevo. ")
                
                    
                system("clear")
                self.__printMensaje("Clusters generados. Guardado en " + fullPathModelSaving)
            
            else:
                
                system("clear")
                self.__printMensaje("No has cargado tweets procesados. Use la opción de cargar archivos para ello.")
                self.__keepExecutingOption = False
            
        if(chosenChar == OP_B):
            
            algoritmo = "agglomerative"

            if(self.__containerTraining != None):
            

                while(True): 
    
                    pathModelSaving = input("Indica la ruta de la carpeta en la que quieres guardar los clusters generados: ")
                    if(not checker.isdir(pathModelSaving)):
                        
                        system("clear")
                        self.__printMensaje("La carpeta especificada no existe. Creela e inténtelo de nuevo. ")
                        
                    else:
                        
                        break
                    
                nameModel = input("Indica el nombre del archivo en donde se almacenarán los clusters: ")
                
                
                while(True):
                    
    #                strNumClusters = input("Introduce el número de clusters a generar por entidad: ")
                    print("Introduce el rango de clusters a generar por entidad: \n")
                    inferiorL = input("Límite inferior: ")
                    superiorL = input("Límite superior: ")
                    
                    if(self.__isGoodNumber(inferiorL) and self.__isGoodNumber(superiorL)):
                        
    
                        limitInf = int(inferiorL)
                        limitSup = int(superiorL)
                        
                        if(limitInf <= limitSup):
                            
                            self.__printMensaje("Generando clusters... Espere")
                            
                            try: 
                                
                                listClusteringModel = []
                                for clusters in range(limitInf, limitSup + 1): 
                                        model = cluMod.ClusteringModel(self.__containerTraining, clusters, algoritmo)
                                        listClusteringModel.append(model)
            #                        dictModel = model.getModel()
                                self.__trainedModel = listClusteringModel
                                            
                                fullPathModelSaving = pathModelSaving + "/" + nameModel
                                self.__pickleFile(self.__trainedModel, fullPathModelSaving)
                                    
                                break
                            
                            except:
                                
                                    system("clear")    
                                    self.__printMensaje("El número de clusters introducidos es mayor que el número de tweets de alguna entidad. "+
                                                            "Inténtelo de nuevo con otro número de clusters.")                            
                        else:
                            
                            system("clear")
                            if(limitInf > limitSup):
                                self.__printMensaje("El límite inferior debe ser menor que el límite superior. Inténtelo de nuevo.")
                                
                            if(limitSup < limitInf):
                                self.__printMensaje("El límite superior debe ser mayor que límite inferior. Inténtelo de nuevo.")

                    else:
                        
                        system("clear")
                        self.__printMensaje("Número de clusters introducido en formato erróneo. Inténtelo de nuevo. ")
                
                    
                system("clear")
                self.__printMensaje("Clusters generados. Guardado en " + fullPathModelSaving)
            
            else:
                
                system("clear")
                self.__printMensaje("No has cargado tweets procesados. Use la opción de cargar archivos para ello.")
                self.__keepExecutingOption = False



        if(chosenChar == OP_C):
            
            system("clear")
            self.__keepExecutingOption = False
            
        
        if(chosenChar != OP_A and chosenChar != OP_B and chosenChar != OP_C):
            
            system("clear")
            self.__printMensaje(INVALID)
            
            

    # OP3 Generar salida
    def __printOptionThree(self):
        
        if(self.__containerTraining != None and self.__trainedModel != None):
            
            while(True):
                
                folderOutPutSaving = input("Indica la ruta de la carpeta en donde quieres guardar la "  + 
                                       "salida del sistema: ")
                nameOut = input("Indica la terminación del nombre del archivo de salida del sistema: ")
                
                if(checker.isdir(folderOutPutSaving)):
                    outGen.OutputGenerator(self.__containerTraining, self.__trainedModel, folderOutPutSaving, nameOut)
                    
                    system("clear")
                    self.__printMensaje("Salida guardada en la carpeta: " + folderOutPutSaving + "/" +nameOut)
                    break
                
                else:
                    
                    system("clear")
                    self.__printMensaje("La carpeta especificada no existe. Créela e inténtelo de nuevo. ")
            
        else:
            
            if(self.__containerTraining == None and self.__trainedModel == None):
                
                system("clear")
                self.__printMensaje("No has cargado tweets preprocesados ni clusters. " + 
                      "Carga tweets yy los clusters desde el menú de cargar archivos o bien "+ 
                      "obtén tweets nuevos y clusters nuevos nuevo.")
                
            else:
                
                
            
                if(self.__containerTraining == None):
                    
                    system("clear")
                    self.__printMensaje("No has cargado tweets procesados. Ve al menú de cargar archivos o" +
                          " preprocesa nuevos tweets para ello.")
                    
                if(self.__trainedModel == None):
                    
                    system("clear")
                    self.__printMensaje("No has cargado clusters ya generados. Ve al menú de cargar archivos o" + 
                          " genera nuevos clusters.")
            
#
#        
    def __printOptionFive(self):
#        
        while(True):
            option = input("Se limpiarán las variables dedicadas a referenciar los tweets procesados y a" + 
                                   "los clusters generados (si hubiere éstos). ¿Desea continuar con la operación? (S/N): ")
                    
            if(option == OPTION_YES):
                
                self.__clearContainers()
                self.__clearModel()
                self.__clearKeys()
                system("clear")
                self.__printMensaje("variables limpiadas")
                break
            
            if(option == OPTION_NO):
                
                system("clear")
                self.__printMensaje("Operación abortada. ")
                break
            
            if(option != OPTION_YES and option != OPTION_NO):
                
                system("clear")
                self.__printMensaje(INVALID)
            
    def __printOptionSix(self, chosenChar):
        
        if(chosenChar == OP_A):
            
            if(self.__yandexKey != None):

                    option = input("Ya hay una clave cargada para la herramienta de traducción. ¿Deseas introducir una nueva? (S/N): ")
                    
                    option = option.lower()
                    
                    if(option == OPTION_YES):
                        
                        while(True):
                            
                            key = input("Introduzca la clave para el acceso a la herramienta: ")
                            
                            print("\n")
                            if(self.__goodKeyYandex(key)):
                                
                                system("clear")
                                
                                self.__yandexKey = key
                                self.__printMensaje("Clave cargada")
                                break
                            else:
                                
                                system("clear")
                                self.__printMensaje("La clave que has introducido no es correcta o no está operativa. Inténtelo de nuevo. \n")


                        
                    if(option == OPTION_NO):
                        
                        system("clear")
                        self.__printMensaje("Operación abortada. ")
                        

                    if(option != OPTION_YES and option != OPTION_NO):
                        
                        system("clear")
                        self.__printMensaje(INVALID)
            else:
                
                while(True):
                    
                    key = input("Introduzca la clave para el acceso a la herramienta de traducción: ")
                    
                    if(self.__goodKeyYandex(key)):
                        
                        system("clear")
                                
                        self.__yandexKey = key
                        self.__printMensaje("Clave cargada")
                        break
                    
                    else:
                        
                        system("clear")
                        self.__printMensaje("La clave que has introducido no es correcta o no está operativa. Inténtelo de nuevo. \n")
    
                    #Comprobar si la clave es válida
                
        if(chosenChar == OP_B):
            
            self.__keepExecutingOption = False
                
        if(chosenChar != OP_A and chosenChar != OP_B):
            
            system("clear")
            self.__printMensaje(INVALID)
            
        
    def __printOptionSeven(self, chosenChar):
                
        if(chosenChar == OP_A):

            system("clear")
            print("La estructura de los directorios de entrada debe ser exactamente la siguiente: " + "\n")
            print("|")
            print("|-- tweets")
            print("       |")
            print("       | --RL2013D01E001")
            print("       | --RL2013D01E002")
            print("       | -- ...")

            
            print("Deberás tener en un directorio la carpeta 'tweets' para que puedas ejecutar las distintas opciones. \n")
            print("La carpeta tweets contendrá un archivo por entidad. Cada archivo deberá tener el siguiente formato: " + "\n")
            print("\t <Identificador tweet> \t <Entidad> \t <Idioma> \t <Cuerpo del tweet>" + "\n")
            

            
            
        if(chosenChar == OP_B):
#            get_ipython().magic('clear')
            system("clear")
            print("Cuando se le pida al usuario introducir alguna ruta, ésta debe ser absoluta, es decir, indicando la ruta completa hasta donde se ubique la carpeta o archivo requerido. \n")
            print("Por ejemplo, si suponemos que la carpeta 'tweets' está en el directorio Escritorio, el path a introducir sería uno de los siguientes: \n" + 
                  "/home/usuario/Escritorio/" + "   o bien   " + "\n" + 
                  "/home/usuario/Escritorio \n")
        if(chosenChar == OP_C):
#            get_ipython().magic('clear')
            system("clear")
            print("Con la opción 6 del menú principal podrás cargar las claves de acceso para hacer uso de la herramienta de traducción de Yandex. No podrás realizar " + 
                  "ningún tipo de preprocesamiento si no introduces dicha clave. \n")
            
        if(chosenChar == OP_D):
            
            self.__keepExecutingOption = False
            system("clear")
            
        if(chosenChar != OP_A and chosenChar != OP_B and chosenChar != OP_C and chosenChar != OP_D):
            
            system("clear")
            self.__printMensaje(INVALID)
            
    def __printMensaje(self, mensaje):
        
        print(HYPHENS  + "\n" +  mensaje.upper() + "\n" + HYPHENS + "\n")

        
    def __goodKeyYandex(self, key):
                    
        success = True
            
        trans = YandexTranslate(key)
            
        try:
                
            trans.translate("hola", "en")["text"][0]

        except:
                
            success = False
                
        return success            
            
    def __isGoodNumber(self, number):
        
        goodNumber = True
        
        try:
            
            int(number)
            
        except ValueError:
            
            goodNumber = False
            
        return goodNumber
        
            
