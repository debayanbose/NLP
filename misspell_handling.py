#    Spell Checking in Python
##############################################################################


import win32com.client 
msword = win32com.client.Dispatch("Word.Application") 
string = "their service is reall pathetik" 
T2=[]
T3=[]
for word in string.split(): 
    if msword.CheckSpelling(word): 
       #print "!%s! OK!" % word 
       T2.append(word)
       T3.append("OK")
    else: 
       #print "!%s! wrong!" % word
       T2.append(word)
       T3.append("Wrong")

spell=zip(T2,T3)
ok_word=[]
wrong_word=[]

for i in range(0,len(spell)):
        if spell[i][1]=="OK": #or post[i][1]=="NN":#or post[i][1]=="JJ" or post[i][1]=="ADV" # or post[i][1]=="NN" or post[i][1]=="VBN":
            a=spell[i][0]
            ok_word.append(a)
        else:
            b=spell[i][0]
            wrong_word.append(b)


# Misspelled to Spelled
############################################################################
import re, collections

def words(text): return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(file('C:\\big.txt').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

    


