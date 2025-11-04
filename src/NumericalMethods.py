class NumericalMethods:
    def rungeKutta4SecondOrder(self, x, y, yDerivative, delta, secondOrderDifferentialY, *args, **kwargs):
        x0 = x
        y0 = y
        dy = yDerivative
   
        k1 = dy
        a1 = secondOrderDifferentialY(x0, y0, dy, *args, **kwargs)

        k2 = dy + a1 * (delta/2)
        a2 = secondOrderDifferentialY(x0 + delta/2, y0 + k1 * delta/2, dy + (delta/2) * a1, *args, **kwargs)

        k3 = dy + a2 * (delta/2)
        a3 = secondOrderDifferentialY(x0 + delta/2, y0 + k2 * delta/2, dy + (delta/2) * a2, *args, **kwargs)

        k4 = dy + a3 * delta
        a4 = secondOrderDifferentialY(x0 + delta, y0 + k3 * delta, dy + delta * a3, *args, **kwargs)

        y = y0 + (delta/6) * (k1 + 2*k2 + 2*k3 + k4)
        yDerivative = dy + (delta/6) * (a1 + 2*a2 + 2*a3 + a4)

        return y, yDerivative
    
    def rungeKutta4FirstOrder(self, x, y, delta, differentialY, *args, **kwargs):
        y0 = y
        x0 = x

        k1 = differentialY(x0, y0, *args, **kwargs)
        k2 = differentialY(x0 + (delta/2), y0 + k1 * (delta/2), *args, **kwargs)
        k3 = differentialY(x0 + (delta/2), y0 + k2 * (delta/2), *args, **kwargs)
        k4 = differentialY(x0 + delta, y0 + k3 * delta, *args, **kwargs)

        y += (delta/6)*(k1 + 2*k2 + 2*k3 + k4)

        return y
    