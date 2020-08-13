from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn
import random


def tag(sentence):
    words = word_tokenize(sentence)
    words = pos_tag(words)
    return words


def paraphraseable(tag):
    return tag.startswith('NN') or tag == 'VB' or tag.startswith('JJ')


def pos(tag):
    if tag.startswith('NN'):
        return wn.NOUN
    elif tag.startswith('V'):
        return wn.VERB


def synonyms(word, tag):
    lemma_lists = [ss.lemmas() for ss in wn.synsets(word, pos(tag))]
    lemmas = [lemma.name() for lemma in sum(lemma_lists, [])]
    return set(lemmas)


def synonymIfExists(sentence):
    for (word, t) in tag(sentence):
        if paraphraseable(t):
            syns = synonyms(word, t)
            if syns:
                if len(syns) > 1:
                    yield [word, list(syns)]
                    continue
        yield [word, []]


def paraphrase(sentence):
    ret = ""
    for x in synonymIfExists(sentence):
        if len(x[1]) == 0:
            ret = f"{ret} {x[0]}"
        else:
            ret = f"{ret} {random.choice(x[1])}"
    ret = ret.strip()
    ret = ret.replace('_', " ")
    return ret
