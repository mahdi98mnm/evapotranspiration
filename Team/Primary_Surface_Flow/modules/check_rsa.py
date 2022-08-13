from deprecated import deprecated
from modules.potential_retention import *


@deprecated(version='0.1', reason="RSA is now begin calculated using GIS")
def calculate_rsa(
    precipitation: float,
    curve_number: float
) -> bool:
    """
    Description
    -----------
    Calculate RSA coefficient
    **Reference**: National Resources Conservation Service, National Engineering Handbook, Section 4 "Hydrology" (1985)

    Parameters
    ----------
    precipitation : float
        Event Rainfall Depth - Starts from 0 - mm

    curve_number : float
        An index of the land condition as indicated by soils, cover, land use - Between 0 to 100 - dimensionless

    Returns
    -------
    - rsa : bool
        Runoff Surface Area - 0 or 1 - dimensionless
    """
    
    potential_retention = calculate_potential_retention(curve_number)
    if (precipitation > 0.2*potential_retention):
        return True
    else:
        return False