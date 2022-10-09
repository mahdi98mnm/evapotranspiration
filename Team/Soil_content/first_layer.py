from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import constant

# khoroji ha hamegi float bashad ... toye return ha float ezafe shvad khob ast?
def soil_water_content_of_evap_layer(
    soil_water_content_of_evap_layer_at_previous_step: float,
    infiltration: float,
    evaporation: float,
    field_capacity_soil_water_content_of_evap_layer: float,
    permanent_wilting_point_soil_water_content_of_evap_layer: float,
    coverd : bool,
    infiltration_to_transp_layer: float = 0,
    infiltration_to_trans_layer: float = 0,
) -> float:
    """
    Description
    ------------
    calculating soil water content of evap layer
    ------------
    soil_water_content_of_evap_layer_at_previous_step: float
        soil water content of firts layer at previous step in milimeter
    infiltration: float
        infiltration in milimeter
    evaporation: float
        evaporation in milimeter
    field_capacity_soil_water_content_of_evap_layer: float
        field capacity soil water content of evap layer in percent
    permanent_wilting_point_soil_water_content_of_evap_layer: float
        permanent wilting point soil water content of evap layer in percent
    coverd: bool
        corved yes(True) or not coverd no(False)
    infiltration_to_transp_layer: float
        infiltration to transpiration layer in milimeter
    infiltration_to_trans_layer: float
        infiltration to transition layer in milimeter
    ------------
    Returns
    ------------
    
    soil_water_content_of_evap_layer: float
        soil water content of evap layer in milimeter
    """

    if coverd is True:
        evap_layer_soil_depth = constant.soil_depth.get('evap_layer_covered')
        temp_1 = (soil_water_content_of_evap_layer_at_previous_step + infiltration - evaporation - infiltration_to_transp_layer)
    else:
        infiltration_to_transp_layer = 0
        evap_layer_soil_depth = constant.soil_depth.get(
            'evap_layer_not_covered')
        temp_1 = (soil_water_content_of_evap_layer_at_previous_step + infiltration - evaporation - infiltration_to_trans_layer)


    temp_2 = (field_capacity_soil_water_content_of_evap_layer /100) * (evap_layer_soil_depth * 10)

    temp_3 = (permanent_wilting_point_soil_water_content_of_evap_layer / 100) * (evap_layer_soil_depth * 10)

    if temp_1 <= temp_3:
        temp_1 = temp_3
        evaporation = soil_water_content_of_evap_layer_at_previous_step - temp_3
        return temp_1

    elif temp_1 >= temp_2:
        if coverd is True:
            infiltration_to_transp_layer = temp_1 - temp_2
            temp_1 = temp_2
        else:
            infiltration_to_trans_layer = temp_1 - temp_2
            temp_1 = temp_2

        return temp_1

    else:
        return temp_1

# khorogi an be soorat integer ast vali bayad float bashad
# Test : PWP < soil water content < FC
# print(soil_water_content_of_evap_layer(
#     field_capacity_soil_water_content_of_evap_layer=40,
#     permanent_wilting_point_soil_water_content_of_evap_layer=20,
#     soil_water_content_of_evap_layer_at_previous_step=10,
#     infiltration_to_transp_layer = 5.2,
#     infiltration_to_trans_layer = 5,
#     infiltration=20,
#     evaporation=2,
#     coverd=True
# ))

# Test : soil water content > FC
# print(soil_water_content_of_evap_layer(
#     field_capacity_soil_water_content_of_evap_layer=40,
#     permanent_wilting_point_soil_water_content_of_evap_layer=20,
#     soil_water_content_of_evap_layer_at_previous_step=10,
#     infiltration=40,
#     evaporation=2,
#     infiltration_to_transp_layer = 5,
#     infiltration_to_trans_layer = 5,
#     coverd=True
# ))


# Test : PWP > soil water content
# print(soil_water_content_of_evap_layer(
#     field_capacity_soil_water_content_of_evap_layer=40,
#     permanent_wilting_point_soil_water_content_of_evap_layer=20,
#     soil_water_content_of_evap_layer_at_previous_step=21,
#     infiltration=4,
#     evaporation=2,
#     infiltration_to_transp_layer = 5,
#     infiltration_to_trans_layer = 5,
#     coverd=True
# ))