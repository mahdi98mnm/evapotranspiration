"""
Library of Functions for Estimating evaporation and sublimation from snow and ice surfaces.
copyright: (c) 2022 by Motahare Soltani.
"""
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn

def evaporation_sublimation_snow_ice_surface(
    u10 : float,
    esn : float,
    e2 : float
) -> float:
    """
    Description
    -----------
    Calculate evaporation from snow and ice surfaces.
    **Reference**: Based on Equation 55-6 in Instructions for methods of calculating the balance of water resources(1393).
    Parameters
    ----------
    u10 : float
        Average daily values of wind speed at a height of 10 meters above the snow surface [m / s]
    
    esn : float
        Saturated vapor pressure corresponding to the temperature of the snow surface [Kpa]

    e2 : float
        Steam pressure at a height of 2 meters above the snow surface [Kpa]

    Returns
    -------
    E : float
       Evaporation 
    """
    return ((0.18 + 0.98 * u10) * (esn - e2))