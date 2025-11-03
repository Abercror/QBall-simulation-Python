class NumericalMethods:
    def rungeKuttaSecondOrder(self, x, y, yDerivative, delta, secondOrderDifferentialY, *args, **kwargs):
        x0 = x
        y0 = y
   
        k0 = yDerivative
        a0 = secondOrderDifferentialY(x0, y0, k0, *args, **kwargs)

        k1 = k0 + a0*(delta/2)
        a1 = secondOrderDifferentialY(x0 + delta/2, y0 + k0 * delta/2, k1, *args, **kwargs)

        k2 = k1 + a1*(delta/2)
        a2 = secondOrderDifferentialY(x0 + delta/2, y0 + k1 * delta/2, k2, *args, **kwargs)

        k3 = k2 + a2*delta
        a3 = secondOrderDifferentialY(x0 + delta, y0 + k2 * delta, k3, *args, **kwargs)

        y += (delta/6) * (k0 + 2*k1 + 2*k2 + k3)
        yDerivative += (delta/6) * (a0 + 2*a1 + 2*a2 + a3)

        return y, yDerivative
    
    def rungeKuttaFirstOrder(self, x, y, delta, differentialY, *args, **kwargs):
        y0 = y
        x0 = x

        k1 = differentialY(x0, y0, *args, **kwargs)
        k2 = differentialY(x0 + (delta/2), y0 + k1 * (delta/2), *args, **kwargs)
        k3 = differentialY(x0 + (delta/2), y0 + k2 * (delta/2), *args, **kwargs)
        k4 = differentialY(x0 + delta, y0 + k3 * delta, *args, **kwargs)

        y += (delta/6)*(k1 + 2*k2 + 2*k3 + k4)

        return y
    