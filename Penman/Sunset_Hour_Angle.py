import math
import Convert
import Solar_Declination

def sunset_hour_angle(
    degree : int,
    minute : int,
    second : int,
    stddate:str
) -> float:
    
    """
    Description
    -----------
    calculate Sunset Hour Angle With Latitude and Solar Declination - eq 25 FAO56
    ----------
    Latitude:
    degree : int
        degree in degree - Positive for the Northern Hemisphere and negative for the Southern Hemisphere
    minute : int
        minute in minute - Positive
    second : int
        second in second - Positive
    stddate : str
        Date with the specified standard
   
    Returns
    -------
    Sunset Hour Angle : float
        Sunset Hour Angle in Radian
    """
        
    return math.acos(-math.tan(Convert.degree_to_Radian(
        degree = degree, minute = minute , second = second)) * math.tan(
            Solar_Declination.solar_declination(stddate)))

# Check_Calculate Sunset Hour Angle ----- page47 EX8 FAO56
# print(sunset_hour_angle(degree = -20, minute = 0 , second = 0 ,stddate = '2019-09-03'))
