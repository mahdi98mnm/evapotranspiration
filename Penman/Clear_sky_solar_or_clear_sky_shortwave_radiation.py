import Extraterrestrial_Radiation
import Solar_or_shortwave_radiation 

def clear_sky_solar_or_clear_sky_shortwave_radiation(
    degree : int,
    minute : int,
    second : int,
    stddate:str,
    Altitude = None
) -> float:
    
    """
    Description
    -----------
    calculate Clear-sky solar or clear-sky shortwave radiation with Extraterrestrial radiation and Altitude - eq 37 FAO56
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
    Altitude : float
        Altitude in meter - station elevation above sea level 
   
    Returns
    -------
    Clear-sky solar or clear-sky shortwave radiation : float
        Clear-sky solar or clear-sky shortwave radiation in MJ / m**2 /day
    """
    if Altitude == None :
        R_SO = 0.75 * Extraterrestrial_Radiation.extraterrestrial_radiation(degree , minute , second , stddate)

    else:
        R_SO = (0.75 + (2 * (10**-5) * Altitude)) * Extraterrestrial_Radiation.extraterrestrial_radiation(
            degree , minute , second , stddate)

    return R_SO

# Check_Clear-sky solar or clear-sky shortwave radiation ----- page62 EX16 FAO56
# R_SO=clear_sky_solar_or_clear_sky_shortwave_radiation(degree=13 , minute=44 , second=0 ,stddate='2019-04-15', Altitude=2)
# R_S=Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Hargreaves(stddate='2019-04-15' , degree=13 , minute=44 , second=0 , T_max=34.8 , T_min=25.6 , Adjustment_coefficient_or_K_RS =0.19)
# print(R_S/R_SO)
