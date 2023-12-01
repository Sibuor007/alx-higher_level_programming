#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        len_s = len(sentence)
    else:
        len_s = 0
    return (len_s, sentence if not sentence else sentence[:1])
