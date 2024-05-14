import random

easymoblist = ["a"]
easymobchances = [1]
mediummoblist = ["a"]
mediummobchances = [1]
hardmoblist = ["a"]
hardmobchances = [1]
extrememoblist = ["a"]
extrememobchances = [1]

class Encounters():
    def __init__(self,difficulty,list,chances):
        self.difficulty = difficulty
        self.list = list
        self.chances = chances

def easymobencounter():
    mobencountered = random.choice(easymoblist,easymobchances,k=1)
    print ("")
    print ("You've encountered a ", mobencountered, "!")
def mediummobencounter():
    mobencountered = random.choice(mediummoblist,mediummobchances,k=1)
    print ("")
    print ("You've encountered a ", mobencountered, "!")
def hardmobencounter():
    mobencountered = random.choice(hardmoblist,hardmobchances,k=1)
    print ("")
    print ("You've encountered a ", mobencountered, "!")
def extrememobencounter():
    mobencountered = random.choice(extrememoblist,extrememobchances,k=1)
    print ("")
    print ("You've encountered a ", mobencountered, "!")