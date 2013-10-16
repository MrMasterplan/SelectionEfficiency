
class Person(object):
    """
    A person holds a list of favorites.
    """

        
    def __init__(self):
        super(Person, self).__init__()
        self.Reset()
        
    def Reset(self):
        self.favList = None
        self.favJobIDEnergyDict = None
        self.favJobIDPositionDict = None
    
    def _InitializefavJobIDEnergyDict(self):
        if self.favJobIDEnergyDict is not None:
            return #assume that it is correctly initialized.
        self.favJobIDEnergyDict = {}
        for jobID,energy in self.favList:
            self.favJobIDEnergyDict[jobID]=energy

    def _InitializefavJobIDPositionDict(self):
        if self.favJobIDPositionDict is not None:
            return #assume that it is correctly initialized.
        self.favJobIDPositionDict = {}
        for i,(jobID,energy) in enumerate(self.favList):
            self.favJobIDPositionDict[jobID]=i

    
    def GetEnergyOfJobID(self,jobID):
        self._InitializefavJobIDEnergyDict()
        return self.favJobIDEnergyDict[jobID]
    
    def GetPositionOfJobID(self,jobID):
        self._InitializefavJobIDPositionDict()
        return self.favJobIDPositionDict[jobID]
    

    