from cmath import exp
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import math


def moisture_reduction_function(
    Soil_wetness_in_previous_step : float,
    Permanent_wilting_point_wet : float,
    Field_capacity_wet : float,
    soil_depth : float
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
    soil_depth : float
        soil_depth in mm
    Returns
    -------
    moisture_reduction_function : float
        moisture_reduction_function in No units
    """
    
    FC = (Field_capacity_wet / 100) * soil_depth
    PWP = (Permanent_wilting_point_wet / 100) * soil_depth

    
    return (Soil_wetness_in_previous_step - PWP) / (FC - PWP)



# print(moisture_reduction_function(
#     Soil_wetness_in_previous_step = 290,
#     Permanent_wilting_point_wet = 20,
#     Field_capacity_wet = 60,
#     soil_depth = 250
# ))


def et_covered(
    Soil_wetness_in_previous_step : float,
    Permanent_wilting_point_wet : float,
    Field_capacity_wet : float,
    soil_depth : float,
    Crop_Coefficient : float,
    Crop_Cover : float,
    Reference_Crop_Evapotranspiration : float
) -> float:
    
    """
    Description
    -----------
    calculate evapotranspiration covered areas With QDWB approach - eq 3 in E:\Term2\payan_name\Modules\Evapotranspiration\Real.docx
    ----------
    Soil_wetness_in_previous_step : float
        Soil_wetness_in_previous_step in percent(volumetric)
    Permanent_wilting_point_wet : float
        Permanent_wilting_point_wet in percent(volumetric)
    Field_capacity_wet : float
        Field_capacity_wet in percent(volumetric)
    soil_depth : float
        soil_depth in mm
    Crop_Coefficient : float
        Crop_Coefficient in No units
    Crop_Cover : float
        Crop_Cover in No units
    Reference_Crop_Evapotranspiration : float
        Reference_Crop_Evapotranspiration in mm
   
    Returns
    -------
    evapotranspiration_covered_areas : float
        evapotranspiration_covered_areas in mm
    """
    f = moisture_reduction_function(
        Soil_wetness_in_previous_step = Soil_wetness_in_previous_step,
        Permanent_wilting_point_wet = Permanent_wilting_point_wet,
        Field_capacity_wet = Field_capacity_wet,
        soil_depth = soil_depth
    )
    
    return f * Crop_Coefficient * Crop_Cover * Reference_Crop_Evapotranspiration



# print(et_covered(
#     Soil_wetness_in_previous_step = 290,
#     Permanent_wilting_point_wet = 20,
#     Field_capacity_wet = 60,
#     soil_depth = 250,
#     Crop_Coefficient = 0.6,
#     Crop_Cover = 0.4,
#     Reference_Crop_Evapotranspiration = 2
#     ))