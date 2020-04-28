import nltk
from nltk.corpus import wordnet as wn
from itertools import product

from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *
from nltk import Tree

document="I do not like that you have to turn the darned thing on every time you want to print. I have been printing on the machine since I set it up, now, all of a sudden, prompt comes up saving the printer is not connected. Ugh! I am 67 and handicapped so it is extremely difficult using the machine not to mention that now I am going to have to figure out what has happened with the connection."

#define the POS for each of the words
sentence = nltk.sent_tokenize(document) 
sentence = [nltk.word_tokenize(sent) for sent in sentence] 
sentence = [nltk.pos_tag(sent) for sent in sentence]

#define the required pareser for noun phrase extraction
noun_extract="NOUN: {<NNP|NN|NNS><NNP|NN|NNS>?<NNP|NN|NNS>?<NNP|NN|NNS>}"
cp = nltk.RegexpParser(noun_extract)
chunked = []
for s in sentence:
    chunked.append(cp.parse(s))

T2=[]
for j in range(0,len(chunked)):
    for i in range(0,len(chunked[j])):
        try:
            a=chunked[j][i].pos()
            T2.append(a)
        except:
            i=i+1
print T2

#Extract and clean the topic from POS tagged parse matrix
T4=[]
for k in range(0,len(T2)):
    T3=[]
    for l in range(0,len(T2[k])):
        key_term=T2[k][l][0][0]
        T3.append(key_term)
    T4.append(T3)
#Check in wordnet dictionary for possible Verb, Adjective/Adverb
T6=[]
for m in range(0,len(T4)):
    T5=[]
    for n in range(0,len(T4[m])):
        verb_synsets=wn.synsets(T4[m][n],pos=wn.VERB)
        adj_synsets=wn.synsets(T4[m][n],pos=wn.ADJ)
        adv_synsets=wn.synsets(T4[m][n],pos=wn.ADV)
        if (len(verb_synsets)<=2 and len(adj_synsets)<=2 and len(adv_synsets)<=2):
            key_term=T4[m][n]
            T5.append(key_term)
        else:
            T5.append([])
    T6.append(T5)

#Finalize key noun-phrase
key_np=[]
for p in range(0,2):
    T7=[]
    for q in range(0,2):
        if(T6[p][q]==T4[p][q]):
            key=T6[p][q]
            T7.append(key)
        else:
            p=p+1
            q=0
    if(len(T7)==len(T6[p])):
        key_np.append(T7)
            
#Extracting the single word themes
noun_extract="NOUN: {<NNP|NN|NNS>}"
cp = nltk.RegexpParser(noun_extract)
chunked = []
for s in sentence:
    chunked.append(cp.parse(s))

T2=[]
for j in range(0,len(chunked)):
    for i in range(0,len(chunked[j])):
        try:
            a=chunked[j][i].pos()
            T2.append(a)
        except:
            i=i+1
print T2

noun_theme=[]
for i in range(0,len(T2)):
    key_1=T2[i][0][0][0]
    noun_theme.append(key_1)
noun_theme=list(set(noun_theme))
