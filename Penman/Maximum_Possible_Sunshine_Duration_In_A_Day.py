import math
import Sunset_Hour_Angle

def maximum_possible_sunshine_duration_in_a_day(
    degree : int,
    minute : int,
    second : int,
    stddate:str
) -> float:
    
    """
    Description
    -----------
    calculate maximum possible sunshine duration in a day - eq 34 FAO56
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
    maximum possible sunshine duration in a day : float
        maximum possible sunshine duration in a day in hours
    """
        
    return (24 / math.pi) * Sunset_Hour_Angle.sunset_hour_angle(degree = degree, minute = minute , second = second , stddate = stddate)

# Check_Calculate maximum possible sunshine duration in a day ----- page49 EX9 FAO56
# print(maximum_possible_sunshine_duration_in_a_day(degree = -20 , minute = 0 , second = 0 , stddate = '2019-09-03'))
