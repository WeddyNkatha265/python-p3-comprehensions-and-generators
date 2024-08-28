#!/usr/bin/env python3

def return_evens(num_list):
    if not num_list:
        return []
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    if not sentence_list:
        return []
    return [f"{sentence}!" for sentence in sentence_list]