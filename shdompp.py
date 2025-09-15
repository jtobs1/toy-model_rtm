import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from scipy import integrate
from warnings import warn
from math import pi
from numpy.polynomial.legendre import Legendre

"""
This method follows PythonicDISORT: 
https://github.com/LDEO-CREW/Pythonic-DISORT/blob/main/docs/Pythonic-DISORT.ipynb
But I will be implimenting it from the ground up, 
excluding certain characteristics to just get the understanding.
Implimented on 09/15/2025.
Monochromatic; solving for intensity; using scattering, absorption, emissions, and phase function.

Basic process:
    1) represent intensity as a spherical harmonic expansion.
    2) get the spherical harmonic coefficients.
    3) convert from spherical harmonics back to angular intensity.
    4) assuming spherically symmetric phase functions,

"""

'''Each "voxel" will contain its own single-scatter albedo, absorption, emissions, and phase function.
For starters, this will just be the same throughout.'''
# Configure the layers:
vgrid_points = 16 # vertical grid points
hgrid_points = vgrid_points # horizontal grid points
tau_arr = np.arange(vgrid_points) / 2 +  0.5
n_layers = len(tau_arr)

# Configure columns:
dx = np.arange(hgrid_points)
dy = np.arange(hgrid_points)

# Configure Quadrature Sets {directions, weights}
n_quad = 16
n_legendre = n_quad # n_legendre <= n_quad
n_fourier = n_quad # n_fourier <= n_quad

# Define Boundary Conditions

# Define Source Terms

# 