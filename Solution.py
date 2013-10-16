
class Solution(dict):
    """A Solution couples a job to a person"""
    def __init__(self):
        super(Solution, self).__init__()
    
    def GetEnergy(self):
        totenergy = 0.
        for jobID,person in self.iteritems():
            totenergy +=person.GetEnergyOfJobID(jobID)
        return totenergy
        
        