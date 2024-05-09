import random

class MobEncounters():
    def __init__(self,biomename,loot,chances):
        self.name = biomename
        self.loot = loot
        self.chances = chances

easymoblist = []
easymobchances = []
mediummoblist = []
mediummobchances = []
hardmoblist = []
hardmobchances = []
extrememoblist = []
extrememobchances = []

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