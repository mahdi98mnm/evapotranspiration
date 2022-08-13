"""
Library of Functions for Estimating snowmelt
copyright: (c) 2022 by Motahare Soltani.
"""

from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
from check import check_maximum_temperature

# Degree-Day Method

#Degree Day factor = 1.5 (mm/day.°c)
DEGREE_DAY_FACTOR = 1.5


def snow_melt(
    tmax : float,
) -> float:

    """
    Description
    -----------
    Calculate snow melting rate.
    **Reference**: Based on Equation 1-3 in SWB Version 2.0 (2018).
    Parameters
    ----------
    tmax : float
        Maximum Daily Temperature [Degrees Celsius]

    Returns
    -------
    M : float
       Snow melting rate [mm / day]
    """
    check_maximum_temperature(tmax)

    return DEGREE_DAY_FACTOR * (tmax)





