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

    with open('family.json') as f:
        data = json.load(f) # load the family.json file

    try:
        if data[partner] != name:
            print "You might want to talk to your partner."
            return
    
    except KeyError:
        pass

    for n,p in data.iteritems():
        if p == name and n != partner: #n if you are
            print "Sure bout that?!"
            return

    data[name] = partner

    with open('family.json', 'w') as f:
        json.dump(data, f) # dump the updated family.json file
    
    print "Registration complete."

def giftgiving():
    with open('family.json') as f:
        data = json.load(f)
    
    family = data.keys()

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
            print i + " picked their their partner's name (" + j + ") out of the hat. Let's restart!"
            choosers.reset()
            choosees.reset()
            continue

        print i + " gives a gift to " + j

def main():
    if args.run:
        giftgiving()
    elif args.register:
        register() 
    else:
        print "did you want to run (--run) the program or register (--register)?"


if __name__ == "__main__":
    main()