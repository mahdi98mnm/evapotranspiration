from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import constant


def soil_water_content_of_first_layer(
    soil_water_content_of_first_layer_at_previous_step: float,
    infiltration: float,
    evaporation: float,
    infiltration_to_lower_layer: float,
    field_capacity_soil_water_content_of_first_layer: float,
    permanent_wilting_point_soil_water_content_of_first_layer: float,
    growing_season: bool
) -> float:
    """
    Description
    ------------
    calculating soil water content of first layer
    ------------
    soil_water_content_of_first_layer_at_previous_step: float
        soil water content of firts layer at previous step in milimeter
    infiltration: float
        infiltration in milimeter
    evaporation: float
        evaporation in milimeter
    infiltration_to_lower_layer: float
        infiltration to lower layer in milimeter
    field_capacity_soil_water_content_of_first_layer: float
        field capacity soil water content of first layer in percent
    permanent_wilting_point_soil_water_content_of_first_layer: float
        permanent wilting point soil water content of first layer in percent
    growing_season: bool
        growing season yes(True) or no(False)
    ------------
    Returns
    ------------
    first one: soil_water_content_of_first_layer: float
        soil water content of first layer in milimeter
    second one: evaporation: float
        evaporation in milimeter
    third one: infiltration_to_lower_layer: float
        infiltration to lower layer in milimeter
    """

    if growing_season is True:
        first_layer_soil_depth = constant.soil_depth.get('first_layer_covered')
    else:
        first_layer_soil_depth = constant.soil_depth.get(
            'first_layer_not_covered')

    temp_1 = (soil_water_content_of_first_layer_at_previous_step + infiltration - evaporation - infiltration_to_lower_layer)

    temp_2 = (field_capacity_soil_water_content_of_first_layer /100) * (first_layer_soil_depth * 10)

    temp_3 = (permanent_wilting_point_soil_water_content_of_first_layer / 100) * (first_layer_soil_depth * 10)

    if temp_1 < temp_3:
        temp_1 = temp_3
        evaporation = soil_water_content_of_first_layer_at_previous_step - temp_3
        return temp_1, evaporation, infiltration_to_lower_layer

    elif temp_1 > temp_2:
        infiltration_to_lower_layer = temp_1 - temp_2
        temp_1 = temp_2
        return temp_1, evaporation, infiltration_to_lower_layer

    else:
        return temp_1, evaporation, infiltration_to_lower_layer


# Test : PWP < soil water content < FC
# print(soil_water_content_of_first_layer(
#     field_capacity_soil_water_content_of_first_layer=40,
#     permanent_wilting_point_soil_water_content_of_first_layer=20,
#     soil_water_content_of_first_layer_at_previous_step=10,
#     infiltration=20,
#     evaporation=2,
#     infiltration_to_lower_layer=5,
#     growing_season=True
# ))


# Test : soil water content > FC
# print(soil_water_content_of_first_layer(
#     field_capacity_soil_water_content_of_first_layer=40,
#     permanent_wilting_point_soil_water_content_of_first_layer=20,
#     soil_water_content_of_first_layer_at_previous_step=10,
#     infiltration=40,
#     evaporation=2,
#     infiltration_to_lower_layer=5,
#     growing_season=True
# ))


# Test : PWP > soil water content
# print(soil_water_content_of_first_layer(
#     field_capacity_soil_water_content_of_first_layer=40,
#     permanent_wilting_point_soil_water_content_of_first_layer=20,
#     soil_water_content_of_first_layer_at_previous_step=21,
#     infiltration=4,
#     evaporation=2,
#     infiltration_to_lower_layer=5,
#     growing_season=True
# ))