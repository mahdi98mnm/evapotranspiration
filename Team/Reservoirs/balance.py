
import math
import func


def Volume_Water2(
    Height : float,
    Height_min : float,
    Height_max : float,
    Area_max : float,
    a : float,
    p : float, 
    Volume_Runoff : float, 
    Volume_Groundwater : float,
    Precipitation : float,
    Volume_evaporation : float, 
    Volume_Wier : float,
    Volume_Infiltration : float, 
    Volume_Use : float,
    A : float = None
) -> float:
    
    """
    Description
    -----------
    Estimate Volume of left over water in reservoir(Volume_water2) Using the Balance equation for reservoirs
    **Reference**: Based on Equation Nouvelot, J.F. (1993) 
    Parameters
    ----------
    Height : float
        height in m
    Height_min : float
        minimum height in m
    Height_max : float
        maximum height in m
    Area_max : float
        Area in m^2 is maximum af Area of water in reservoir = Height_max * Area
    a : float
    p: float
        a and p are adjustable parameters
        a>0 and p>1
    Volume_Runoff : float
        Volume of runoff that enter reservoir from watershed in m**3
    Volume_groundwater : float
        volume that enters from groundwater in m**3
    precipitation : float
        rainfall on reservoir in m
    Volume_evaporation : float
        volume of water that vape from reservoir through time in m**3
    Volume_Wier : float
        The volume of water discharged from the tank. When overflow is measured, this can be determined with good accuracy.
         For most tanks, it is enough to use the appropriate overflow formula with its geometry in m**3
    Volume_infiltration : float
        volume of water that penetrate and seepage in m^3 Can Be Calculated Using ``func.Volume_infiltration()``
    Volume_Use : float
        volume of water that release and use in downstream with diffrent purposes in m^3
    
    volume_water : float
        Volume of water at the start time in m^3
        it's diffrences from type of reservoirs
        reservoir considered as a unadjustable reservoir 
    Volume_Percipitation : float
        volume of percipitation that falls on the reservoir in m^3 Can Be Calculated Using ``func.Volume_Percipitation()``
    
    
    Returns
    -------
    Volume_water2 : float
        volume of water that remain in the reservoir at the end of the time
    """
    V_1 = func.Volume_Water(
        Height = Height,
        Height_min = Height_min,
        Height_max = Height_max,
        Area_max = Area_max,
        a = a,
        p = p
    )

    V_2 = func.Volume_precipitation(
        Precipitation = Precipitation,
        Height = Height,
        Height_min = Height_min,
        Height_max = Height_max,
        Area_max = Area_max,
        a = a,
        p = p,
        A = A
    )
    return V_1 + (Volume_Runoff + Volume_Groundwater + V_2) - (
        Volume_evaporation + Volume_Wier + Volume_Infiltration + Volume_Use)


print(Volume_Water2(
    Height = 990,
    Height_min = 968,
    Height_max = 1050,
    Area_max = 47000000,
    a = 0.5,
    p = 1.5, 
    Volume_Runoff = 100000000, 
    Volume_Groundwater = 10000000,
    Precipitation = 0.2,
    Volume_evaporation = 200000000,
    Volume_Wier = 1000000,
    Volume_Infiltration = 10000000,
    Volume_Use = 500000000,
    A = 40000000))