#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(x)

def fprime(x):
    return np.cos(x)

def dfdx(x, dx):
    return (f(x+dx) - f(x))/dx

dx = np.logspace(-16.0,-1.0,1000)

x0 = 1.0

eps = abs(dfdx(x0, dx) - fprime(x0))

plt.loglog(dx, eps)

plt.xlabel("$\Delta x$")
plt.ylabel("error in difference approximation")

plt.tight_layout()

plt.savefig("deriv_error.eps")


