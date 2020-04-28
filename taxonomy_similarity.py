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
                if pathsim != None:
                        print pathsim,wupsim


if __name__ == "__main__":
        #getSenseSimilarity('cat','walk')
        getSenseSimilarity('University','School')
        

from nltk.corpus import wordnet as wn
from itertools import product

def compare(word1, word2):
    ss1 = wn.synsets(word1)
    ss2 = wn.synsets(word2)
    return max(s1.wup_similarity(s2) for (s1, s2) in product(ss1, ss2))
        
        
from nltk import wordnet  
from nltk import wntools