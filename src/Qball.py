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

    def tildeEnergyDerivative(self, tildePosition, energy, tildeOmega):
        value = 4 * math.pi * (tildePosition**2) * (0.5 * (self.xDerivative**2) + 0.5 * (tildeOmega**2) * (self.x**2) + 1 - math.cos(self.x))
        return value
    
    def tildeChargeDerivative(self, tildePosition, charge, *args):
        return 4 * math.pi * (self.x**2) * (tildePosition**2)

