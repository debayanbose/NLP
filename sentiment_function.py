def sentiment(content):
    from pattern.en import parse, split, wordnet 
    wordnet.sentiment.load()
    relevant_types = ['JJ', 'VB', 'VBD','VBN','VBG' 'RB',] 
    score = 0
    sentences = split(parse(content, lemmata=True))
    for sentence in sentences:
        for word in sentence.words:
            if word.type in relevant_types:
                pos, neg, obj = wordnet.sentiment[word.lemma]
                score = score + ((pos - neg) * (1 - obj)) 
    #return 1 if score >= 0 else -1
    return score

f=sentiment("he is a very excellent guy")

import nltk
def extract_entities(text):
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'node'):
                print chunk.node, ' '.join(c[0] for c in chunk.leaves())
                

extract_entities("Valve trying to stop consumers rights on Steam Gamo, on 31 July 2012 - 11:18 PM, said: jehurey, on 31 July 2012 - 11:12 PM, said: Is Valve putting a forced arbitration clause in their EULA? It doesn't really surprise me. Gabe Newell was a former Microsoft bigwig from the Windows heydays. I knew something was up when Randy Pritchford, a few years ago, was saying some rather odd remarks about the Steam service, but you could tell that he didn't want to say something that would get him in trouble. Gamers love Steam because of all these deals. Valve essentially forces developers into an environment in which the prices of their game tanks, and then Valve advertises it and they get all the credit. What do you mean forces the prices of their games to tank? You mean games that are 3+ years old or sell like complete shit - if it was not for steam most of those developers would have never made any money look at how much ArmA sold during the summer sale - game would have not sold otherwise I wonder how much the developer gets after Valve gets their cut It wouldn't surprise me if there isn't some sort of contractual agreement that Valve essentially controls the price of YOUR game after its been on the Steam service for X amount of time. Because we're seeing that after 12-18 months or so, all games tank in price down to $2.50-$9.99 And now Valve wants to control the USER-generated content through Steam. This is why they created DOTA. Because it serves as the vessel. People can create in-game items for a game, they sell it through the Steam marketplace, and Valve gets their cut for being the middle man. There is something very fishy with Steam. Gabe Newell is pissed because he knows that Windows 8 and Mac OS will have closed environments for applications. The App store is a threat to his store")
sentiment("HP products are pathetic and bad worse horrible ")
