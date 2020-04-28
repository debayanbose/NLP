import numpy as np


list1="Hp has great products and service is exceptional. Orders are placed one day and delivered the next, and promotions are the best in the industry."

list2=re.findall(r'\w+', list1,flags = re.UNICODE | re.LOCALE)
#word.append(words)



T21=[]

for j in range(0,len(list2)):
    ttok=nk.word_tokenize(list2[j])
    post=nk.pos_tag(ttok)
    T21.append(post)
T1=[]
for i in range(0,len(T21)):
    T2=np.array(T21[i])
    if(T2[0][1]==T2[0][1]=="VBD" or T2[0][1]=="VBG"):
        a=T2[0][0]
    else:
        i=i+1
    T1.append(a)
lookup=list(set(T1))


theme=["recommend","satisfy"]
#lookup=["suggest","pleased"]

themescore=[]
for thmlen in range(0,len(theme)):
    score=0
    for lkuplen in range(0,len(lookup)):
        try:
            synword1=wn.synsets(theme[thmlen])
            synword2=wn.synsets(lookup[lkuplen])
            intm_score=max(word1.wup_similarity(word2) for (word1,word2) in product(synword1,synword2))
            score=score+intm_score
        except:
            score=0
    themescore.append(score/len(lookup))
print themescore  
#print lookup 




