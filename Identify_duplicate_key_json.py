#!/usr/bin/python env
# Identify duplicate parameter in the input json file

import json
 
def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
           raise ValueError("duplicate key: %r" % (k,))
        else:
           d[k] = v
    return d
 
def main():
    with open("input.json") as f:
        d = json.load(f, object_pairs_hook=dict_raise_on_duplicates)
 
    print(d)