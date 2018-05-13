#!/usr/bin/env python

import sys
import random
import json
from randdraw import RandDraw # choosers = RandDraw([1,2,3])


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--run", help="Run the gift exchange.", action='store_true')
parser.add_argument("--register", help="Register as a member of the gift exchange.", action='store_true')
args = parser.parse_args()

def register():
    name = raw_input("What is your name? ")
    if not name:
        print "Cannot proceed without a name."
        return
    
    partner = raw_input("Who is your partner? Leave blank if you are single. ") or None
    
    # Create an empty family.json if it does not exist
    try:
        with open('family.json') as f:
            data = json.load(f) # load the family.json file
    except IOError:
        data = {}

    # cannot choose a choosee who has chosen someone else
    try:
        if data[partner] != name:
            print partner + " seems to think that " + data[partner] + " is their partner, and not you."
            return
    except KeyError:
        pass

    # cannot choose a choosee or say that you are single if you are chosen by someone else
    for n,p in data.iteritems():
        if p == name and n != partner: #n if you are
            print "Sure bout that?! " + n + " seems to think that you are their partner."
            return

    data[name] = partner

    with open('family.json', 'w') as f:
        json.dump(data, f) # dump the updated family.json file
    
    print "Registration complete."

def giftgiving(familyfile):
    try:
        with open(familyfile) as f:
            data = json.load(f)
    except IOError:
        print "Nobody has registered for the gift exchange"
        return
    
    family = data.keys()

    if len(data) == 1:
        print "A gift exchange cannot comprise of just one person."
        return

    elif len(data) == 2 and family[0] == data[family[1]]:
        print "A gift exchange cannot comprise of just two partners."
        return

    elif len(data) == 3 and (data[family[0]] is not None or data[family[1]] is not None):
        print "A gift exchange cannot comprise of a trio of which 2 people are partners."
        return

    choosers = RandDraw(family[:]) 
    choosees = RandDraw(family[:])
    
    while not choosers.done():
        i = choosers.draw()
        j = choosees.draw()

        if i == j: 
            print i + " picked their own name out of the hat. Let's restart!"
            choosers.reset()
            choosees.reset()
            continue   
        elif data[i] == j:
            print i + " picked their partner's name (" + j + ") out of the hat. Let's restart!"
            choosers.reset()
            choosees.reset()
            continue

        print i + " gives a gift to " + j

def main():
    if args.run:
        giftgiving('family.json')
    elif args.register:
        register() 
    else:
        print "did you want to run (--run) the program or register (--register)?"


if __name__ == "__main__":
    main()