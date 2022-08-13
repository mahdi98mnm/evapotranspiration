from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import constant


def calculate_upward_flux(
    root_depth: float,
    field_capacity_soil_water_content_of_second_layer: float,
    field_capacity_soil_water_content_of_third_layer: float,
    permanent_wilting_point_soil_water_content_of_second_layer: float,
    permanent_wilting_point_soil_water_content_of_third_layer: float,
    soil_water_content_of_second_layer_at_previous_step: float,
    soil_water_content_of_third_layer_at_previous_step: float,
    hydraulic_conductivity_of_third_layer: float
) -> float:
    """
    Description
    ------------
    calculating soil water content of third layer
    ------------
    root_depth: float
        root depth in cm
    field_capacity_soil_water_content_of_second_layer: float
        field capacity soil water content of second layer in percent
    field_capacity_soil_water_content_of_third_layer: float
        field capacity soil water content of third layer in percent
    permanent_wilting_point_soil_water_content_of_second_layer: float
        permanent wilting point soil water content of second layer in percent
    permanent_wilting_point_soil_water_content_of_third_layer: float
        permanent wilting point soil water content of third layer in percent
    soil_water_content_of_second_layer_at_previous_step: float
        soil water content of second layer at previous step in milimeter
    soil_water_content_of_third_layer_at_previous_step: float
        soil water content of third layer at previous step in milimeter
    hydraulic_conductivity_of_third_layer: float
        hydraulic conductivity of third layer in milimeter per day
    ------------
    Returns
    ------------
    upward_flux_to_upper_layer: float
        upward flux to upper layer in milimeter
    """

    third_layer_soil_depth = constant.soil_depth.get('third_layer_covered')
    if soil_water_content_of_second_layer_at_previous_step >= soil_water_content_of_third_layer_at_previous_step:
        return 0
    
    else:
        temp_1 = (field_capacity_soil_water_content_of_second_layer /
                  100) * (root_depth * 10)

        temp_2 = (field_capacity_soil_water_content_of_third_layer /
                  100) * (third_layer_soil_depth * 10)

        temp_3 = (permanent_wilting_point_soil_water_content_of_second_layer /
                  100) * (root_depth * 10)

        temp_4 = (permanent_wilting_point_soil_water_content_of_third_layer /
                  100) * (third_layer_soil_depth * 10)

        t2 = (soil_water_content_of_second_layer_at_previous_step - temp_3) / (temp_1 - temp_3)

        t3 = (soil_water_content_of_third_layer_at_previous_step - temp_4) / (temp_2 - temp_4)

        alpha = (t3 - t2) * t3
        
        return alpha * hydraulic_conductivity_of_third_layer
