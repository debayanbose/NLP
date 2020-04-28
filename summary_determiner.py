# coding=UTF-8
from __future__ import division
import re
 
 
class SummaryTool(object):
 

    def split_content_to_sentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")
 

    def split_content_to_paragraphs(self, content):
        return content.split("\n\n")
 

    def sentences_intersection(self, sent1, sent2):
 

        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))
 

        if (len(s1) + len(s2)) == 0:
            return 0
 

        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)
 

    def format_sentence(self, sentence):
        sentence = re.sub(r'\W+', '', sentence)
        return sentence

    def get_senteces_ranks(self, content):
 
        
        sentences = self.split_content_to_sentences(content)
 

        n = len(sentences)
        values = [[0 for x in xrange(n)] for x in xrange(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])
 


        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.format_sentence(sentences[i])] = score
        return sentences_dic
 
    # Return the best sentence in a paragraph
    def get_best_sentence(self, paragraph, sentences_dic):
 
        # Split the paragraph into sentences
        sentences = self.split_content_to_sentences(paragraph)
 
        # Ignore short paragraphs
        if len(sentences) < 2:
            return ""
 
        # Get the best sentence according to the sentences dictionary
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s
 
        return best_sentence
 
    # Build the summary
    def get_summary(self, title, content, sentences_dic):
 
        # Split the content into paragraphs
        paragraphs = self.split_content_to_paragraphs(content)
 
        # Add the title
        summary = []
        summary.append(title.strip())
        summary.append("")
 
        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)
 
        return ("\n").join(summary)
 
 
def main():
 
   
    title = """
    Dolphin
    """
 
    content1 = """
    Evolution
    See also: Evolution of cetaceans
    Dolphins, along with whales and porpoises, are descendants of terrestrial mammals, most likely of the Artiodactyl order. The ancestors of the modern-day dolphins entered the water roughly 50 million years ago, in the Eocene epoch.
    
    
    Hind limb buds are apparent on an embryo of a spotted dolphin in the fifth week of development as small bumps (hind limb buds) near the base of the tail. The pin is approximately 2.5 cm (1.0 in) long.
    
    Modern dolphin skeletons have two small, rod-shaped pelvic bones thought to be vestigial hind limbs. In October 2006, an unusual bottlenose dolphin was captured in Japan; it had small fins on each side of its genital slit, which scientists believe to be a more pronounced development of these vestigial hind limbs.[21]
    
    Anatomy
    Dolphins have a streamlined fusiform body, adapted for fast swimming. The tail fin, called the fluke, is used for propulsion, while the pectoral fins together with the entire tail section provide directional control. The dorsal fin, in those species that have one, provides stability while swimming. Though it varies by species, basic coloration patterns are shades of grey, usually with a lighter underside, often with lines and patches of different hue and contrast.
    
    The head contains the melon, a round organ used for echolocation. In many species, elongated jaws form a distinct beak; species such as the bottlenose have a curved mouth which looks like a fixed smile. Some species have up to 250 teeth. Dolphins breathe through a blowhole on top of their head. The trachea is anterior to the brain. The dolphin brain is large and highly complex, and is different in structure from that of most land mammals.
    
    Unlike most mammals, dolphins do not have hair, except for a few hairs around the tip of their rostrum (beak) which they lose shortly before or after birth.[22] The only exception to this is the Boto river dolphin, which has persistent small hairs on the rostrum.[23]
    
    Dolphins' reproductive organs are located on the underside of the body. Males have two slits, one concealing the penis and one further behind for the anus.[24] The female has one genital slit, housing the vagina and the anus. Two mammary slits are positioned on either side of the female's genital slit.[25][26][27]
    Though the exact methods used to achieve this are not known, dolphins can tolerate and recover from extreme injuries, such as shark bites. The healing process is rapid and even very deep wounds do not cause dolphins to hemorrhage to death. Furthermore, even gaping wounds restore in such a way that the animal's body shape is restored, and infection of such large wounds seems rare.[28]
    
    A study at the U.S. National Marine Mammal Foundation revealed that dolphins, like humans, develop a natural form of type 2 diabetes, which may lead to a better understanding of the disease and new treatments for both humans and dolphins.[29]
    
    Senses
    Most dolphins have acute eyesight, both in and out of the water, and they can hear frequencies ten times or more above the upper limit of adult human hearing.[30] Though they have a small ear opening on each side of their head, it is believed hearing underwater is also, if not exclusively, done with the lower jaw, which conducts sound to the middle ear via a fat-filled cavity in the lower jaw bone. Hearing is also used for echolocation, which all dolphins have. Dolphin teeth are believed to function as antennae to receive incoming sound and to pinpoint the exact location of an object.[31] Beyond locating an object, echolocation also provides the animal with an idea on the object's shape and size, though how exactly this works is not yet understood.[32] The Indus Dolphin is effectively blind. This may be because not much light penetrates the waters of the Indus river (due to suspended sediments), making eyes futile.[33]
    
    The dolphin's sense of touch is also well-developed, with free nerve endings densely packed in the skin, especially around the snout, pectoral fins and genital area. However, dolphins lack an olfactory nerve and lobes, and thus are believed to have no sense of smell.[34] They do have a sense of taste and show preferences for certain kinds of fish. Since dolphins spend most of their time below the surface, tasting the water could function like smelling, in that substances in the water can signal the presence of objects that are not in the dolphin’s mouth.
    
    Though most dolphins do not have hair, they do have hair follicles that may perform some sensory function.[35] The small hairs on the rostrum of the Boto river dolphin are believed to function as a tactile sense possibly to compensate for the Boto's poor eyesight.[36]
    
    Behavior
    
    
    
    A pod of Indo-Pacific bottlenose dolphins in the Red Sea.
    See also: Whale surfacing behaviour
    Dolphins are often regarded as one of Earth's most intelligent animals, though it is hard to say just how intelligent. Comparing species' relative intelligence is complicated by differences in sensory apparatus, response modes, and nature of cognition. Furthermore, the difficulty and expense of experimental work with large aquatic animals has so far prevented some tests and limited sample size and rigor in others. Compared to many other species, however, dolphin behavior has been studied extensively, both in captivity and in the wild. See cetacean intelligence for more details.
    
    """
 
    content="Valve trying to stop consumers rights on Steam Gamo, on 31 July 2012 - 11:18 PM, said: jehurey, on 31 July 2012 - 11:12 PM, said: Is Valve putting a forced arbitration clause in their EULA? It doesn't really surprise me. Gabe Newell was a former Microsoft bigwig from the Windows heydays. I knew something was up when Randy Pritchford, a few years ago, was saying some rather odd remarks about the Steam service, but you could tell that he didn't want to say something that would get him in trouble. Gamers love Steam because of all these deals. Valve essentially forces developers into an environment in which the prices of their game tanks, and then Valve advertises it and they get all the credit. What do you mean forces the prices of their games to tank? You mean games that are 3+ years old or sell like complete shit - if it was not for steam most of those developers would have never made any money look at how much ArmA sold during the summer sale - game would have not sold otherwise I wonder how much the developer gets after Valve gets their cut It wouldn't surprise me if there isn't some sort of contractual agreement that Valve essentially controls the price of YOUR game after its been on the Steam service for X amount of time. Because we're seeing that after 12-18 months or so, all games tank in price down to $2.50-$9.99 And now Valve wants to control the USER-generated content through Steam. This is why they created DOTA. Because it serves as the vessel. People can create in-game items for a game, they sell it through the Steam marketplace, and Valve gets their cut for being the middle man. There is something very fishy with Steam. Gabe Newell is pissed because he knows that Windows 8 and Mac OS will have closed environments for applications. The App store is a threat to his store"
    st = SummaryTool()
 
    sentences_dic = st.get_senteces_ranks(content)
 
    
    summary = st.get_summary(title, content, sentences_dic)
 

    print summary
 

 #   print ""
 #   print "Original Length %s" % (len(title) + len(content))
 #   print "Summary Length %s" % len(summary)
 #   print "Summary Ratio: %s" % (100 - (100 * (len(summary) / (len(title) + len(content)))))
 
 
#if __name__ == '__main__':
#    main()