from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import constant

# khoroji ha hamegi float bashad ... toye return ha float ezafe shvad khob ast?
def soil_water_content_of_transp_layer(
    coverd: bool,
    field_capacity_soil_water_content_of_transp_layer: float,
    permanent_wilting_point_soil_water_content_of_transp_layer: float,
    soil_water_content_of_transp_layer_at_previous_step: float,
    stress_coefficient : float,
    infiltration_from_evap_to_transp_layer : float = 0,
    infiltration_from_transp_to_trans_layer : float = 0,
    transpiration: float = 0,
    upward_flux_from_trans_to_transp_layer: float = 0,
    upward_flux_from_transp_to_evap_layer: float = 0,
    root_depth: float = 0,
    MAD: float = 0
) -> float:
    """
    Description
    ------------
    calculating soil water content of transp layer
    ------------
    coverd: bool
        corved yes(True) or not coverd no(False)
    field_capacity_soil_water_content_of_transp_layer: float
        feild capacity soil water content of transp layer in percent
    permanent_wilting_point_soil_water_content_of_transp_layer: float
        permanent wilting point soil water content of transp layer in percent
    soil_water_content_of_transp_layer_at_previous_step: float
        soil water content of transp layer at previous step in milimeter
    stress_coefficient : float
        deficit irrigation - between 0 - 1 in unitless
    infiltration_from_evap_to_transp_layer : float
        infiltration from evaporation to transpiration layer in milimeter
    infiltration_from_transp_to_trans_layer : float
        infiltration from transpiration to transition layer in milimeter
    transpiration: float
        transpiration in milimeter
    upward_flux_from_trans_to_transp_layer: float
        upward flux from transition to transpiration layer in milimeter
    upward_flux_from_transp_to_evap_layer: float
        upward flux from transpiration to evaporation layer in milimeter
    root_depth: float
        root depth in cm
    MAD: float
        MAD(Maximum Allowable Depletion) between 0 to 1
    ------------
    Returns
    ------------
    soil_water_content_of_transp_layer: float
        soil water content of transp layer in milimeter
    """
    
    

    if coverd is False:
        return "Transpiration layer is not defined"
    else:
        if infiltration_from_evap_to_transp_layer > 0:
            upward_flux_from_transp_to_evap_layer = 0

        if infiltration_from_transp_to_trans_layer > 0:
            upward_flux_from_trans_to_transp_layer = 0
        
        if infiltration_from_transp_to_trans_layer > 0:
            upward_flux_from_transp_to_evap_layer = 0
        
        transp_layer_soil_depth = root_depth

        temp_1 = (soil_water_content_of_transp_layer_at_previous_step + infiltration_from_evap_to_transp_layer + upward_flux_from_trans_to_transp_layer
                - transpiration - upward_flux_from_transp_to_evap_layer - infiltration_from_transp_to_trans_layer)

        temp_2 = (field_capacity_soil_water_content_of_transp_layer / 100) * (transp_layer_soil_depth * 10)

        temp_3 = (permanent_wilting_point_soil_water_content_of_transp_layer / 100) * (transp_layer_soil_depth * 10)
        
        if temp_1 <= temp_3:
            temp_1 = temp_3
            transpiration = (soil_water_content_of_transp_layer_at_previous_step - temp_3 + upward_flux_from_trans_to_transp_layer)
            # transpiration = (soil_water_content_of_transp_layer_at_previous_step - upward_flux_from_transp_to_evap_layer + upward_flux_from_trans_to_transp_layer)
            # in porside she ke kodom dorste - faghat toye manfi tafafod dare

            return temp_1

        elif temp_1 >= temp_2:
            infiltration_from_transp_to_trans_layer = temp_1 - temp_2
            temp_1 = temp_2

            return temp_1

        elif temp_3 < temp_1 < temp_2:
            temp_4 = (temp_2 - temp_3) * MAD
            if temp_1 >= temp_4:

                return temp_1

            else:
                irrigation_requirement = stress_coefficient * (temp_2 - temp_1)
                temp_1 = temp_2
                return temp_1


# test
# kamtar az PWP
# print(soil_water_content_of_transp_layer(
#     coverd = True,
#     field_capacity_soil_water_content_of_transp_layer = 40,
#     permanent_wilting_point_soil_water_content_of_transp_layer = 10,
#     soil_water_content_of_transp_layer_at_previous_step = 100,
#     infiltration_from_evap_to_transp_layer = 5,
#     infiltration_from_transp_to_trans_layer = 2,
#     stress_coefficient = 0.8,
#     transpiration = 5,
#     upward_flux_from_trans_to_transp_layer = 5,
#     upward_flux_from_transp_to_evap_layer = 5,
#     root_depth = 100,
#     MAD = 0.5)
# )

# bishtar az FC
# print(soil_water_content_of_transp_layer(
#     coverd = True,
#     field_capacity_soil_water_content_of_transp_layer = 40,
#     permanent_wilting_point_soil_water_content_of_transp_layer = 10,
#     soil_water_content_of_transp_layer_at_previous_step = 400,
#     infiltration_from_evap_to_transp_layer = 20,
#     infiltration_from_transp_to_trans_layer = 2,
#     stress_coefficient = 0.8,
#     transpiration = 5,
#     upward_flux_from_trans_to_transp_layer = 5,
#     upward_flux_from_transp_to_evap_layer = 5,
#     root_depth = 100,
#     MAD = 0.5)
# )

# bishtar az MAD
# print(soil_water_content_of_transp_layer(
#     coverd = True,
#     field_capacity_soil_water_content_of_transp_layer = 40,
#     permanent_wilting_point_soil_water_content_of_transp_layer = 10,
#     soil_water_content_of_transp_layer_at_previous_step = 180,
#     infiltration_from_evap_to_transp_layer = 20,
#     infiltration_from_transp_to_trans_layer = 2,
#     stress_coefficient = 0.8,
#     transpiration = 5,
#     upward_flux_from_trans_to_transp_layer = 5,
#     upward_flux_from_transp_to_evap_layer = 5,
#     root_depth = 100,
#     MAD = 0.5)
# )

# kamtar az MAD
# print(soil_water_content_of_transp_layer(
#     coverd = True,
#     field_capacity_soil_water_content_of_transp_layer = 40,
#     permanent_wilting_point_soil_water_content_of_transp_layer = 10,
#     soil_water_content_of_transp_layer_at_previous_step = 130,
#     infiltration_from_evap_to_transp_layer = 20,
#     infiltration_from_transp_to_trans_layer = 2,
#     stress_coefficient = 0.8,
#     transpiration = 5,
#     upward_flux_from_trans_to_transp_layer = 5,
#     upward_flux_from_transp_to_evap_layer = 5,
#     root_depth = 100,
#     MAD = 0.5)
# )