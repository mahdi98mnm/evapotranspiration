from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import constant


def soil_water_content_of_third_layer(
    growing_season: bool,
    field_capacity_soil_water_content_of_third_layer: float,
    permanent_wilting_point_soil_water_content_of_third_layer: float,
    soil_water_content_of_third_layer_at_previous_step: float,
    deep_percolation: float,
    upward_flux_to_upper_layer: float = 0,
    infiltration_from_upper_layer: float = 0
) -> float:
    """
    Description
    ------------
    calculating soil water content of third layer
    ------------
    growing_season: bool
        growing season yes or no
    field_capacity_soil_water_content_of_third_layer: float
        field capacity soil water content of third layer in percent
    permanent_wilting_point_soil_water_content_of_third_layer: float
        permanent wilting point soil water content of third layer in percent
    soil_water_content_of_third_layer_at_previous_step: float
        soil water content of third layer at previous step in milimeter
    deep_percolation: float
        deep percolation in milimeter
    infiltration_from_upper_layer: float
        infiltration from upper layer in milimeter
    upward_flux_to_upper_layer: float
        upward flux to upper layer in milimeter
    ------------
    Returns
    ------------
    first one: soil_water_content_of_third_layer: float
        soil water content of third layer in milimeter
    second one: upward_flux_to_upper_layer: float
        upward flux to upper layer in milimeter
    third one: deep_percolation: float
        deep percolation in milimeter
    """
    if upward_flux_to_upper_layer > 0:
        infiltration_from_upper_layer = 0
    
    if infiltration_from_upper_layer > 0:
        upward_flux_to_upper_layer = 0

    if growing_season is True:
        third_layer_soil_depth = constant.soil_depth.get('third_layer_covered')

        temp_1 = (soil_water_content_of_third_layer_at_previous_step - deep_percolation +
                  infiltration_from_upper_layer - upward_flux_to_upper_layer)

        temp_2 = (field_capacity_soil_water_content_of_third_layer /
                  100) * (third_layer_soil_depth * 10)

        temp_3 = (permanent_wilting_point_soil_water_content_of_third_layer /
                  100) * (third_layer_soil_depth * 10)

        if temp_1 < temp_3:
            upward_flux_from_lower_layer = upward_flux_from_lower_layer - (temp_3 - temp_1) 
            # upward_flux_to_upper_layer = (
            #     soil_water_content_of_third_layer_at_previous_step - deep_percolation - temp_3)
            temp_1 = temp_3
            return temp_1, upward_flux_to_upper_layer, deep_percolation

        elif temp_1 > temp_2:
            deep_percolation = (temp_1 - temp_2)
            temp_1 = temp_2
            return temp_1, upward_flux_to_upper_layer, deep_percolation

        else:
            return temp_1, upward_flux_to_upper_layer, deep_percolation

    else:
        return('while there is no crop, third layer is not defined ')


# test
# print(soil_water_content_of_third_layer(
#     growing_season = True,
#     field_capacity_soil_water_content_of_third_layer = 40,
#     permanent_wilting_point_soil_water_content_of_third_layer = 20,
#     soil_water_content_of_third_layer_at_previous_step = 200,
#     deep_percolation = 10,
#     upward_flux_to_upper_layer = 0,
#     infiltration_from_upper_layer = 20))