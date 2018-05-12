#!/usr/bin/env python

import sys
import random
import json

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--run", help="Run the gift exchange.", action='store_true')
parser.add_argument("--register", help="Register as a member of the gift exchange.", action='store_true')
args = parser.parse_args()

def register():
    name = raw_input("What is your name? ")
    if not name:
        print "Cannot proceed without a name."
        
    else:

        partner = raw_input("Who is your partner? Leave blank if you are single. ") or None

        with open('family.json') as f:
            data = json.load(f) # load the family.json file

        member_dict = {name: partner}

        data.update(member_dict) # append the newly registered member to it

        with open('family.json', 'w') as f:
            json.dump(data, f) # dump the updated family.json file
        
        print "Registration complete."
        


def giftgiving():
    with open('family.json') as f:
        data = json.load(f)
    
    family = data.keys()

    choosers = family[:]
    choosees = family[:]

    random.shuffle(choosers)
    random.shuffle(choosees)
    
    for i,j in zip(choosers,choosees):
        if i == j: 
            print i + " picked their own name out of the hat. Let's restart!"
            giftgiving() # restart giftgiving process if chooser chooses themself as choosee
            break
        
        elif data[i] == j:
            print i + " picked their their partner's name (" + j + ") out of the hat. Let's restart!"
            giftgiving() # restart giftgiving process if chooser chooses themself as choosee
            break

        print i + " gives a gift to " + j



def main():
    if args.run == True:
        giftgiving()
    
    elif args.register == True:
        register()
        
    else:
        print "did you want to run (--run) the program or register (--register)?"


main()