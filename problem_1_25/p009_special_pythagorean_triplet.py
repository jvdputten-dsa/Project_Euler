# a^2 + b^2 = c^2
# a + b + c = 1000
# c = 1000 - a - b
# a^2 + b^2 = (-a -b + 1000)^2
# a^2 + b^2 = 1.000.000 + a^2 + b^2 - 2000a + 2ab - 2000b
# 2000a -2ab + 2000b = 1.000.000
# 1000a -ab + 1000b = 500.000
# a + b - ab/1000 = 500

import numpy as np

def equation(a, b):
    return a + b - ((a*b)/1000)

def get_a_b():
    for a in range(1, 500):
        for b in range(1, 500):
            if equation(a,b) == 500:
                return a,b

a,b = get_a_b()

c_squared = a**2 + b**2
c = np.sqrt(c_squared)
print(a, b, c, a*b*c)