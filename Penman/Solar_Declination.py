import math
import Standard_Date_To_Julian_Day

def solar_declination(
    stddate: str
) -> float:
    
    """
    Description
    -----------
    calculate Solar Declination With Julian Date - eq 24 FAO56
    ----------
    stddate : str
        Date with the specified standard
   
    Returns
    -------
    Solar Declination : float
        Solar Declination in Radian
    """
        
    return 0.409 * math.sin(((2 * math.pi * Standard_Date_To_Julian_Day.standard_date_to_Julian_day(stddate)) / 365) - 1.39)

# Check_Calculate Solar Declination ----- page47 EX8 FAO56
# print(solar_declination('2019-09-03'))
