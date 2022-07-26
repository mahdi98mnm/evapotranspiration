import Solar_or_shortwave_radiation

def net_solar_or_shortwave_radiation(
    method_Solar_or_shortwave_radiation : str,
    stddate : str,
    degree,
    minute,
    second,
    Actual_duration_of_sunshine_in_a_day = None,
    Monthly_average_sunshine_duration = None,
    mode_data = None,
    T_max = None,
    T_min = None,
    Adjustment_coefficient_or_K_RS = None
) -> float:
    
    """
    Description
    -----------
    calculate Net solar or shortwave radiation with Solar or shortwave radiation - eq 38 FAO56
    ----------
    method_Solar_or_shortwave_radiation : str
        Angstrom or Hargreaves for Solar or shortwave radiation
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
    Actual duration of sunshine in a day : float
        Actual duration of sunshine in a day in hour per day
    T_max : float
        Maximum Temperature in celsius
    T_min : float
        Minimum Temperature in celsius
    Adjustment_coefficient_or_K_RS : float
        Adjustment coefficient in C**-0.5 -- between 0.16 to 0.19
            for interior locations, where land mass dominates and air masses are not strongly
            influenced by a large water body, kRs ≅ 0.16;
            for coastal locations, situated on or adjacent to the coast of a large land mass and where
            air masses are influenced by a nearby water body, kRs ≅ 0.19
    
   
    Returns
    -------
    Net solar or shortwave radiation : float
        Net solar or shortwave radiation in MJ / m**2 /day
    """
    if method_Solar_or_shortwave_radiation == 'Angstrom':
        R_ns = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Angstrom(
            stddate = stddate,
            degree = degree, 
            minute = minute,
            second = second,
            mode_data = mode_data,
            Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day,
            Monthly_average_sunshine_duration = Monthly_average_sunshine_duration) * 0.77

    elif method_Solar_or_shortwave_radiation == 'Hargreaves':
        R_ns = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Hargreaves(
            stddate = stddate,
            degree = degree,
            minute = minute,
            second = second,
            T_max = T_max,
            T_min = T_min,
            Adjustment_coefficient_or_K_RS = Adjustment_coefficient_or_K_RS
            ) * 0.77
        
    return R_ns

# Check_Net solar or shortwave radiation ----- page62 EX16 FAO56
# print(net_solar_or_shortwave_radiation(method_Solar_or_shortwave_radiation='Hargreaves' ,stddate='2019-04-15' , degree=13 , minute=44 , second=0 , T_max=34.8 , T_min=25.6 , Adjustment_coefficient_or_K_RS =0.19 ))
# Check_Net solar or shortwave radiation ----- page53 EX12 FAO56
# print(net_solar_or_shortwave_radiation(method_Solar_or_shortwave_radiation='Angstrom' , stddate='2019-05-15',degree=-22 , minute=54 , second= 0 , Actual_duration_of_sunshine_in_a_day = 220 , mode_data = 'monthly'))