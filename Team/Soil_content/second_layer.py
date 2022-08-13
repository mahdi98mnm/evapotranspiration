from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import constant


def soil_water_content_of_second_layer(
    growing_season: bool,
    field_capacity_soil_water_content_of_second_layer: float,
    permanent_wilting_point_soil_water_content_of_second_layer: float,
    soil_water_content_of_second_layer_at_previous_step: float,
    infiltration_from_upper_layer: float,
    transpiration: float = 0,
    infiltration_to_lower_layer: float = 0,
    upward_flux_from_lower_layer: float = 0,
    upward_flux_to_upper_layer: float = 0, #new...Add in flowchart
    deep_percolation: float = 0,
    root_depth: float = 0,
    MAD: float = 0
) -> float:
    """
    Description
    ------------
    calculating soil water content of second layer
    ------------
    growing_season: bool
        growing season yes or no
    field_capacity_soil_water_content_of_second_layer: float
        feild capacity soil water content of second layer in percent
    permanent_wilting_point_soil_water_content_of_second_layer: float
        permanent wilting point soil water content of second layer in percent

    soil_water_content_of_second_layer_at_previous_step: float
        soil water content of second layer at previous step in milimeter
    infiltration_from_upper_layer: float
        infiltration from upper layer in milimeter
    transpiration: float
        transpiration in milimeter
    infiltration_to_lower_layer: float
        infiltration to lower layer in milimeter
    upward_flux_from_lower_layer: float
        upward flux from lower layer in milimeter
    deep_percolation: float
        deep percolation in milimeter
    root_depth: float
        root depth in cm
    MAD: float
        MAD between 0 to 1
    ------------
    Returns
    ------------
    first one: soil_water_content_of_second_layer: float
        soil water content of second layer in milimeter
    second one: transpiration
        transpiration in milimeter
    third one: infiltration_to_lower_layer
        infiltration to lower layer in milimeter
    forth one: irrigation_requirement: float
        irrigation requirement in milimeter
    fifth one: deep_percolation: float
        deep percolation in milimeter
    """
    if upward_flux_from_lower_layer > 0:
        infiltration_to_lower_layer = 0
    
    if infiltration_to_lower_layer > 0:
        upward_flux_from_lower_layer = 0


    irrigation_requirement = 0

    if growing_season is True:
        deep_percolation = 0
        second_layer_soil_depth = root_depth

        temp_1 = (soil_water_content_of_second_layer_at_previous_step +
                  infiltration_from_upper_layer - transpiration - infiltration_to_lower_layer +
                  upward_flux_from_lower_layer)

        temp_2 = (field_capacity_soil_water_content_of_second_layer /
                  100) * (second_layer_soil_depth * 10)

        temp_3 = (permanent_wilting_point_soil_water_content_of_second_layer /
                  100) * (second_layer_soil_depth * 10)
        
        if temp_1 < temp_3:
            temp_1 = temp_3
            transpiration = (soil_water_content_of_second_layer_at_previous_step -
                             temp_3 + upward_flux_from_lower_layer)
            return temp_1, transpiration, infiltration_to_lower_layer, irrigation_requirement, deep_percolation

        elif temp_1 > temp_2:
            infiltration_to_lower_layer = temp_1 - temp_2
            temp_1 = temp_2
            return temp_1, transpiration, infiltration_to_lower_layer, irrigation_requirement, deep_percolation

        elif temp_3 < temp_1 < temp_2:
            temp_4 = (temp_2 - temp_3) * MAD
            if temp_1 > temp_4:
                return temp_1, transpiration, infiltration_to_lower_layer, irrigation_requirement, deep_percolation

            else:
                irrigation_requirement = temp_2 - temp_4
                temp_1 = temp_2
                return temp_1, transpiration, infiltration_to_lower_layer, irrigation_requirement, deep_percolation

    else:
        transpiration = 0
        infiltration_to_lower_layer = 0
        second_layer_soil_depth = constant.soil_depth.get(
            'second_layer_not_covered')

        temp_1 = (soil_water_content_of_second_layer_at_previous_step +
                  infiltration_from_upper_layer - deep_percolation - upward_flux_to_upper_layer)

        temp_2 = (field_capacity_soil_water_content_of_second_layer /
                  100) * (second_layer_soil_depth * 10)

        temp_3 = (permanent_wilting_point_soil_water_content_of_second_layer /
                  100) * (second_layer_soil_depth * 10)

        if temp_1 > temp_2:
            deep_percolation = temp_1 - temp_2
            temp_1 = temp_2
            return temp_1, transpiration, infiltration_to_lower_layer, irrigation_requirement, deep_percolation

        elif temp_1 < temp_3:
            temp_1 = temp_3
            upward_flux_to_upper_layer = upward_flux_to_upper_layer - (temp_3 - temp_1) 
            # deep_percolation = (
            #     soil_water_content_of_second_layer_at_previous_step + infiltration_from_upper_layer - temp_3)
            return temp_1, transpiration, infiltration_to_lower_layer, irrigation_requirement, deep_percolation

        else:
            return temp_1, transpiration, infiltration_to_lower_layer, irrigation_requirement, deep_percolation


# test
# print(soil_water_content_of_second_layer(
#     growing_season = True,
#     field_capacity_soil_water_content_of_second_layer = 40,
#     permanent_wilting_point_soil_water_content_of_second_layer = 20,
#     soil_water_content_of_second_layer_at_previous_step = 70,
#     infiltration_from_upper_layer = 150,
#     transpiration = 5,
#     infiltration_to_lower_layer = 3,
#     upward_flux_from_lower_layer = 0,
#     deep_percolation = 0,
#     root_depth = 100,
#     MAD = 0.5)
# )
