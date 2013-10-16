
import ROOT
from Config import Config
from  ScenarioCreation import GenerateCompleteNewScenario
from LotteryMethod import CreateLotterySolution

# from Plotting import CleanHistDistOfFavourites,PlotDistOfFavourites,CleanHistDistOfSolutionEnergies,PlotDistOfSolutionEnergies

hdist = ROOT.TH1D("DistOfFavourites", "Disttribution of Favourite Positions",Config.NumberOfJobs,-0.5,Config.NumberOfJobs-0.5)

henergy = ROOT.TH1D("DistOfSolutionEnergies", "Disttribution of Solution Energies",100,0000,12000)

scenario = GenerateCompleteNewScenario()

for i in range(100):
    solution = CreateLotterySolution(scenario)

    for jobID,person in solution.iteritems():
        hdist.Fill(person.GetPositionOfJobID(jobID))
    henergy.Fill(solution.GetEnergy())
    print solution.GetEnergy()
    
henergy.Draw()

