################################################################################
#            How to handle coreferencing in Python
################################################################################


import nltk as nk
import re
import scipy
import numpy as np

import csv
datafile = open('C:\data.csv', 'r')
datareader = csv.reader(datafile)
data1 = []
for row in datareader:
    data1.append(row)

data1=np.array(data1)
data2=data1[1:,1]
data3=list(data2)

list2 = [x for x in data3 if x != '']
stlist=["for","the"]
cnt=range(len(stlist))
word=[]

for i in range(0,len(list2)-1):
    words=re.findall(r'\w+', list2[i],flags = re.UNICODE | re.LOCALE)
    word.append(words)

wordlist=[]
b=[]
for i in range(0,len(word)-1):
    b=word[i]+b
wordlist.append(b)
    

def duplicateremove(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

stlist1=duplicateremove(wordlist[0])

#Create list of counts for each string list
T2=[]
cnt=range(0,len(stlist1))
b=range(0,len(list2))
c=[]
for i in range(0,len(list2)):
    for j in range(0,len(stlist1)):
        cnt=list2[i].count(stlist1[j])
        c.append(cnt)

string_part = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
count_list=string_part(c,len(stlist1))







str1="he is a nice man. The man is pretty good and he has a manly attitude. But the management skill is pathetic but technically he is brilliant"
list2 = re.split('[?!.][\s]*',str1)
T2=[]
for j in range(0,len(list2)):
    ttok=nk.word_tokenize(list2[j])
    post=nk.pos_tag(ttok)
    T1=[]
    for i in range(0,len(post)):
        if post[i][1]=="NNP" or post[i][1]=="NN":#or post[i][1]=="JJ" or post[i][1]=="ADV" # or post[i][1]=="NN" or post[i][1]=="VBN":
            a=post[i][0]
            T1.append(a)
    b=[" ".join(T1)]
    T2.append(b)



def kwdCount(textContent, keyword1,keyword2):
    lines=textContent.split("\n")
    count=len([1 for line in lines if line.find(keyword)!=-1])
    return count
    
    
#str2="hello world some words here goodbye world. He is a "
#lines=str2.split("\n")
#count1=len([1 for line in lines if line.find("he")!=-1])
#count2=len([1 for line in lines if line.find("hello")!=-1])
#if(count1>0 and count2>0):
    count3=1

from nltk.corpus import wordnet as wn


def getSenseSimilarity(worda,wordb):
        """
        find similarity betwwn word senses of two words
        """
        wordasynsets = wn.synsets(worda)
        wordbsynsets = wn.synsets(wordb)
        synsetnamea = [wn.synset(str(syns.name)) for syns in wordasynsets]
        synsetnameb = [wn.synset(str(syns.name)) for syns in wordbsynsets]
        T2=[]
        for sseta, ssetb in [(sseta,ssetb) for sseta in synsetnamea\
        for ssetb in synsetnameb]:
                pathsim = sseta.path_similarity(ssetb)
                wupsim = sseta.wup_similarity(ssetb)
                #if pathsim != None:
                #        print pathsim,wupsim


#if __name__ == "__main__":
        #getSenseSimilarity('cat','walk')
#        getSenseSimilarity('University','School')
        
score=0
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from itertools import product

def compare(word1, word2):
    ss1 = wn.synsets(word1)
    ss2 = wn.synsets(word2)
    try:
        score= max(s1.wup_similarity(s2) for (s1, s2) in product(ss1, ss2))
        return score
    except:
        score= 0
        return score
        
#str1="This has a software unit and hardware unit. It has license, support and services"
theme=["printer"]
lookup=["printing"] # include driver
themescore=[]
for thmlen in range(0,len(theme)):
    score=0
    for lkuplen in range(0,len(lookup)):
        try:
            synword1=wn.synsets(theme[thmlen])
            synword2=wn.synsets(lookup[lkuplen])
            intm_score=max(word1.wup_similarity(word2) for (word1,word2) in product(synword1,synword2))
            score=score + intm_score
        except:
            score=0
            
    themescore.append(score)
print themescore

from pattern.en import sentiment
print sentiment("Valve trying to stop consumers rights on Steam Gamo, on 31 July 2012 - 11:18 PM, said: jehurey, on 31 July 2012 - 11:12 PM, said: Is Valve putting a forced arbitration clause in their EULA? It doesn't really surprise me. Gabe Newell was a former Microsoft bigwig from the Windows heydays. I knew something was up when Randy Pritchford, a few years ago, was saying some rather odd remarks about the Steam service, but you could tell that he didn't want to say something that would get him in trouble. Gamers love Steam because of all these deals. Valve essentially forces developers into an environment in which the prices of their game tanks, and then Valve advertises it and they get all the credit. What do you mean forces the prices of their games to tank? You mean games that are 3+ years old or sell like complete shit - if it was not for steam most of those developers would have never made any money look at how much ArmA sold during the summer sale - game would have not sold otherwise I wonder how much the developer gets after Valve gets their cut It wouldn't surprise me if there isn't some sort of contractual agreement that Valve essentially controls the price of YOUR game after its been on the Steam service for X amount of time. Because we're seeing that after 12-18 months or so, all games tank in price down to $2.50-$9.99 And now Valve wants to control the USER-generated content through Steam. This is why they created DOTA. Because it serves as the vessel. People can create in-game items for a game, they sell it through the Steam marketplace, and Valve gets their cut for being the middle man. There is something very fishy with Steam. Gabe Newell is pissed because he knows that Windows 8 and Mac OS will have closed environments for applications. The App store is a threat to his store ")

        

