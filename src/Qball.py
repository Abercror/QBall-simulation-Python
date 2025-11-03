from NumericalMethods import NumericalMethods
import numpy as np
import math

class Qball(NumericalMethods):
    def __init__(self, 
                 x, 
                 xDerivative, 
                 tildePosition, 
                 tildeEnergy, 
                 tildeCharge):
        self.x = x
        self.xDerivative = xDerivative
        self.tildePosition = tildePosition
        self.tildeEnergy = tildeEnergy
        self.tildeCharge = tildeCharge

    def xSecondDerivative(self, tildePosition, x, xDerivative, tildeOmega):
        if self.tildePosition != 0:
            value = math.sin(x) - (tildeOmega**2)*x - ((2/tildePosition))*(xDerivative)
        else:
            value = 0
        
        return value
    
    def updateSecondOrder(self, delta, method, tildeOmega):
        methods = {
            "RungeKutta": self.rungeKuttaSecondOrder
        }
        numericalMethod = methods[method]

        self.x, self.xDerivative = numericalMethod(self.tildePosition, self.x, self.xDerivative, delta, self.xSecondDerivative, tildeOmega)



    def tildeEnergyDerivative(self, tildePosition, energy, tildeOmega):
        value = 4 * math.pi * (tildePosition**2) * (0.5 * (self.xDerivative**2) + 0.5 * (tildeOmega**2) * (self.x**2) + 1 - math.cos(self.x))
        return value
    
    def tildeChargeDerivative(self, tildePosition, charge, *args):
        return 4 * math.pi * (self.x**2) * (tildePosition**2)


    def updateFirstOrder(self, delta, method, tildeOmega):
        methods = {
            "RungeKutta": self.rungeKuttaFirstOrder
        }
        numericalMethod = methods[method]

        self.tildeEnergy = numericalMethod(self.tildePosition, self.tildeEnergy, delta, self.tildeEnergyDerivative, tildeOmega)
        self.tildeCharge = numericalMethod(self.tildePosition, self.tildeCharge, delta, self.tildeChargeDerivative, tildeOmega)

