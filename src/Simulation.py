
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

    def clearData(self):
        self.history = {"Reduced Position": [],
                        "Reduced Phi": [],
                        "Reduced Energy": [], 
                        "Reduced Charge": []
                        }

    def run(self, steps, delta, method, tildeOmega):
        for _ in range(steps):
            self.record()
            self.particle.updateSecondOrder(delta, method, tildeOmega)
            self.particle.updateFirstOrder(delta, method, tildeOmega)
            self.particle.tildePosition += delta