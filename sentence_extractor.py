################################################################################
#           Information Extraction using delimiter
#
#Things to use in punctuation: . ; : , ? ! - () [] {} and but however moreover
#
#Hierarchy: () {} [] treated separately
#. ? ! next hierarchy
#; , - 
#
################################################################################

import re
import numpy as np
str1= "Ram and Shyam and Kamal are going and they are singing but not dancing. He is going and singing"
Sentences1 = re.split('[?!.][\s]*',str1)

T3=[]
for j in range(0,len(Sentences)):
    
    Sentences = re.split('and|but',Sentences1[j])
    segments=np.str(0)
    segment=np.str(0)
    T2=[]
    i=0
    while (i < len(Sentences)):
        if(len(re.findall(r'\w+', Sentences[i]))>=3):
            T2.append(Sentences[i])
            i=i+1
        else:
            if (i < len(Sentences)-1):
                segments1=segments+Sentences[i]+Sentences[i+1]
                i=i+1
                while(len(re.findall(r'\w+', segments1))< 3):
                    segments1=segments1+Sentences[i+1]
                    i=i+1
            else:
                segments1=Sentences[i]
    
            T2.append(segments1)
            segments=segments1
            i=i+1
    T3.append(T2)
    
