#!/usr/bin/env python3

def return_evens(num_list):
    list=[num for num in num_list if num%2==0]
    return list
def make_exclamation(sentence_list):
    list=[sentence + "!" for sentence in sentence_list ]
    return list