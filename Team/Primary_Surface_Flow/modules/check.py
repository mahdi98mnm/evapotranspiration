"""
Internal Validation Functions.
"""

from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
from operator import lt, gt



def check_precipitation(
    precipitation : float
) -> NoReturn:
    
    """
    Description
    -----------
    Check if precipitation value is negative

    Parameters
    ----------
    precipitation : float
        Event rainfall depth - Starts from 0 - mm
    """
    
    if not isinstance(precipitation, (int, float)):
        raise TypeError(
            f'Precipitation value must be int or float: {precipitation}'
        )

    if lt(precipitation, 0):
        raise ValueError(
            f'Precipitation value must be greater than zero: {precipitation}'
        )


def check_curve_number(
    curve_number : float
) -> NoReturn:
    
    """
    Description
    -----------
    Check if curve number is valid

    Parameters
    ----------
    curve_number : float
        An index of the land condition as indicated by soils, cover, land use - Between 0 to 100 - dimensionless
    """
    
    if not isinstance(curve_number, (int, float)):
        raise TypeError(
            f'Curve number must be int or float: {curve_number}'
        )

    if lt(curve_number, 0) or gt(curve_number, 100):
        raise ValueError(
            f'Curve number must be between 0 to 100: {curve_number}'
        )


def check_rsa(
    rsa : bool
) -> NoReturn:
    
    """
    Description
    -----------
    Check if Runoff source area is valid

    Parameters
    ----------
    rsa : bool
        Runoff source area - 0 or 1 - dimensionless
    """

    if not isinstance(rsa, bool):
        raise TypeError(
            f'RSA must be boolean: {rsa}'
        )


def check_antecedent_precipitation(
    antecedent_precipitation : float
) -> NoReturn:
    
    """
    Description
    -----------
    Check if Antecedent precipitation is valid

    Parameters
    ----------
    antecedent_precipitation: float
        Antecedent precipitation is precipitation falling before, but influencing the runoff yields of, a given rainfall event - Starts from 0 - mm
    """
    
    if not isinstance(antecedent_precipitation, (int, float)):
        raise TypeError(
            f'Antecedent precipitation must be int or float: {antecedent_precipitation}'
        )

    if lt(antecedent_precipitation, 0):
        raise ValueError(
            f'Antecedent precipitation must be greater than zero: {antecedent_precipitation}'
        )


def check_is_growing_season(
    is_growing_season : bool
) -> NoReturn:
    
    """
    Description
    -----------
    Check if is_growing_season is valid

    Parameters
    ----------
    is_growing_season : bool
        Check if it's growing season or not - 0 or 1 - dimensionless
    """

    if not isinstance(is_growing_season, bool):
        raise TypeError(
            f'is_growing_season must be boolean: {is_growing_season}'
        )