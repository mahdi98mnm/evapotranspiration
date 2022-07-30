

def available_Water(
    Permanent_wilting_point_wet : float,
    Field_capacity_wet : float,
    soil_depth : float
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
    soil_depth : float
        soil_depth in mm
   
    Returns
    -------
    Available_Water : float
        Available_Water in No units
    
    """
    FC = Field_capacity_wet * soil_depth
    PWP = Permanent_wilting_point_wet * soil_depth

    return (FC - PWP) / 100


# print(available_Water(Permanent_wilting_point_wet = 20, Field_capacity_wet = 60, soil_depth = 250))

