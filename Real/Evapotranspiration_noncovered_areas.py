from cmath import exp
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import math
import Available_Water
import Ratio_ac_evW_to_total


def e_noncovered(
    Is_in_fisrt_step : bool,
    Permanent_wilting_point_wet : float,
    Field_capacity_wet : float,
    soil_depth : float,
    Crop_Cover: float,
    Reference_Crop_Evapotranspiration : float,
    infiltration : float = None,
    Available_Evaporable_Water_in_previous_step : float = None,
    initial_Available_Evaporable_Water : float = None
) -> float:

    """
    Description
    -----------
    calculate Evapotranspiration_noncovered_areas With Ke and cc and ET0 - eq 4 in E:\Term2\payan_name\Modules\Evapotranspiration\Real.docx 
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
        Crop_Cover in no units
    Reference_Crop_Evapotranspiration : float
        Reference_Crop_Evapotranspiration in mm
    infiltration : float
        infiltration in mm
    Available_Evaporable_Water_in_previous_step : float
        Available_Evaporable_Water_in_previous_step in mm
    initial_Available_Evaporable_Water : float
        initial_Available_Evaporable_Water in mm - If we are on the first day, we must enter a hypothetical value
   
    Returns
    -------
    Evapotranspiration_noncovered_areas : float
        Evapotranspiration_noncovered_areas in mm
    
    """
    
    Ke = Ratio_ac_evW_to_total.ratio_of_actual_evaporable_water_to_total_evaporable_water(
        Is_in_fisrt_step = Is_in_fisrt_step,
        Permanent_wilting_point_wet = Permanent_wilting_point_wet,
        Field_capacity_wet = Field_capacity_wet,
        soil_depth = soil_depth,
        Crop_Cover = Crop_Cover,
        Reference_Crop_Evapotranspiration = Reference_Crop_Evapotranspiration,
        infiltration = infiltration,
        Available_Evaporable_Water_in_previous_step = Available_Evaporable_Water_in_previous_step,
        initial_Available_Evaporable_Water = initial_Available_Evaporable_Water
    )

    return (1 - Crop_Cover) * Reference_Crop_Evapotranspiration * Ke



# print(e_noncovered(
#     Is_in_fisrt_step = True,
#     Permanent_wilting_point_wet = 20,
#     Field_capacity_wet = 60,
#     soil_depth = 250,
#     Crop_Cover = 0.4,
#     Reference_Crop_Evapotranspiration = 2,
#     initial_Available_Evaporable_Water = 145))
