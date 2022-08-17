"""
Library of Functions for Estimating snowfall
copyright: (c) 2022 by Motahare Soltani.
"""

from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn



def snow_fall(
    tmax : float,
    tmin : float,
    tmean : float
):

    """
    Description
    -----------
    Check snowfall.
    **Reference**: Based on Equation 1-2 in SWB Version 2.0 (2018).
    Parameters
    ----------
    tmax : float
        Maximum Daily Temperature [Degrees Celsius]

    tmin : float
        Minimum Daily Temperature [Degrees Celsius]

    tmean : float
        Mean Daily Temperature [Degrees Celsius]
        
    Returns
    -------
    p : A sentence about the precipitation is snow or rain & boolean parameter.
    """

    if (tmean - 1/3 * (tmax - tmin)) <= 0:
        print('Snow')
        return True
    else:
        print('Rain')
        return False
     


