################################################################################
#
#Summary Extraction feature based on word frequency
#
#
################################################################################


from nltk.probability import FreqDist 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import nltk.data

    
   
input = "version. Those apps will dominate the distribution and monetization opportunities for Windows 8 for the next six months, and almost all of them need a keyboard. Another view is to consider what Microsoft has done as impressive. They are choosing to accommodate the desktop and keyboard legacy by creating a very portable and mobile accessory for keyboard integration. Thus Microsoft is saying not all Windows 8 experiences begin and end with touch and sensor technology, as is the case with today's tablets. With the Surface keyboard, Microsoft is questioning the status quo that tablets and desktop need to be worlds apart. Microsoft is instead showing OEMs you can have your cake and eat it too; i.e., Windows 8 can support tablet app use cases, and it can support the millions of desktop apps that are readily available to run. I could be guessing at all of this but recent Intel research points to Microsoft's integration to be on the right track. As explained in this article from Intel Free Press people were given the opportunity to use both touch and keyboard on an integrated device.The study found people like the combined integration when experiencing the keyboard with a touch device. “Many gave practical or emotional reasons for liking the physical keyboard, such as the way it feels or sounds when pressing down on the different keys. Most participants did not like interacting with the virtual keyboard, even when touch was their favorite input modality.” The way I see it, it’s not that Windows 8 isn’t cut out for tablet. It’s that Windows 8 is cut out for both tablet and desktop apps. Before Windows 8 that has always been a less than perfect integration, with keyboard as a novelty accessory to tablet, or clumsy touch-based devices that run Windows 7. The possibility is very real that properly mixing the best of desktop and tablet (as done with Windows 8 via devices like Surface and Ultrabooks) might be a bit of technical peanut butter and chocolate we've been waiting for. "

         
tokenizer = RegexpTokenizer('\w+')
    
# get the frequency of each word in the input
base_words = [word.lower() 
for word in tokenizer.tokenize(input)]
words = [word for word in base_words if word not in stopwords.words()]
word_frequencies = FreqDist(words)
    
# now create a set of the most frequent words
most_frequent_words = [pair[0] for pair in 
word_frequencies.items()[:5]]
    
        
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
actual_sentences = sent_detector.tokenize(input)
working_sentences = [sentence.lower() 
for sentence in actual_sentences]
    
output_sentences = []
num_sentences=6
    
for word in most_frequent_words:
    for i in range(0, len(working_sentences)):
        if (word in working_sentences[i] 
        and actual_sentences[i] not in output_sentences):
            output_sentences.append(actual_sentences[i])
            break
        if len(output_sentences) >= num_sentences: break
        if len(output_sentences) >= num_sentences: break
    
output_sentences.sort( lambda s1, s2:
    input.find(s1) - input.find(s2) )

summary= "  ".join(output_sentences)


