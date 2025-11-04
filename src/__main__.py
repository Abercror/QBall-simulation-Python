from pathlib import Path
from Qball import Qball
from Simulation import Simulation
from NumericalMethods import NumericalMethods
from graph import graphing
import numpy as np
import math

startingPosition = 0
endingPosition = 100
delta = 0.01
steps = math.floor((endingPosition - startingPosition) / delta)

# functionA = 10e12
# Lambda = math.sqrt(0.135 * 0.13)

tildeOmega = [i for i in np.linspace(-2, 2, 100)]
# omega = [1]
# tildeOmega = [(functionA*i)/(Lambda**2) for i in omega]

method = "RungeKutta"

def initialQballValues(startingPosition):
    x = np.float64(6.0)
    dx = np.float64(0)
    tildePosition = np.float64(startingPosition)
    tildeEnergy = np.float64(0)
    tildeCharge = np.float64(0)
    particle = Qball(x, dx, tildePosition, tildeEnergy, tildeCharge)
    return particle

def fileStructure():
    qBallSimulation = Path(__file__).parent.parent
    resultsDirectory = Path(qBallSimulation, "Results")
    resultsDirectory.mkdir(parents=True, exist_ok=True)
    return resultsDirectory

def main(method):
    resultsDirectory = fileStructure()

    for i in tildeOmega:
        index = tildeOmega.index(i)
        particle = initialQballValues(startingPosition)
        graphName = f"{index} Omega = {tildeOmega[index]}.png"
        graphLocation = Path(resultsDirectory, graphName)

        sim = Simulation(particle)
        sim.run(steps, delta, method, i)
        graphing(sim.history, graphLocation)
        sim.clearData()
        print(i)

if __name__ == "__main__":
    main(method)