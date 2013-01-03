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

letters = set(['A', 'B', 'C', 'E', 'F', 'H', 'I', 'J', 'L', 'M', 'N', 'P', 'Q', 'T', 'V', 'X', 'Y', 'Z'])

combos_of_three_letters = []
for a in letters:
    new_letters = (list(set(letters) - set([a])))
    print new_letters



