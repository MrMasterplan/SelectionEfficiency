
import random
from Solution import Solution

def CreateLotterySolution(scenario):
    #establish the choosing order:
    queue = scenario[:]
    random.shuffle(queue)
    
    solution=Solution()
    
    for person in queue:
        his_choice = GetFavoriteChoice(person.favList,solution)
        solution[his_choice]=person
    return solution

def GetFavoriteChoice(favList,solution):
    for jobID,energy in favList:
        if jobID not in solution:
            break
    return jobID
