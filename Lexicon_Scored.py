#!/usr/bin/python3
import json

class LexiconScore:

        def __init__(self,pos,neg,os):
                self.pos=pos
                self.neg=neg
                self.os=os

def get_lexicon(Sysnset):
        array = Sysnset[4].split(" ")
        all_words = [words.split('#')[0] for words in array]
        return all_words


def row_data(row):
        row_array = row.split("\t")
        return row_array

def type_cast(val):
        try:
                val = float(val)
                return val
        except ValueError:
                return float(0)


def make_object(line_array):
        positive=type_cast(line_array[2])
        negative=type_cast(line_array[3])
        obj_score=1-(positive+negative)
        obj = LexiconScore(positive,negative,obj_score)
        return obj


def get_scores(file):
        file = open(file)
        dictionary = {}
		for line in file:
                f = open('tweet_with_score.json','a')
                if not line.startswith('#'):
                        row_dat = row_data(line)
                        lexicons = get_lexicon(row_dat)
                        for lex_word in lexicons:
                                o=make_object(row_dat)
                                dictionary[lex_word]={'positive':o.pos, 'negative':o.neg, 'neutral':o.os}
        dict = json.dumps(dictionary)
        f.write(dict)
        f.close()


get_scores("sentiwords.txt")
