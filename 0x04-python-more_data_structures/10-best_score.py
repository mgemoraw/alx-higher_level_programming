#!/usr/bin/python3
def best_score(a_dictionary):
     if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max_value = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == max_value:
            return key
