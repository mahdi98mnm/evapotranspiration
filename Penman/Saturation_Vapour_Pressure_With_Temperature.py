from cmath import exp
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import math


def saturation_vapour_pressure_with_temperature(
    Temperature : float
) -> float:
    
    """
    Description
    -----------
    calculate Saturation Vapour Pressure With Temperature - eq 11 FAO56
    ----------
    Temperature : float
        Temperature in celsius
   
    Returns
    -------
    Saturation Vapour Pressure : float
        Saturation Vapour Pressure in Kilo pascal
    """
    
    return 0.6108 * math.exp((17.27 * Temperature) / (Temperature + 237.3))


# Check_saturation_vapour_pressure_with_temperature ----- page36 EX3 FAO56
# print(saturation_vapour_pressure_with_temperature(24.5))


def total_saturation_vapour_pressure(
    T_max : float,
    T_min : float
) -> float:
    
    """
    Description
    -----------
    calculate Total Saturation Vapour Pressure With max and min Temperature - eq 12 FAO56
    ----------
    T_max : float
        Maximum Temperature in celsius
    T_min : float
        Minimum Temperature in celsius

    Returns
    -------
    Total Saturation Vapour Pressure : float
        Total Saturation Vapour Pressure in Kilo pascal
    """
    

    return (saturation_vapour_pressure_with_temperature(T_max) + 
    saturation_vapour_pressure_with_temperature(T_min)) / 2
    
# Check_calculate Total Saturation Vapour Pressure With max and min Pressuree ----- page36 EX3 FAO56
# print(total_saturation_vapour_pressure(24.5,15))
