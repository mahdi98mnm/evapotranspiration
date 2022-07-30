
import Available_Water

def ratio_of_actual_evaporable_water_to_total_evaporable_water(
    Is_in_fisrt_step : bool,
    Permanent_wilting_point_wet : float,
    Field_capacity_wet : float,
    soil_depth : float,
    Crop_Cover : float,
    Reference_Crop_Evapotranspiration : float,
    e_a : float,
    infiltration : float = None,
    Available_Evaporable_Water_in_previous_step : float = None,
    initial_Available_Evaporable_Water : float = None
) -> float:
    
    """
    Description
    -----------
    calculate ratio of actual evaporable water to total evaporable water - eq 5 in E:\Term2\payan_name\Modules\Evapotranspiration\Real.docx
    ----------
    Is_in_fisrt_step : bool
        Is_in_fisrt_step in boolean - True if we are on the first day, False if we are not on the first day
    Permanent_wilting_point_wet : float
        Permanent_wilting_point_wet in percent(volumetric)
    Field_capacity_wet : float
        Field_capacity_wet in percent(volumetric)
    soil_depth : float
        soil_depth in mm
    Crop_Cover : float
        Crop_Cover in No units
    Reference_Crop_Evapotranspiration : float
        Reference_Crop_Evapotranspiration in mm
    e_a : float
        Evapotranspiration_noncovered_areas in mm
    infiltration : float
        infiltration in mm
    Available_Evaporable_Water_in_previous_step : float
        Available_Evaporable_Water_in_previous_step in mm
    initial_Available_Evaporable_Water : float
        initial_Available_Evaporable_Water in mm - If we are on the first day, we must enter a hypothetical value
   
    Returns
    -------
    ratio_of_actual_evaporable_water_to_total_evaporable_water : float
        ratio_of_actual_evaporable_water_to_total_evaporable_water in No units
    """
    if Is_in_fisrt_step is True : 
        AE = initial_Available_Evaporable_Water
    else:
        AE = available_evaporable_water(
            e_a = e_a,
            Is_in_fisrt_step = Is_in_fisrt_step,
            infiltration = infiltration,
            Available_Evaporable_Water_in_previous_step = Available_Evaporable_Water_in_previous_step
        )
        
    
    AW = Available_Water.available_Water(
        Permanent_wilting_point_wet = Permanent_wilting_point_wet,
        Field_capacity_wet = Field_capacity_wet,
        soil_depth = soil_depth
    )

    return AE / AW





# print(ratio_of_actual_evaporable_water_to_total_evaporable_water(
#     Is_in_fisrt_step = True,
#     Permanent_wilting_point_wet = 20,
#     Field_capacity_wet = 60,
#     soil_depth = 250,
#     Crop_Cover = 0.4,
#     Reference_Crop_Evapotranspiration = 2,
#     initial_Available_Evaporable_Water = 145))