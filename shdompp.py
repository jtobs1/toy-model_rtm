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
https://www.comsol.com/blogs/heat-transfer-in-participating-media-and-the-discrete-ordinates-method 
But I will be implimenting it from the ground up, 
excluding certain characteristics to just get the understanding.
Implimented on 09/15/2025.
Monochromatic; solving for intensity; using scattering, absorption, emissions, and phase function.

Basic process:
    1) Transform Source Function to Discrete Ordinate.
        - Use Legendre Polynomials for this (a_l,m).
    2) Integrate Source Function in RTE to get Intensity (need a_l,m).
        - Integrate "backwards."
        - Source Function and Extinction are bilinearly interpolated between grid points. 
    3) Transform Intensity back to Spherical Harmonics.
        - Use Legendre Polynomials (again) with corresponding weights, w_j,k.
    4) Convert Intensity in SH to Source Function.
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