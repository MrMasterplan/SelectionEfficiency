"""
This file constains the code that is responsible for setting up a scenario.

The generation fo favourites so far offers the following methods:
    Type 1:
        all jobs have equal chance of being the top choice.
        the favLists are random shuffles.
    Type 2:
        there is a gradiont of favourites, equal for all.
        favLists are created based on this gradient of probablities
    Type 3: (to be implemented)
        a location (on a 2D square) is assigned to every job and to every person.
        every person orders all jobs based on distance from him. 
        

"""

from Person import Person
from Config import Config
from FavoriteList import FavoriteList
import random
import math

def GenerateCompleteNewScenario():
    population = MakeNewPopulation()
    scenario = GenerateFavourites(population)
    return scenario

def MakeNewPopulation():
    population = [] # list of people
    for i in range(Config.NumberOfPersons):
        population.append(Person())
    return population

def GenerateFavourites(population):
    #Method 3
    # return GenerateFavouritesFromLocation(population)
    
    for person in population:
        #generate a favList for each person
        
        #Method 1
        #simply take a random shuffle of all possible jobs.
        jobs = range(Config.NumberOfJobs)
        random.shuffle(jobs)
        
        #Method 2
        #Create a distribution of skewed weights and select randoms according to that
        # until all jobs are taken
        # distro = StepFunctionDistribution(Config.NumberOfJobs//2,1.0,0.2)
        # distro = LinearDeclineDistribution()
        # jobs = GenerateShuffleListFromDistro(distro)
                
        favList = FavoriteList()
        favList+=[ (jobID,i) for i,jobID in enumerate(jobs)]
        person.favList = favList
    return population

def GenerateFavouritesFromLocation(population):
    
    def getPosition():
        return (random.uniform(0,1.),random.uniform(0,1.))
    
    jobpositions = [ (getPosition(),jobID) for jobID in range(Config.NumberOfJobs)]
    for person in population:
        perspos = getPosition()
        jobdists = [((perspos[0]-jobpos[0])**2+(perspos[0]-jobpos[0])**2,jobid) for jobpos,jobid in jobpositions]
        jobdists.sort()
        
        favList = FavoriteList()
        favList+=[ (jobID,i) for i,(x,jobID) in enumerate(jobdists)]
        person.favList = favList
    return population
        
    

def StepFunctionDistribution(stepIndex,val_below,val_above):
    distro = [(val_below,i) for i in range(Config.NumberOfJobs)]
    for i in range(int(stepIndex),Config.NumberOfJobs):
        distro[i] = (val_above,i)
    return distro

def LinearDeclineDistribution():
    distro = [(1.0 - float(i)/Config.NumberOfJobs,i) for i in range(Config.NumberOfJobs)]
    return distro

def GenerateShuffleListFromDistro(distro):
    shufflist = []
    length = sum([val for val,i in distro])
    while distro:
        location = random.uniform(0,length)
        for i,(val,index) in enumerate(distro):
            if val > location:
                break
            else:
                location -= val
        length -=val
        shufflist.append(index)
        del distro[i]
    return shufflist
        
    
    

