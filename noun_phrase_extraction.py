#       Extract two words theme using POS and bi-gram
#############################################################################
import nltk
from nltk.corpus import brown
import numpy as np
from itertools import chain 
from nltk.corpus import wordnet as wn


brown_train = brown.tagged_sents(categories='news')
regexp_tagger = nltk.RegexpTagger(
    [(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
     (r'(-|:|;)$', ':'),
     (r'\'*$', 'MD'),
     (r'(The|the|A|a|An|an)$', 'AT'),
     (r'.*able$', 'JJ'),
     (r'^[A-Z].*$', 'NNP'),
     (r'.*ness$', 'NN'),
     (r'.*ly$', 'RB'),
     (r'.*s$', 'NNS'),
     (r'.*ing$', 'VBG'),
     (r'.*ed$', 'VBD'),
     (r'.*', 'NN')
])
unigram_tagger = nltk.UnigramTagger(brown_train, backoff=regexp_tagger)
bigram_tagger = nltk.BigramTagger(brown_train, backoff=unigram_tagger)

 
cfg = {}
cfg["NNP+NNP"] = "NNP"
cfg["NN+NN"] = "NNI"
cfg["NNI+NN"] = "NNI"
cfg["JJ+JJ"] = "JJ"
cfg["JJ+NN"] = "NNI"

class NPExtractor(object):
 
    def __init__(self, sentence):
        self.sentence = sentence
 
    # Split the sentence into singlw words/tokens
    def tokenize_sentence(self, sentence):
        tokens = nltk.word_tokenize(sentence)
        return tokens
 
    # Normalize brown corpus' tags ("NN", "NN-PL", "NNS" > "NN")
    def normalize_tags(self, tagged):
        n_tagged = []
        for t in tagged:
            if t[1] == "NP-TL" or t[1] == "NP":
                n_tagged.append((t[0], "NNP"))
                continue
            if t[1].endswith("-TL"):
                n_tagged.append((t[0], t[1][:-3]))
                continue
            if t[1].endswith("S"):
                n_tagged.append((t[0], t[1][:-1]))
                continue
            n_tagged.append((t[0], t[1]))
        return n_tagged
 
    # Extract the main topics from the sentence
    def extract(self):
 
        tokens = self.tokenize_sentence(self.sentence)
        tags = self.normalize_tags(bigram_tagger.tag(tokens))
 
        merge = True
        while merge:
            merge = False
            for x in range(0, len(tags) - 1):
                t1 = tags[x]
                t2 = tags[x + 1]
                key = "%s+%s" % (t1[1], t2[1])
                value = cfg.get(key, '')
                if value:
                    merge = True
                    tags.pop(x)
                    tags.pop(x)
                    match = "%s %s" % (t1[0], t2[0])
                    pos = value
                    tags.insert(x, (match, pos))
                    break
 
        matches = []
        for t in tags:
            if t[1] == "NNP" or t[1] == "NNI":
            #if t[1] == "NNP" or t[1] == "NNI" or t[1] == "NN":
                matches.append(t[0])
        return matches
 
 
document = "This printer is awsome "


np_extractor = NPExtractor(document)
result = np_extractor.extract()
final=set(result)
theme=list(final)
sentence = nltk.sent_tokenize(document) 
sentence = [nltk.word_tokenize(sent) for sent in sentence] 
sentence = [nltk.pos_tag(sent) for sent in sentence]
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


################################################################################
# Identify key topic in a sentence. topic is different from theme
###############################################################################
noun_theme=[]
for i in range(0,len(T2)):
    key_1=T2[i][0][0][0]
    noun_theme.append(key_1)
noun_theme=list(set(noun_theme))

for k in range(0,len(noun_theme)):
    theme.append(noun_theme[k])


T4=[nltk.word_tokenize(sent) for sent in theme] 



T6=[]
for m in range(0,len(T4)):
    T5=[]
    for n in range(0,len(T4[m])):
        verb_synsets=wn.synsets(T4[m][n],pos=wn.VERB)
        adj_synsets=wn.synsets(T4[m][n],pos=wn.ADJ)
        adv_synsets=wn.synsets(T4[m][n],pos=wn.ADV)
        noun_synsets=wn.synsets(T4[m][n],pos=wn.NOUN)
        if (len(verb_synsets)<1 and len(adj_synsets)<1 and len(adv_synsets)<1 and len(noun_synsets)<3):
            key_term=T4[m][n]
            T5.append(key_term)
        else:
            T5.append([])
    T6.append(T5)
print T6

key_np=[]

for p in range(0,len(T6)):
    T7=[]
    q=0
    if(len(T6[p])>1):
        for q in range(0,len(T6[p])):
            try:
                if(T6[p][q]==T4[p][q]):
                    key=T6[p][q]
                    T7.append(key)
                
                else:
                    p=p+1
            except:
                p=p+1
                
    else:
        if(T6[p]==T4[p]):
            key=T6[p]
            T7.append(key)
        else:
            p=p+1
    try:
        if(len(T7)==len(T6[p])):
            key_np.append(T7)
            q=0
    except:
        q=0

final=[]
for k in range(0,len(key_np)):
    if(len(key_np[k])>1):
        documents = [' '.join(key_np[k])]
    else:
        documents = [' '.join(key_np[k][0])]
    final.append(documents)

topic= list(set((chain(*final))))