# A Python Package to Calculate:
#     - Primary Interception
#     - Primary Flow
#     - Primary Infiltration
# from input Precipitation data.

from deprecated import deprecated
from modules.potential_retention import *
from modules.check_rsa import *
from modules.CN_modification import *
from typing import Tuple
from modules.check import *


@deprecated(version='0.1', reason="RSA is no longer calculated in newer method")
def calculate_runoff(
    precipitation: float,
    curve_number: float
) -> float:
    """
    Description
    -----------
    Calculate runoff using precipitation and curve number.
    **Reference**: National Resources Conservation Service, National Engineering Handbook, Section 4 "Hydrology" (1985)

    Parameters
    ----------
    precipitation : float
        Event rainfall depth - Starts from 0 - mm

    curve_number : float
        An index of the land condition as indicated by soils, cover, land use - Between 0 to 100 - dimensionless

    Returns
    -------
    - runoff : float
        Runoff depth resulted from precpitation - Starts from 0 - mm
    """

    if calculate_rsa(precipitation, curve_number):
        return (precipitation - 0.2*calculate_potential_retention(curve_number))**2 \
            / (precipitation + 0.8*calculate_potential_retention(curve_number))
    else:
        return 0


def calculate_runoff(
    precipitation: float,
    curve_number: float,
    rsa: bool,
    antecedent_precipitation: float = None,
    is_growing_season: bool = None
) -> Tuple[float, float]:
    """
    Description
    -----------
    Calculate Runoff using precipitation and curve number.
    **Reference**: National Resources Conservation Service, National Engineering Handbook, Section 4 "Hydrology" (1985)

    Parameters
    ----------
    precipitation : float
        Event Rainfall Depth - Starts from 0 - mm

    curve_number : float
        An index of the land condition as indicated by soils, cover, land use - Between 0 to 100 - dimensionless

    rsa : bool
        Runoff source area - 0 or 1 - dimensionless

    antecedent_precipitation: float
        Antecedent precipitation is precipitation falling before, but influencing the runoff yields of, a given rainfall event - Starts from 0 - mm

    is_growing_season: bool
        Check whether it's growing season or not - 0 or 1 - dimensionless

    Returns
    -------
    - runoff : float
        Runoff depth resulted from precpitation - Starts from 0 - mm

    - underground_runoff: float
        Runoff depth that enters the soil - Starts from 0 - mm
    """

    check_precipitation(precipitation)
    check_curve_number(curve_number)
    check_rsa(rsa)
    if antecedent_precipitation:
        check_antecedent_precipitation(antecedent_precipitation)
    if is_growing_season:
        check_is_growing_season(is_growing_season)


    if antecedent_precipitation:
        modified_cn = modify_CN(curve_number, antecedent_precipitation, is_growing_season)
    else:
        modified_cn = curve_number

    if rsa:
        runoff = (precipitation - 0.2*calculate_potential_retention(modified_cn))**2 \
            / (precipitation + 0.8*calculate_potential_retention(modified_cn))
    else:
        runoff = 0


    underground_runoff = 0
    if gt(runoff, 0):
        underground_runoff = precipitation - runoff
    
    if lt(underground_runoff, 0):
        underground_runoff = 0


    return runoff, underground_runoff