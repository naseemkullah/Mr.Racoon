import random

class RandDraw:
    def __init__(self, list): 
        """
        Constructs a random draw from a list. A mark is initially placed at the end of the list
        and random elements are drawn and swapped with the element at the mark which decrements
        by one after every draw. 
        """
        self.l = list
        self.m = len(self.l)-1 

    def draw(self):
        if self.done():
            raise IndexError
    
        i = random.randint(0,self.m)

        # swap the randomly chosen element with the element at mark
        temp = self.l[i]
        self.l[i] = self.l[self.m]
        self.l[self.m] = temp

        # decrement the mark and return the randomly chosen element
        self.m -= 1
        return temp

    def reset(self):
        self.m = len(self.l)-1

    def done(self):
        return self.m == -1
        

