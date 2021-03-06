"""
Project Toxic Span Detection
Implementation of class extracting words from given spans
@authors: Julia Kłos, Patrycja Cieplicka
@date: 12.01.2020
"""
from nltk.tokenize import sent_tokenize

class WordsExtraction:
    """
    Class created for extracting words from given spans
    """
    def extractWordIndexUsingList(self,text, span_list):
        word_list = []
        for [fst, snd] in span_list:
            sentences = sent_tokenize(text[fst:snd+1])
            for sent in sentences:
                word_list.append(sent)
        return word_list

    def extractToxicWordIndexUsingSpans(self,row):
        if(row.toxicity):
            new_spans = []
            ## compare every 2 indeces
            for x, y in zip(row.spans, row.spans[1:]):
                ## first idx
                if(x == row.spans[0]):
                    new_spans.append([x])
                ## if last element
                if(y == row.spans[-1]):
                    new_spans[-1].append(y)
                 ## if jump occurs- the end of word
                elif( y - x > 1):
                    ## add ending to last span
                    new_spans[-1].append(x)
                    ## create new span
                    new_spans.append([y])
            return self.extractWordIndexUsingList(row.text, new_spans)
                
        else:
            return []
