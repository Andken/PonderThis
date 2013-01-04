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
import sys

def done(answers):
    for k in answers.iterkeys():
        if not answers[k]: 
            return False
    return True

def getNextFalseAnswer(answers, key):
    passed_key = False
    if key == ('X', 'X', 'X'):
        passed_key = True

    for k in answers.iterkeys():
        if passed_key:
            if not answers[k]: 
                return k
        else:
            if k == key:
                passed_key = True
    return ('Z', 'Z', 'Z')

def rotateStringRight(s):
    return s[1:]+s[0]
    
def rotateStringLeft(s):
    length = len(s)
    return s[length-1] + s[0:length-1]

def swap(s, i1, i2):
    new = list(s)
    new[i1] = s[i2]
    new[i2] = s[i1]
    return ''.join(new)

def getNextWorking(next_answer, working):
#    print " gnw: ", next_answer, working
    # figure out which letter is off

    i0 = working.index(next_answer[0])
    i1 = working.index(next_answer[1])
    i2 = working.index(next_answer[2])

    # six permutations of 0 1 2
    # 0 1 2 --- already good!
    # 0 2 1 --- swap last two
    # 1 0 2 --- swap first two
    # 1 2 0 --- rotate right
    # 2 0 1 --- rotate left
    # 2 1 0 --- swap first and last
    

    if i0<i1 and i0<i2 and i1>i2:
        return swap(working, i1, i2)
    elif i0>i1 and i0<i2 and i1<i2:
        return swap(working, i0, i1)
    elif i0<i1 and i0>i2 and i1>i2:
        while not isSubsequence(next_answer, working):
            working = rotateStringRight(working)
        return working
    elif i0>i1 and i0>i2 and i1<i2:
        while not isSubsequence(next_answer, working):
            working = rotateStringLeft(working)
        return working
    elif i0>i1 and i0>i2 and i1>i2:
        return swap(working, i0, i2)

    # this one works, just return it
    return working


def isSubsequence(sub, str):
    start_index = 0
    for letter in sub:
        start_index = str.find(letter, start_index) + 1
        if start_index == 0: 
            return False
    return True
        
def checkWorkingAnswers(working_answers, working):
    for wa in working_answers:
#        print "  $$ checking ", wa, working
        if not isSubsequence(wa, working):
            return False
    return True

#letters = "EISH"
letters = "ABCEFHIJLMNPQTVXYZ"
combos_of_three_letters = list(itertools.combinations(letters, 3))
permutes_of_three_letters = list(itertools.permutations(letters, 3))

permutes_of_answer = []
permutes_of_answer.append(letters)

answers = dict(zip(list(itertools.permutations(letters, 3)), [False]*len(list(itertools.permutations(letters, 3)))))

working = letters
permutes = []

for p in list(itertools.permutations(letters, 3)):
    if isSubsequence(p, working):
        answers[p] = True

permutes.append(working)

#while not next_answer == "":
#    next_answer = getNextFalseAnswer(answers, next_answer)
#    print next_answer

#for k in answers.iterkeys():
#    if answers[k]:
#        print k


while not done(answers):
#    print "# permutes: ", len(permutes)
    working_answers = []
    next_answer = ('X', 'X', 'X')
    next_answer = getNextFalseAnswer(answers, next_answer)

    continuation = False
    while not next_answer == ('Z', 'Z', 'Z'):
#        print "next_answer: ", next_answer
        new_working = getNextWorking(next_answer, working)
#        print " getNextWorking returned: ", new_working
        if checkWorkingAnswers(working_answers, new_working):
#            print " appending"
            working_answers.append(next_answer)
            working = new_working
            continuation = True
    
        next_answer = getNextFalseAnswer(answers, next_answer)
        if next_answer == ('Z', 'Z', 'Z') and continuation:
            continuation = False
            next_answer = ('X', 'X', 'X')
    
    for p in list(itertools.permutations(letters, 3)):
        if isSubsequence(p, working):
            answers[p] = True

#    print "   Adding: ", working
    permutes.append(working)

# first check off the ones that exist in the first pass, then modify based on first one that doesn't match...repeat


answers2 = dict(zip(list(itertools.permutations(letters, 3)), [0]*len(list(itertools.permutations(letters, 3)))))


for p in permutes:
    for k in answers2.iterkeys():
        if isSubsequence(k, p):
            answers2[k] += 1



for p in permutes:
    print p
    ss = 0
    for k in answers2.iterkeys():
        if isSubsequence(k, p):
            if answers2[k] == 1:
                print " ", k, answers2[k]
            ss += 1
    print p, ss

            

# 4896 different permutations must match
# 18 letters * 13 permutations = 234 ... probably useless
# (18 choose 3) * 13  = 10608, so there might be many solutions
