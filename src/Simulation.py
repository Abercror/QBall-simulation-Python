
class Simulation:
    def __init__(self, particle):
        self.particle = particle
        self.history = {"Reduced Position": [],
                        "Reduced Phi": [],
                        "Reduced Energy": [], 
                        "Reduced Charge": []
                        }
        
    # def conversionToNormal(self, functionA, Lambda):
    #     position = (self.particle.tildePosition * functionA) / (Lambda**2)
    #     phi = self.particle.x * functionA
    #     energy = ((functionA**3)*self.particle.tildeEnergy) / (Lambda**2)
    #     charge = (functionA / Lambda)**4 * self.particle.tildeCharge
        
    #     return (position, phi, energy, charge)

    def record(self):
        # data = self.conversionToNormal(functionA, Lambda)
        self.history["Reduced Position"].append(self.particle.tildePosition)
        self.history["Reduced Phi"].append(self.particle.x)
        self.history["Reduced Energy"].append(self.particle.tildeEnergy)
        self.history["Reduced Charge"].append(self.particle.tildeCharge)

    def updateFirstOrder(self, delta, method, tildeOmega):
        methods = {
            "RungeKutta": self.particle.rungeKutta4FirstOrder
        }
        numericalMethod = methods[method]

        self.particle.tildeEnergy = numericalMethod(self.particle.tildePosition, self.particle.tildeEnergy, delta, self.particle.tildeEnergyDerivative, tildeOmega)
        self.particle.tildeCharge = numericalMethod(self.particle.tildePosition, self.particle.tildeCharge, delta, self.particle.tildeChargeDerivative, tildeOmega)

    def updateSecondOrder(self, delta, method, tildeOmega):
        methods = {
            "RungeKutta": self.particle.rungeKutta4SecondOrder
        }
        numericalMethod = methods[method]

        self.particle.x, self.particle.xDerivative = numericalMethod(self.particle.tildePosition, self.particle.x, self.particle.xDerivative, delta, self.particle.xSecondDerivative, tildeOmega)


    def update(self, delta, method, tildeOmega):
        self.updateSecondOrder(delta, method, tildeOmega)
        self.updateFirstOrder(delta, method, tildeOmega)
        
    def clearData(self):
        self.history = {"Reduced Position": [],
                        "Reduced Phi": [],
                        "Reduced Energy": [], 
                        "Reduced Charge": []
                        }

    def run(self, steps, delta, method, tildeOmega):
        self.updateFirstOrder(delta, method, tildeOmega)
        for _ in range(steps):
            self.record()
            self.update(delta, method, tildeOmega)
            self.particle.tildePosition += delta