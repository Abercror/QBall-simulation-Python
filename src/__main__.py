from pathlib import Path
from Qball import Qball
from Simulation import Simulation
from NumericalMethods import NumericalMethods
from graph import graphing
import numpy as np
import math

startingPosition = 0
endingPosition = 1000
delta = 0.1
steps = math.floor((endingPosition - startingPosition) / delta)

# functionA = 10e12
# Lambda = math.sqrt(0.135 * 0.13)

x0 = [i for i in np.linspace(0, 1, 100)]
tildeOmega = [i for i in np.linspace(0,1, 100)]
# tildeOmega = [1]

method = "RungeKutta"

def initialQballValues(startingPosition, i):
    x = np.float64(i)
    dx = np.float64(0)
    tildePosition = np.float64(startingPosition)
    tildeEnergy = np.float64(0)
    tildeCharge = np.float64(0)
    particle = Qball(x, dx, tildePosition, tildeEnergy, tildeCharge)
    return particle

def fileStructure(xvalue, index):
    qBallSimulation = Path(__file__).parent.parent
    resultsDirectory = Path(qBallSimulation, "Results")
    resultsDirectory.mkdir(parents=True, exist_ok=True)
    xFolder = Path(resultsDirectory, f"{index} Initial x = {xvalue}")
    xFolder.mkdir(parents=True, exist_ok=True)
    return xFolder

def main(method):

    for i in x0:
        x0index = x0.index(i)
        xFolder = fileStructure(i, x0index)
        for j in tildeOmega:
            omegaIndex = tildeOmega.index(j)
            particle = initialQballValues(startingPosition, i)
            graphName = f"{omegaIndex} Omega = {tildeOmega[omegaIndex]}.png"
            graphLocation = Path(xFolder, graphName)

            sim = Simulation(particle)
            sim.run(steps, delta, method, j)
            graphing(sim.history, graphLocation)
            sim.clearData()
            print(i)

if __name__ == "__main__":
    main(method)