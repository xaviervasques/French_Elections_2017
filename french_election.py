# coding=utf-8

import json
import pandas as pd
import matplotlib.pyplot as plt
import re


tweets_data_path = '/Users/Xavi/Desktop/tweets_data_3.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue


# Nombre de tweets
print "##########################################################################"
print "Le nombre total de tweets est : %i" %(len(tweets_data))
print "##########################################################################"
print "\n"


# On utilise panda pour mettre les données dans un data frame
tweets = pd.DataFrame()

# Trois colonnes pour le texte du tweet, la langue et le pays
tweets['text'] = map(lambda tweet: tweet.get('text', None),tweets_data)
tweets['lang'] = map(lambda tweet: tweet.get('lang', None),tweets_data)
tweets['place'] = map(lambda tweet: tweet.get('place', None),tweets_data)

# Langue
tweets_by_lang = tweets['lang'].value_counts()
#fig, ax = plt.subplots()
#ax.tick_params(axis='x', labelsize=15)
#ax.tick_params(axis='y', labelsize=10)
#ax.set_xlabel('Languages', fontsize=15)
#ax.set_ylabel('Number of tweets' , fontsize=15)
#ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
#tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
#plt.show()

print "##########################################################################"
print "Langues des tweets "
print "##########################################################################"
print tweets_by_lang[:5]
print "\n"

# Places
tweets_by_country = tweets['place'].value_counts()
#fig, ax = plt.subplots()
#ax.tick_params(axis='x', labelsize=15)
#ax.tick_params(axis='y', labelsize=10)
#ax.set_xlabel('Places', fontsize=15)
#ax.set_ylabel('Number of tweets' , fontsize=15)
#ax.set_title('Top 20 places', fontsize=15, fontweight='bold')
#tweets_by_country[:20].plot(ax=ax, kind='bar', color='blue')
#plt.show()

#print "#####################################"
#print "Localisation des tweets "
#print "#####################################"
#print tweets_by_country[:20]
print "\n"


# Trouver les noms qui nous intéressent et les compter
def word_in_text(word,text):
    if text == None:
        return False
    word = word.lower()
    text = text.lower()
    match = re.search(word,text)
    if match:
        return True
    else:
        return False

print "##########################################################################"
print "Classement des candidats"
print "##########################################################################"

# Candidat Macron
tweets['macron'] = tweets['text'].apply(lambda tweet: word_in_text('macron', tweet))
tweets['Macron'] = tweets['text'].apply(lambda tweet: word_in_text('Macron', tweet))
tweets['emmanuel macron'] = tweets['text'].apply(lambda tweet: word_in_text('emmanuel macron', tweet))
tweets['@EmmanuelMacron'] = tweets['text'].apply(lambda tweet: word_in_text('@EmmanuelMacron', tweet))
tweets['#Macron'] = tweets['text'].apply(lambda tweet: word_in_text('#Macron', tweet))
tweets['Emmanuel Macron'] = tweets['text'].apply(lambda tweet: word_in_text('Emmanuel Macron', tweet))

macron = tweets['macron'].value_counts()[True] + tweets['Macron'].value_counts()[True] + tweets['emmanuel macron'].value_counts()[True] + tweets['@EmmanuelMacron'].value_counts()[True] + tweets['#Macron'].value_counts()[True] + tweets['Emmanuel Macron'].value_counts()[True]

print "Nombre de tweet pour le candidat Emmanuel Macron = %i"%macron

# Candidat Fillon
tweets['Fillon'] = tweets['text'].apply(lambda tweet: word_in_text('Fillon', tweet))
tweets['fillon'] = tweets['text'].apply(lambda tweet: word_in_text('fillon', tweet))
tweets['françois fillon'] = tweets['text'].apply(lambda tweet: word_in_text('françois fillon', tweet))
tweets['François Fillon'] = tweets['text'].apply(lambda tweet: word_in_text('François Fillon', tweet))
tweets['@FrancoisFillon'] = tweets['text'].apply(lambda tweet: word_in_text('@FrancoisFillon', tweet))
tweets['#Fillon'] = tweets['text'].apply(lambda tweet: word_in_text('#Fillon', tweet))
tweets['@francoisfillon'] = tweets['text'].apply(lambda tweet: word_in_text('@francoisfillon', tweet))
tweets['Francois Fillon'] = tweets['text'].apply(lambda tweet: word_in_text('Francois Fillon', tweet))

fillon = tweets['Fillon'].value_counts()[True] + tweets['fillon'].value_counts()[True] + tweets['@FrancoisFillon'].value_counts()[True] + tweets['#Fillon'].value_counts()[True] + tweets['@francoisfillon'].value_counts()[True] + tweets['Francois Fillon'].value_counts()[True]


print "Nombre de tweet pour le candidat François Fillon = %i"%fillon

# Candidat Hamon
tweets['Benoit Hamon'] = tweets['text'].apply(lambda tweet: word_in_text('Benoit Hamon', tweet))
tweets['Benoît Hamon'] = tweets['text'].apply(lambda tweet: word_in_text('Benoît Hamon', tweet))
tweets['benoit hamon'] = tweets['text'].apply(lambda tweet: word_in_text('benoit hamon', tweet))
tweets['hamon'] = tweets['text'].apply(lambda tweet: word_in_text('hamon', tweet))
tweets['Hamon'] = tweets['text'].apply(lambda tweet: word_in_text('Hamon', tweet))
tweets['@benoithamon'] = tweets['text'].apply(lambda tweet: word_in_text('@benoithamon', tweet))
tweets['#Hamon2017'] = tweets['text'].apply(lambda tweet: word_in_text('#Hamon2017', tweet))
tweets['@AvecHamon2017'] = tweets['text'].apply(lambda tweet: word_in_text('@AvecHamon2017', tweet))

hamon = tweets['Benoit Hamon'].value_counts()[True] + tweets['benoit hamon'].value_counts()[True] + tweets['hamon'].value_counts()[True] + tweets['Hamon'].value_counts()[True] + tweets['@benoithamon'].value_counts()[True] + tweets['#Hamon2017'].value_counts()[True] + tweets['@AvecHamon2017'].value_counts()[True]

print "Nombre de tweet pour le candidat Benoît Hamon = %i"%hamon


# Candidat Melenchon
tweets['Jean-Luc Melenchon'] = tweets['text'].apply(lambda tweet: word_in_text('Jean-Luc Melenchon', tweet))
tweets['Melenchon'] = tweets['text'].apply(lambda tweet: word_in_text('Melenchon', tweet))
tweets['jean-luc melenchon'] = tweets['text'].apply(lambda tweet: word_in_text('jean-luc melenchon', tweet))
tweets['melenchon'] = tweets['text'].apply(lambda tweet: word_in_text('melenchon', tweet))
tweets['@JLMelenchon'] = tweets['text'].apply(lambda tweet: word_in_text('@JLMelenchon', tweet))

melenchon = tweets['Jean-Luc Melenchon'].value_counts()[True] + tweets['Melenchon'].value_counts()[True] + tweets['jean-luc melenchon'].value_counts()[True] + tweets['melenchon'].value_counts()[True] + tweets['@JLMelenchon'].value_counts()[True]

print "Nombre de tweet pour le candidat Jean-Luc Mélenchon = %i"%melenchon

# Candidat Lassalle
tweets['Jean Lassalle'] = tweets['text'].apply(lambda tweet: word_in_text('Jean Lassalle', tweet))
tweets['jean lassalle'] = tweets['text'].apply(lambda tweet: word_in_text('jean lassalle', tweet))
tweets['Lassalle'] = tweets['text'].apply(lambda tweet: word_in_text('Lassalle', tweet))
tweets['lassalle'] = tweets['text'].apply(lambda tweet: word_in_text('lassalle', tweet))
tweets['@jeanlassalle'] = tweets['text'].apply(lambda tweet: word_in_text('@jeanlassalle', tweet))
tweets['#Lassalle'] = tweets['text'].apply(lambda tweet: word_in_text('#Lassalle', tweet))

lassalle = tweets['Jean Lassalle'].value_counts()[True] + tweets['jean lassalle'].value_counts()[True] + tweets['Lassalle'].value_counts()[True] + tweets['lassalle'].value_counts()[True] + tweets['@jeanlassalle'].value_counts()[True] + tweets['#Lassalle'].value_counts()[True]

print "Nombre de tweet pour le candidat Jean Lassalle = %i"%lassalle

# Candidat Aignan
tweets['Nicolas Dupont Aignan'] = tweets['text'].apply(lambda tweet: word_in_text('Nicolas Dupont Aignan', tweet))
tweets['nicolas dupont aignan'] = tweets['text'].apply(lambda tweet: word_in_text('nicolas dupont aignan', tweet))
tweets['Dupont Aignan'] = tweets['text'].apply(lambda tweet: word_in_text('Dupont Aignan', tweet))
tweets['dupont aignan'] = tweets['text'].apply(lambda tweet: word_in_text('dupont aignan', tweet))
tweets['@DLF_Officiel'] = tweets['text'].apply(lambda tweet: word_in_text('@DLF_Officiel', tweet))
tweets['#DupontAignan'] = tweets['text'].apply(lambda tweet: word_in_text('#DupontAignan', tweet))
tweets['@dupontaignan'] = tweets['text'].apply(lambda tweet: word_in_text('@dupontaignan', tweet))
tweets['Nicolas Dupont-Aignan'] = tweets['text'].apply(lambda tweet: word_in_text('Nicolas Dupont-Aignan', tweet))

aignan = tweets['Nicolas Dupont Aignan'].value_counts()[True] + tweets['nicolas dupont aignan'].value_counts()[True] + tweets['Dupont Aignan'].value_counts()[True] + tweets['dupont aignan'].value_counts()[True] + tweets['@DLF_Officiel'].value_counts()[True] + tweets['#DupontAignan'].value_counts()[True] + tweets['@dupontaignan'].value_counts()[True] + tweets['Nicolas Dupont-Aignan'].value_counts()[True]

print "Nombre de tweet pour le candidat Nicolas Dupont Aignan = %i"%aignan

# Candidat Arthaud
tweets['Nathalie Arthaud'] = tweets['text'].apply(lambda tweet: word_in_text('Nathalie Arthaud', tweet))
tweets['nathalie arthaud'] = tweets['text'].apply(lambda tweet: word_in_text('nathalie arthaud', tweet))
tweets['Arthaud'] = tweets['text'].apply(lambda tweet: word_in_text('Arthaud', tweet))
tweets['arthaud'] = tweets['text'].apply(lambda tweet: word_in_text('arthaud', tweet))
tweets['@n_arthaud'] = tweets['text'].apply(lambda tweet: word_in_text('@n_arthaud', tweet))
tweets['@N_Arthaud'] = tweets['text'].apply(lambda tweet: word_in_text('@N_Arthaud', tweet))
tweets['#arthaud'] = tweets['text'].apply(lambda tweet: word_in_text('#arthaud', tweet))

arthaud = tweets['Nathalie Arthaud'].value_counts()[True] + tweets['nathalie arthaud'].value_counts()[True] + tweets['Arthaud'].value_counts()[True] + tweets['arthaud'].value_counts()[True] + tweets['@n_arthaud'].value_counts()[True] + tweets['@N_Arthaud'].value_counts()[True] + tweets['#arthaud'].value_counts()[True]

print "Nombre de tweet pour la candidate Nathalie Arthaud = %i"%arthaud


# Candidat Cheminade
tweets['Jacques Cheminade'] = tweets['text'].apply(lambda tweet: word_in_text('Jacques Cheminade', tweet))
tweets['jacques cheminade'] = tweets['text'].apply(lambda tweet: word_in_text('jacques cheminade', tweet))
tweets['Cheminade'] = tweets['text'].apply(lambda tweet: word_in_text('Cheminade', tweet))
tweets['cheminade'] = tweets['text'].apply(lambda tweet: word_in_text('cheminade', tweet))
tweets['@JCheminade'] = tweets['text'].apply(lambda tweet: word_in_text('@JCheminade', tweet))
tweets['#cheminade2017'] = tweets['text'].apply(lambda tweet: word_in_text('#cheminade2017', tweet))

cheminade = tweets['Jacques Cheminade'].value_counts()[True] + tweets['jacques cheminade'].value_counts()[True] + tweets['Cheminade'].value_counts()[True] + tweets['cheminade'].value_counts()[True] + tweets['@JCheminade'].value_counts()[True] + tweets['#cheminade2017'].value_counts()[True]

print "Nombre de tweet pour le candidat Jacques Cheminade = %i"%cheminade

# Candidat Asselineau
tweets['Francois Asselineau'] = tweets['text'].apply(lambda tweet: word_in_text('Francois Asselineau', tweet))
tweets['Asselineau'] = tweets['text'].apply(lambda tweet: word_in_text('Asselineau', tweet))
tweets['asselineau'] = tweets['text'].apply(lambda tweet: word_in_text('asselineau', tweet))
tweets['francois asselineau'] = tweets['text'].apply(lambda tweet: word_in_text('francois asselineau', tweet))
tweets['@UPR_Asselineau'] = tweets['text'].apply(lambda tweet: word_in_text('@UPR_Asselineau', tweet))
tweets['#cheminade2017'] = tweets['text'].apply(lambda tweet: word_in_text('#cheminade2017', tweet))

asselineau = tweets['Jacques Cheminade'].value_counts()[True] + tweets['jacques cheminade'].value_counts()[True] + tweets['Cheminade'].value_counts()[True] + tweets['cheminade'].value_counts()[True] + tweets['@JCheminade'].value_counts()[True] + tweets['#cheminade2017'].value_counts()[True]

print "Nombre de tweet pour le candidat Francois Asselineau = %i"%asselineau

# Candidat Poutou
tweets['Philippe Poutou'] = tweets['text'].apply(lambda tweet: word_in_text('Philippe Poutou', tweet))
tweets['philippe poutou'] = tweets['text'].apply(lambda tweet: word_in_text('philippe poutou', tweet))
tweets['Poutou'] = tweets['text'].apply(lambda tweet: word_in_text('Poutou', tweet))
tweets['poutou'] = tweets['text'].apply(lambda tweet: word_in_text('poutou', tweet))
tweets['@PhilippePoutou'] = tweets['text'].apply(lambda tweet: word_in_text('@PhilippePoutou', tweet))
tweets['#Poutou2017'] = tweets['text'].apply(lambda tweet: word_in_text('#Poutou2017', tweet))

poutou = tweets['Philippe Poutou'].value_counts()[True] + tweets['philippe poutou'].value_counts()[True] + tweets['Poutou'].value_counts()[True] + tweets['poutou'].value_counts()[True] + tweets['@PhilippePoutou'].value_counts()[True] + tweets['#Poutou2017'].value_counts()[True]

print "Nombre de tweet pour le candidat Philippe Poutou = %i"%poutou

# Candidate Le Pen
tweets['Le Pen'] = tweets['text'].apply(lambda tweet: word_in_text('Le Pen', tweet))
tweets['le pen'] = tweets['text'].apply(lambda tweet: word_in_text('le pen', tweet))
tweets['marine le pen'] = tweets['text'].apply(lambda tweet: word_in_text('marine le pen', tweet))
tweets['Marine Le Pen'] = tweets['text'].apply(lambda tweet: word_in_text('Marine Le Pen', tweet))
tweets['@MLP_officiel'] = tweets['text'].apply(lambda tweet: word_in_text('@MLP_officiel', tweet))
tweets['#MarineLePen'] = tweets['text'].apply(lambda tweet: word_in_text('#MarineLePen', tweet))
tweets['#Marine2017'] = tweets['text'].apply(lambda tweet: word_in_text('#Marine2017', tweet))

lepen = tweets['Le Pen'].value_counts()[True] + tweets['le pen'].value_counts()[True] + tweets['marine le pen'].value_counts()[True] + tweets['Marine Le Pen'].value_counts()[True] + tweets['@MLP_officiel'].value_counts()[True] + tweets['#MarineLePen'].value_counts()[True] + tweets['#Marine2017'].value_counts()[True]

print "Nombre de tweet pour la candidate Marine Le Pen = %i"%lepen

print "\n"

print "##########################################################################"
print "Classement #NomDuCandidatPresident"
print "##########################################################################"

# Candidat Poutou
tweets['#MacronPresident'] = tweets['text'].apply(lambda tweet: word_in_text('#MacronPresident', tweet))
tweets['#MarinePresidente'] = tweets['text'].apply(lambda tweet: word_in_text('#MarinePresidente', tweet))
tweets['#MelenchonPresident'] = tweets['text'].apply(lambda tweet: word_in_text('#MelenchonPresident', tweet))
tweets['#PoutouPresident'] = tweets['text'].apply(lambda tweet: word_in_text('#PoutouPresident', tweet))
tweets['#HamonPresident'] = tweets['text'].apply(lambda tweet: word_in_text('#HamonPresident', tweet))
tweets['#AsselineauPresident'] = tweets['text'].apply(lambda tweet: word_in_text('#AsselineauPresident', tweet))
tweets['#CheminadePresident'] = tweets['text'].apply(lambda tweet: word_in_text('#CheminadePresident', tweet))
tweets['#ArthaudPresidente'] = tweets['text'].apply(lambda tweet: word_in_text('#ArthaudPresidente', tweet))
tweets['#NDAPresident'] = tweets['text'].apply(lambda tweet: word_in_text('#NDAPresident', tweet))
tweets['#LassallePresident'] = tweets['text'].apply(lambda tweet: word_in_text('#LassallePresident', tweet))
tweets['#FillonPresident'] = tweets['text'].apply(lambda tweet: word_in_text('#FillonPresident', tweet))

MacronPresident = tweets['#MacronPresident'].value_counts()[True]
FillonPresident = tweets['#FillonPresident'].value_counts()[True]
MarinePresidente = tweets['#MarinePresidente'].value_counts()[True]
#NDAPresident = tweets['#NDAPresident'].value_counts()[True]
#ArthaudPresidente = tweets['#ArthaudPresidente'].value_counts()[True]
#CheminadePresident = tweets['#CheminadePresident'].value_counts()[True]
#AsselineauPresident = tweets['#AsselineauPresident'].value_counts()[True]
#PoutouPresident = tweets['#PoutouPresident'].value_counts()[True]
#HamonPresident = tweets['#HamonPresident'].value_counts()[True]
#MelenchonPresident = tweets['#MelenchonPresident'].value_counts()[True]
#LassallePresident = tweets['#LassallePresident'].value_counts()[True]

print "Nombre de #MacronPresident = %i"%MacronPresident
print "Nombre de #FillonPresident = %i"%FillonPresident
print "Nombre de #MarinePresidente = %i"%MarinePresidente
print "Nombre de #NDAPresident = %i"%NDAPresident
print "Nombre de #ArthaudPresidente = %i"%ArthaudPresidente
print "Nombre de #CheminadePresident = %i"%CheminadePresident
print "Nombre de #AsselineauPresident = %i"%AsselineauPresident
print "Nombre de #PoutouPresident = %i"%PoutouPresident
print "Nombre de #HamonPresident = %i"%HamonPresident
print "Nombre de #MelenchonPresident = %i"%MelenchonPresident
print "Nombre de #LassallePresident = %i"%LassallePresident

print "\n"




# Plot it
#prg_langs = ['macron', 'fillon', 'le pen']
#tweets_by_prg_lang = [tweets['macron'].value_counts()[True], tweets['fillon'].value_counts()[True], tweets['le pen'].value_counts()[True]]

#x_pos = list(range(len(prg_langs)))
#width = 0.8
#fig, ax = plt.subplots()
#plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# Setting axis labels and ticks
#ax.set_ylabel('Number of tweets', fontsize=15)
#ax.set_title('Ranking: Macron vs. Fillon vs. Le Pen (Raw data)', fontsize=10, fontweight='bold')
#ax.set_xticks([p + 0.4 * width for p in x_pos])
#ax.set_xticklabels(prg_langs)
#plt.grid()
#plt.show()


















