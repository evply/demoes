#!/usr/bin/env python
# -*- coding: utf-8 -*-

def _insert_item_in_all(item, seq):
    result = []
    length = len(seq)

    for i in range(length + 1):
        result.append(seq[:i] + [item] + seq[i:])
    return result

def perm(seq):

    if len(seq) == 2:
        return insert_item_in_all(seq[-1], seq[0:-1])
     return reduce(lambda x,y:x + y, map(lambda s: insert_item_in_all(seq[-1], s), perm(seq[0:-1])))
