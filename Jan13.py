#!/usr/bin/python

# Ponder This Challenge:
# The following six permutations of the letters EISH
#     EISH
#     HESI
#     IEHS
#     HISE
#     SEHI
#     SIHE
# satisfy that for every three letters, and every order, there exists a permutation in which these three letters appear in this order. For example, SHE appears in the last line and HIS appears in the fourth line.
# Find 13 permutations of the letters ABCEFHIJLMNPQTVXYZ which satisfy the same condition: for every three letters and every one of their six possible orders, there exists at least one permutation in which the letters appear in this order.
# A bonus question: What is special about this set of letters?

import itertools

def isSubsequence(sub, str):
    start_index = 0
    for letter in sub:
        start_index = str.find(letter, start_index) + 1
        if start_index == 0: 
            return False
    return True
        

#letters = ['E', 'I', 'S', 'H']
#letters = ['A', 'B', 'C', 'E', 'F', 'H', 'I', 'J', 'L', 'M', 'N', 'P', 'Q', 'T', 'V', 'X', 'Y', 'Z']
letters = "ABCEFHIJLMNPQTVXYZ"
combos_of_three_letters = list(itertools.combinations(letters, 3))
permutes_of_three_letters = list(itertools.permutations(letters, 3))

permutes_of_answer = []
permutes_of_answer.append(letters)

answers = dict(zip(list(itertools.permutations(letters, 3)), [False]*len(list(itertools.permutations(letters, 3)))))


for p in list(itertools.permutations(letters, 3)):
    if isSubsequence(p, letters):
        print "%c%c%c" % (p[0], p[1], p[2])
    else:
        print "nope %c%c%c" % (p[0], p[1], p[2])


# 4896 different permutations must match
# 18 letters * 13 permutations = 234 ... probably useless
# (18 choose 3) * 13  = 10608, so there might be many solutions
