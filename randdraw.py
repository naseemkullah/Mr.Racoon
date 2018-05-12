import random

class RandDraw:
    def __init__(self, list): 
        """
        Constructs a random draw from list l.
        """
        self.l = list # saves the provided list into the object we are constructing
        self.m = len(self.l)-1 # create the mark, and set it to the end of the list
        # there is an invisible "return self" at the end of every contructor

    def draw(self):
        if self.done():
            raise IndexError
    
        i = random.randint(0,self.m) # Random.randint(random,0,self.m)

        temp = self.l[i]
        self.l[i] = self.l[self.m]
        self.l[self.m] = temp

        self.m -= 1
        return temp

    def reset(self):
        self.m = len(self.l)-1

    def done(self):
        return self.m == -1
        

