from cmath import exp
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import math

def Total_evaporable_water(
    Permanent_wilting_point_wet : float,
    Field_capacity_wet : float
) -> float:

    """
    Description
    -----------
    calculate Total_evaporable_water or Available_water With FC and PWP 
    ----------
    Permanent_wilting_point_wet : float
        Permanent_wilting_point_wet in percent(volumetric)
    Field_capacity_wet : float
        Field_capacity_wet in percent(volumetric)
   
    Returns
    -------
    Total_evaporable_water : float
        Total_evaporable_water in No units
    
    """

    return (Field_capacity_wet - Permanent_wilting_point_wet) / 100

dfbhdfj

def Available_Evaporable_Water(
    infiltration_rate : float,
    Available_Evaporable_Water_in_previous_step : float,
    
    Permanent_wilting_point_wet : float,
    Field_capacity_wet : float
) -> float:

    """
    Description
    -----------
    calculate Available_water With FC and PWP 
    ----------
    Permanent_wilting_point_wet : float
        Permanent_wilting_point_wet in percent(volumetric)
    Field_capacity_wet : float
        Field_capacity_wet in percent(volumetric)
   
    Returns
    -------
    moisture_reduction_function : float
        moisture_reduction_function in No units
    
    """

    return (Field_capacity_wet - Permanent_wilting_point_wet) / 100






def ratio_of_actual_evaporable_water_to_total_evaporable_water(
    Available_Evaporable_Water : float,
    initial_Available_Evaporable_Water : float,
    Is_in_fisrt_step : bool,
    Total_evaporable_water : float
) -> float:
    
    """
    Description
    -----------
    calculate ratio of actual evaporable water to total evaporable water - eq 5 in E:\Term2\payan_name\Modules\Evapotranspiration\Real.docx
    ----------
    Available_Evaporable_Water : float
        Available_Evaporable_Water in mm
    initial_Available_Evaporable_Water : float
        initial_Available_Evaporable_Water in mm - If we are on the first day, we must enter a hypothetical value
    Is_in_fisrt_step : bool
        Is_in_fisrt_step in boolean - True if we are on the first day, False if we are not on the first day
    Total_evaporable_water : float
        Total_evaporable_water in mm
   
    Returns
    -------
    ratio_of_actual_evaporable_water_to_total_evaporable_water : float
        ratio_of_actual_evaporable_water_to_total_evaporable_water in No units
    """
    if Is_in_fisrt_step is True:
        ratio = initial_Available_Evaporable_Water / Total_evaporable_water

    else:
        ratio = Available_Evaporable_Water / Total_evaporable_water
    
    return ratio


def Available_water(
    Permanent_wilting_point_wet : float,
    Field_capacity_wet : float
) -> float:

    """
    Description
    -----------
    calculate Available_water With FC and PWP 
    ----------
    Permanent_wilting_point_wet : float
        Permanent_wilting_point_wet in percent(volumetric)
    Field_capacity_wet : float
        Field_capacity_wet in percent(volumetric)
   
    Returns
    -------
    moisture_reduction_function : float
        moisture_reduction_function in No units
    
    """

    return (Field_capacity_wet - Permanent_wilting_point_wet) / 100









def moisture_reduction_function(
    Soil_wetness_in_previous_step : float,
    Permanent_wilting_point_wet : float,
    Field_capacity_wet : float
) -> float:
    
    """
    Description
    -----------
    calculate moisture reduction function With FC and PWP and SW(t-1) - eq 2 in E:\Term2\payan_name\Modules\Evapotranspiration\Real.docx
    ----------
    Soil_wetness_in_previous_step : float
        Soil_wetness_in_previous_step in percent(volumetric)
    Permanent_wilting_point_wet : float
        Permanent_wilting_point_wet in percent(volumetric)
    Field_capacity_wet : float
        Field_capacity_wet in percent(volumetric)
   
    Returns
    -------
    moisture_reduction_function : float
        moisture_reduction_function in No units
    """
    
    return (Soil_wetness_in_previous_step - Permanent_wilting_point_wet) / (Field_capacity_wet - Permanent_wilting_point_wet)



