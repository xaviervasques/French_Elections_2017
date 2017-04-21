# coding=utf-8

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import pandas as pd
import matplotlib.pyplot as plt

#Variables that contains the user credentials to access Twitter API
access_token = " #######"
access_token_secret = "########"
consumer_key = "###########"
consumer_secret = "############@"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print data
        return True
    
    def on_error(self, status):
        print status


if __name__ == '__main__':
    
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=[u"Macron",u"macron",u"emmanuel macron",u"Emmanuel Macron",u"@EmmanuelMacron", u"#Macron",u"Fillon",u"fillon",u"françois fillon",u"francois fillon",u"François Fillon", u"Francois Fillon",u"@FrancoisFillon",u"#Fillon",u"#FillonPresident",u"@francoisfillon",u"Le Pen",u"le pen",u"marine le pen",u"Marine Le Pen" u"@MLP_officiel",u"#MarineLePen",u"#Marine2017",u"Benoit Hamon",u"Benoît Hamon",u"benoit hamon",u"hamon",u"Hamon",u"@benoithamon",u"#Hamon2017",u"@AvecHamon2017",u"Jean-Luc Mélenchon",u"Melenchon",u"Mélenchon",u"jean-luc mélenchon",u"melenchon",u"mélenchon",u"@JLMelenchon",u"Jean Lassalle",u"jean lassalle",u"Lassalle",u"lassalle",u"@jeanlassalle",u"#Lassalle",u"Nicolas Dupont Aignan",u"nicolas dupont aignan",u"Dupont Aignan",u"dupont aignan",u"@DLF_Officiel",u"#DupontAignan",u"@dupontaignan",u"Nicolas Dupont-Aignan",u"Nathalie Arthaud",u"nathalie arthaud",u"Arthaud","arthaud",u"@n_arthaud",u"@N_Arthaud",u"Jacques Cheminade",u"jacques cheminade",u"Cheminade",u"cheminade",u"@JCheminade",u"#cheminade2017",u"François Asselineau",u"Francois Asselineau",u"Asselineau",u"asselineau",u"françois asselineau",u"francois asselineau",u"@UPR_Asselineau",u"Philippe Poutou",u"philippe poutou",u"Poutou",u"poutou",u"@PhilippePoutou",u"#Poutou2017"])







