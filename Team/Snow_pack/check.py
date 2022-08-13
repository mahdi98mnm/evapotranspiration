"""
Internal Validation Functions.
copyright: (c) 2022 by Motahare Soltani.
"""

from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn

def check_maximum_temperature(
    tmax : float
) -> NoReturn:
    
    """
    Description
    -----------
    Check the daily maximum temperature is above the freezing point (0°c).
    Parameters
    ----------
    tmax : float
        Maximum Daily Temperature [Degrees Celsius]
    """
    
    if not tmax > 0:
        raise ValueError(
            f'The daily maximum temperature must be above the freezing point (0°c) : {tmax}'
        )