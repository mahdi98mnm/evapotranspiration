from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import constant


def calculate_upward_flux(
    coverd: bool,
    field_capacity_soil_water_content_of_evap_layer: float,
    field_capacity_soil_water_content_of_trans_layer: float,
    permanent_wilting_point_soil_water_content_of_evap_layer: float,
    permanent_wilting_point_soil_water_content_of_trans_layer: float,
    soil_water_content_of_evap_layer_at_previous_step: float,
    soil_water_content_of_trans_layer_at_previous_step: float, 
    hydraulic_conductivity_of_trans_layer: float,
    field_capacity_soil_water_content_of_transp_layer: float = None,
    permanent_wilting_point_soil_water_content_of_transp_layer: float = None,
    soil_water_content_of_transp_layer_at_previous_step: float = None,
    hydraulic_conductivity_of_transp_layer: float = None,
    root_depth: float = None,
) -> float:
    """
    Description
    ------------
    calculating soil water content of trans layer
    ------------
    coverd: bool
        corved yes(True) or not coverd no(False)
    root_depth: float
        root depth in cm
    field_capacity_soil_water_content_of_evap_layer : float
        field capacity soil water content of evaporation layer in percent
    field_capacity_soil_water_content_of_transp_layer: float
        field capacity soil water content of transpiration layer in percent
    field_capacity_soil_water_content_of_trans_layer: float
        field capacity soil water content of transition layer in percent
    permanent_wilting_point_soil_water_content_of_evap_layer : float
        permanent wilting point soil water content of evaporation layer in percent
    permanent_wilting_point_soil_water_content_of_transp_layer: float
        permanent wilting point soil water content of transpiration layer in percent
    permanent_wilting_point_soil_water_content_of_trans_layer: float
        permanent wilting point soil water content of transition layer in percent
    soil_water_content_of_evap_layer_at_previous_step : float
        soil water content of evaporation layer at previous step in milimeter
    soil_water_content_of_transp_layer_at_previous_step: float
        soil water content of transpiration layer at previous step in milimeter
    soil_water_content_of_trans_layer_at_previous_step: float
        soil water content of transition layer at previous step in milimeter
    hydraulic_conductivity_of_transp_layer: float
        hydraulic conductivity of transpiration layer in milimeter per day
    hydraulic_conductivity_of_trans_layer: float
        hydraulic conductivity of transition layer in milimeter per day
    ------------
    Returns
    ------------
    upward_transp_to_evap: float
        upward flux from transpiration to evaporation layer in milimeter
    upward_trans_to_transp
        upward flux from transition to transpiration layer in milimeter
    upward_trans_to_evap
        upward flux from transition to evaporation layer in milimeter
    """

    

    evap_layer_soil_depth = constant.soil_depth.get('evap_layer_covered')
    trans_layer_soil_depth = constant.soil_depth.get('trans_layer_covered')
    temp_1_fc = (field_capacity_soil_water_content_of_evap_layer / 100) * (evap_layer_soil_depth * 10)
    temp_3_fc = (field_capacity_soil_water_content_of_trans_layer / 100) * (trans_layer_soil_depth * 10)
    temp_1_pwp = (permanent_wilting_point_soil_water_content_of_evap_layer / 100) * (evap_layer_soil_depth * 10)
    temp_3_pwp = (permanent_wilting_point_soil_water_content_of_trans_layer / 100) * (trans_layer_soil_depth * 10)
    t1 = (soil_water_content_of_evap_layer_at_previous_step - temp_1_pwp) / (temp_1_fc - temp_1_pwp)
    t3 = (soil_water_content_of_trans_layer_at_previous_step - temp_3_pwp) / (temp_3_fc - temp_3_pwp)

    
    if coverd == True :
        if soil_water_content_of_transp_layer_at_previous_step >= soil_water_content_of_trans_layer_at_previous_step:
            upward_trans_to_transp = 0


        elif soil_water_content_of_evap_layer_at_previous_step >= soil_water_content_of_transp_layer_at_previous_step:
            upward_transp_to_evap = 0

        else:
            
            temp_2_fc = (field_capacity_soil_water_content_of_transp_layer / 100) * (root_depth * 10)
            

            
            temp_2_pwp = (permanent_wilting_point_soil_water_content_of_transp_layer / 100) * (root_depth * 10)
            

            
            t2 = (soil_water_content_of_transp_layer_at_previous_step - temp_2_pwp) / (temp_2_fc - temp_2_pwp)
            

            alpha_transp_to_evap = (t2 - t1)
            alpha_trans_to_transp = (t3 - t2)

            upward_transp_to_evap = alpha_transp_to_evap * hydraulic_conductivity_of_transp_layer
            upward_trans_to_transp = alpha_trans_to_transp * hydraulic_conductivity_of_trans_layer
            upward_trans_to_evap = None

    else:
        alpha_trans_to_evap = (t3 - t1)
        upward_trans_to_evap = alpha_trans_to_evap * hydraulic_conductivity_of_trans_layer
        upward_trans_to_transp = None
        upward_transp_to_evap = None


    return upward_transp_to_evap,upward_trans_to_transp,upward_trans_to_evap

# test
# print(calculate_upward_flux(
#     coverd = True,
#     root_depth = 100,
#     field_capacity_soil_water_content_of_evap_layer = 75,
#     field_capacity_soil_water_content_of_transp_layer = 75,
#     field_capacity_soil_water_content_of_trans_layer = 75,
#     permanent_wilting_point_soil_water_content_of_evap_layer = 25,
#     permanent_wilting_point_soil_water_content_of_transp_layer = 25,
#     permanent_wilting_point_soil_water_content_of_trans_layer = 25,
#     soil_water_content_of_evap_layer_at_previous_step = 50,
#     soil_water_content_of_transp_layer_at_previous_step = 620.5,
#     soil_water_content_of_trans_layer_at_previous_step = 700,
#     hydraulic_conductivity_of_transp_layer = 1,
#     hydraulic_conductivity_of_trans_layer = 1
# ))