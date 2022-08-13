import math
import check

def Height_Standard(
  Height: float,
  Height_min: float,
  Height_max: float  
) -> float:
    check.check_not_negative(Height = Height)
    check.check_not_negative(Height = Height_min)
    check.check_not_negative(Height = Height_max)
    check.check_max_min(Height_max, Height_min)    
    return (Height - Height_min) / (Height_max - Height_min)

def Area_Water(
    Height : float,
    Height_min : float,
    Height_max : float,
    Area_max : float,
    a : float,
    p : float
) -> float:

    """
    Description
    -----------
    Convert height of water in reservoir in m to Area of water in m^2.
    **Reference**: Based on Equation Vecchia, A.V., 2002
    Parameters
    ----------
    Height : float
        height in m
    Height_max : float
        maximum height in m
    Area_max : float
        Area in m^2 is maximum af Area of water in reservoir = Height_max * Area
    Height_Standard : float
        Height_Standard in m
    a : float
    p: float
        a and p are adjustable parameters
        a>0 and p>1
    

    Returns
    -------
    Area of water : float
        Area of surface water in m^2
    """
    check.check_Value_a(a)
    check.check_Value_p(p)
    Height_S = Height_Standard(Height, Height_min, Height_max)
    
    return Area_max * (a * Height_S + 0.5 * (1 - a)(1 - math.cos(math.pi * Height_S))) ** (p - 1) * (1 + ((1 - a) / 2 * a)* pi * math.sin(pi * Height_S)) 


def Volume_Water(
    Height : float,
    Height_min : float,
    Height_max : float,
    Area_max : float,
    a : float,
    p : float
) -> float:
    
    """
    Description
    -----------
    Convert height of water in reservoir in m to Area of water in m^2.
    **Reference**: Based on Equation Vecchia, A.V., 2002 .
    Parameters
    ----------
    Height_min : float
        minimum height in m
    Height_max : float
        maximum height in m
    Area_max : float
        Area in m^2 is maximum af Area of water in reservoir = Height_max * Area
    Height_Standard : float
        Height_Standard in m
    a : float
    p: float
        a and p are adjustable parameters
        a>0 and p>1
    

    Returns
    -------
    Area of water : float
        Area of surface water in m^2
    """
    check.check_Value_p(p)
    check.check_Value_a(a)

    Height_S = Height_Standard(Height,Height_min,Height_max)

    Volume_Water = (Area_max *(Height_max - Height_min) / (p * a)) * (a * Height_S + 0.5 * (1 - a) * (1 - math.cos(math.pi * Height_S))) ** p

    return   Volume_Water

def Volume_precipitation(
    Precipitation : float,
    Area_water : float
) -> float:
    """
    Description
    -----------
    Estimate rainfall volume that rain on the reservoir in m^3.
    **Reference**: Based on Equation Nouvelot, J.F. (1993) 
    Parameters
    ----------
    precipitation : float
        rainfall on reservoir in m
    Area : float
        Area of surface water in reservoir
    """
    
    return Precipitation * Area_water
