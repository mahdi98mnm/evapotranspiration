import math
import Standard_Date_To_Julian_Day

def inverse_relative_distance_earth_sun(
    stddate: str
) -> float:
    
    """
    Description
    -----------
    calculate Inverse Relative Distance Earth Sun With Julian Date - eq 23 FAO56
    ----------
    stddate : str
        Date with the specified standard
   
    Returns
    -------
    Inverse Relative Distance Earth Sun : float
        Inverse Relative Distance Earth Sun in Radian
    """
        
    return 1 + (0.033 * math.cos((2 * math.pi * Standard_Date_To_Julian_Day.standard_date_to_Julian_day(stddate))/365))

# Check_Calculate Inverse Relative Distance Earth Sun ----- page47 EX8 FAO56
# print(inverse_relative_distance_earth_sun('2019-09-03'))
