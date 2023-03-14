#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    fl = None
    if sentence != '':
        fl = sentence[0]
    return (ln, fl)
