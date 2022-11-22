from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import constant

# khoroji ha hamegi float bashad ... toye return ha float ezafe shvad khob ast?
def soil_water_content_of_trans_layer(
    coverd: bool,
    field_capacity_soil_water_content_of_trans_layer: float,
    permanent_wilting_point_soil_water_content_of_trans_layer: float,
    soil_water_content_of_trans_layer_at_previous_step: float,
    deep_percolation: float,
    infiltration_from_transp_to_trans_layer : float = 0,
    upward_flux_from_trans_to_transp_layer: float = 0
) -> float:
    """
    Description
    ------------
    calculating soil water content of trans layer
    ------------
    coverd: bool
        corved yes(True) or not coverd no(False)
    field_capacity_soil_water_content_of_trans_layer: float
        field capacity soil water content of trans layer in percent
    permanent_wilting_point_soil_water_content_of_trans_layer: float
        permanent wilting point soil water content of trans layer in percent
    soil_water_content_of_trans_layer_at_previous_step: float
        soil water content of trans layer at previous step in milimeter
    deep_percolation: float
        deep percolation in milimeter
    infiltration_from_transp_to_trans_layer : float
        infiltration from transpiration to transition layer in milimeter
    upward_flux_from_trans_to_transp_layer: float
        upward flux from transition to transpiration layer in milimeter
    ------------
    Returns
    ------------
    soil_water_content_of_trans_layer: float
        soil water content of trans layer in milimeter
    """
    
    if coverd is False:

        return('while there is no crop, trans layer is not defined ')

        
    else:

        trans_layer_soil_depth = constant.soil_depth.get('trans_layer_covered')

        if infiltration_from_transp_to_trans_layer > 0:
            upward_flux_from_trans_to_transp_layer = 0
    
        if upward_flux_from_trans_to_transp_layer > 0:
            infiltration_from_transp_to_trans_layer = 0


        temp_1 = (soil_water_content_of_trans_layer_at_previous_step + infiltration_from_transp_to_trans_layer
                 - deep_percolation - upward_flux_from_trans_to_transp_layer)

        temp_2 = (field_capacity_soil_water_content_of_trans_layer / 100) * (trans_layer_soil_depth * 10)

        temp_3 = (permanent_wilting_point_soil_water_content_of_trans_layer / 100) * (trans_layer_soil_depth * 10)


        if temp_1 < temp_3:
            upward_flux_from_trans_to_transp_layer = upward_flux_from_trans_to_transp_layer - (temp_3 - temp_1) 
            temp_1 = temp_3

            return temp_1

        elif temp_1 > temp_2:
            deep_percolation = (temp_1 - temp_2)
            temp_1 = temp_2

            return temp_1

        else:
            return temp_1


# test
# kamtar az PWP
# print(soil_water_content_of_trans_layer(
#     coverd = True,
#     field_capacity_soil_water_content_of_trans_layer = 40,
#     permanent_wilting_point_soil_water_content_of_trans_layer = 20,
#     soil_water_content_of_trans_layer_at_previous_step = 200,
#     deep_percolation = 10,
#     infiltration_from_transp_to_trans_layer = 5,
#     upward_flux_from_trans_to_transp_layer= 5))

# bishtar az FC
# print(soil_water_content_of_trans_layer(
#     coverd = True,
#     field_capacity_soil_water_content_of_trans_layer = 40,
#     permanent_wilting_point_soil_water_content_of_trans_layer = 20,
#     soil_water_content_of_trans_layer_at_previous_step = 400,
#     deep_percolation = 5,
#     infiltration_from_transp_to_trans_layer = 10,
#     upward_flux_from_trans_to_transp_layer= 5))

# beyne PWP va FC
print(soil_water_content_of_trans_layer(
    coverd = True,
    field_capacity_soil_water_content_of_trans_layer = 40,
    permanent_wilting_point_soil_water_content_of_trans_layer = 20,
    soil_water_content_of_trans_layer_at_previous_step = 300,
    deep_percolation = 5,
    infiltration_from_transp_to_trans_layer = 10,
    upward_flux_from_trans_to_transp_layer= 5))