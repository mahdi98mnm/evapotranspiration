


def available_evaporable_water(
    e_a : float,
    Is_in_fisrt_step : bool,
    infiltration : float,
    initial_Available_Evaporable_Water : float = None,
    Available_Evaporable_Water_in_previous_step : float = None
) -> float:

    """
    Description
    -----------
    calculate Available_water With FC and PWP 
    ----------
    e_a : float
        Evapotranspiration_noncovered_areas in mm
    Is_in_fisrt_step : bool
        Is_in_fisrt_step in boolean - True if we are on the first day, False if we are not on the first day
    infiltration : float
        infiltration in mm
    initial_Available_Evaporable_Water : float
        initial_Available_Evaporable_Water in mm - If we are on the first day, we must enter a hypothetical value
    Available_Evaporable_Water_in_previous_step : float
        Available_Evaporable_Water_in_previous_step in mm
    

    Returns
    -------
    available_evaporable_water : float
        available_evaporable_water in mm
    
    """
    if Is_in_fisrt_step is True:
        AE = initial_Available_Evaporable_Water
    else:
        AE = Available_Evaporable_Water_in_previous_step
    
    

    return (0.5 * infiltration) + AE - e_a


# print(available_evaporable_water(
#     infiltration = 150,
#     Permanent_wilting_point_wet = 20,
#     Field_capacity_wet = 60,
#     soil_depth = 250,
#     Is_in_fisrt_step = False,
#     Crop_Cover = 0.5,
#     Reference_Crop_Evapotranspiration = 3,
#     Available_Evaporable_Water_in_previous_step = 125
# ))