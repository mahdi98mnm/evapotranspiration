import math

def dms_to_dd(
    degree : int,
    minute : int,
    second : int
    ) -> float:
 
    """
    Description
    -----------
    Convert degree_minute_second to degree 
    ----------
    Latitude:
    degree : int
        degree in degree - Positive for the Northern Hemisphere and negative for the Southern Hemisphere
    minute : int
        minute in minute - Positive
    second : int
        second in second - Positive

   
    Returns
    -------
    dms_to_dd : float
        dms_to_dd in degree
    """
    if degree < 0 :
        dd = -(abs(degree) + float(minute) / 60 + float(second) / 3600)
    else:
        dd = degree + float(minute) / 60 + float(second) / 3600

    return dd

# Check_dms_to_dd ----- page50 EX10 FAO56
# print(dms_to_dd(-22 , 54 , 0))


def degree_to_Radian(
    degree : int,
    minute : int,
    second : int
) -> float:
    
    """
    Description
    -----------
    Convert degree to Radian 
    ----------
    Latitude:
    degree : int
        degree in degree - Positive for the Northern Hemisphere and negative for the Southern Hemisphere
    minute : int
        minute in minute - Positive
    second : int
        second in second - Positive

   
    Returns
    -------
    Latitude : float
        Latitude in Radian
    """
        
    return math.radians(dms_to_dd(degree, minute , second))

# Check_Convert degree to Radian ----- page50 EX10 FAO56
# print(degree_to_Radian(-22 , 54 , 0))


def temperature_celsius_To_kelvin(
    Temperature : float,
) -> float:
    
    """
    Description
    -----------
    Convert Temperature celsius To Kelvin 
    ----------
    Temperature : float
        Temperature in celsius
    
    Returns
    -------
    Temperature : float
        Temperature in Kelvin
    """
        
    return Temperature + 273.16