import math
import Constant
import Inverse_Relative_Distance_Earth_Sun
import Sunset_Hour_Angle
import Convert
import Solar_Declination

def extraterrestrial_radiation(
    degree : int,
    minute : int,
    second : int,
    stddate:str
) -> float:
    
    """
    Description
    -----------
    calculate Extraterrestrial Radiation - eq 28 FAO56
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
    Extraterrestrial Radiation : float
        Extraterrestrial Radiation in MJ/m**2/day
    """
    temp_1 = ((24 * 60 )/ math.pi) * Constant.SOLAR_CONSTANT * Inverse_Relative_Distance_Earth_Sun.inverse_relative_distance_earth_sun(
        stddate)

    temp_2 = Sunset_Hour_Angle.sunset_hour_angle(degree, minute, second, stddate) * math.sin(
        Convert.degree_to_Radian(degree, minute , second)) * math.sin(Solar_Declination.solar_declination(stddate))

    temp_3 = math.cos(Convert.degree_to_Radian(degree, minute , second))* math.cos(
        Solar_Declination.solar_declination(stddate)) * math.sin(Sunset_Hour_Angle.sunset_hour_angle(degree, minute , second,stddate))

    return temp_1 * (temp_2 + temp_3)

# Check_Calculate Extraterrestrial Radiation ----- page47 EX8 FAO56
# print(extraterrestrial_radiation(degree = -20 , minute = 0 , second = 0 , stddate = '2019-09-03'))
