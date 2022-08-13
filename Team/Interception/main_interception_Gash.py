"""
library of functions for estimating intrception Gush method
copyright:2022/5/6 by sakineh amiri

"""

#from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import math
from  errors_interception_Gash import(
    check_Evaporation_to_Rainfall_Ratio,
    check_precipitation
    )

def saturated_precipitation (
        canopy_storage_capacity : float,
        canopy_cover : float,
        Evaporation_to_Rainfall_Ratio: float)-> float:
    """
    Description
    -------------------------
    calculate interception by Gash mathod , saturated_precipitation
    **reference**based on researches of Gash(1995):
    SWB Version 2.0—A ,page :27 & 28 ,
    A Modified Gash Model for Estimating Rainfall Interception
    Loss of Forest Using Remote Sensing Observations at
    Regional Scale_ Yaokui Cui  and Li Jia _2014
    -------------------------
    type input :
       canopy_storage_capacity : float
       canopy_cover : float 
       Evaporation_to_Rainfall_Ratio : float 
    type output :
      saturated_precipitation : float
    ------------------------
    unit:
       canopy_storage_capacity :  inch & constant
       canopy_cover :   dimentionless
       Evaporation_to_Rainfall_Ratio :  dimentionless
       saturated_precipitation :  inch    

    """    
    check_Evaporation_to_Rainfall_Ratio(Evaporation_to_Rainfall_Ratio)
    saturated_precipitation = -(canopy_storage_capacity/\
    (canopy_cover * Evaporation_to_Rainfall_Ratio))* math.log(1-Evaporation_to_Rainfall_Ratio)
    
    return(saturated_precipitation)



def ratio_of_trunk_Storage_Capacity_to_stem_flow (
        trunk_Storage_Capacity : float,
        stem_flow :float
        )->float :
    """
    Description
    -------------------------
    calculate interception by Gash mathod , ratio_of_trunk_Storage_Capacity_to_stem_flow
    **reference**based on researches of Gash(1995):
    SWB Version 2.0—A ,page :27 & 28 ,
    A Modified Gash Model for Estimating Rainfall Interception
    Loss of Forest Using Remote Sensing Observations at
    Regional Scale_ Yaokui Cui  and Li Jia _2014
    parameters
    -------------------------
    type input :
       trunk_Storage_Capacity : float
       stem_flow : float  
    type output :
       ratio_of_trunk_Storage_Capacity_to_stem_flow: float
    ------------------------
    unit:
       trunk_Storage_Capacity : Constant value [l]:inch
       stem_flow :  dimentionless
       ratio_of_trunk_Storage_Capacity_to_stem_flow : inch   

    """
    ratio_of_trunk_Storage_Capacity_to_stem_flow = trunk_Storage_Capacity/stem_flow
    return(ratio_of_trunk_Storage_Capacity_to_stem_flow)



def interception_Gash_model(
        total_precipitation_of_day : float,
        canopy_storage_capacity : float,
        canopy_cover : float,
        Evaporation_to_Rainfall_Ratio: float,
        ratio_of_trunk_Storage_Capacity_to_stem_flow :float,
        trunk_Storage_Capacity : float,
        stem_flow: float)-> float:
    sp = saturated_precipitation (
            canopy_storage_capacity = canopy_storage_capacity,
            canopy_cover = canopy_cover,
            Evaporation_to_Rainfall_Ratio = Evaporation_to_Rainfall_Ratio)
    """
    Description
    -------------------------
    calculate interception by Gash mathod 
    **reference**based on researches of Gash(1995):
    SWB Version 2.0—A ,page :27 & 28 ,
    A Modified Gash Model for Estimating Rainfall Interception
    Loss of Forest Using Remote Sensing Observations at
    Regional Scale_ Yaokui Cui  and Li Jia _2014
    parameters
    -------------------------
    type input :
        total_precipitation_of_day :float
        saturated_precipitation : float
        ratio_of_trunk_Storage_Capacity_to_stem_flow : float
        canopy_cover : float
        Evaporation_to_Rainfall_Ratio : float
        trunk_Storage_Capacity : float 
    type output :
       interception : float
    ------------------------
    unit:
       total_precipitation_of_day : inch
        saturated_precipitation : inch
        ratio_of_trunk_Storage_Capacity_to_stem_flow : constant value
        canopy_cover :  dimentionless
        Evaporation_to_Rainfall_Ratio : dimentionless
        trunk_Storage_Capacity : constant value 
        interception : inch

    """    
    
    check_precipitation( total_precipitation_of_day)
    check_Evaporation_to_Rainfall_Ratio(Evaporation_to_Rainfall_Ratio)
    
    if total_precipitation_of_day < sp :
         interception= canopy_cover * total_precipitation_of_day
    elif ( total_precipitation_of_day >= sp 
    and 
    total_precipitation_of_day <= ratio_of_trunk_Storage_Capacity_to_stem_flow):
        interception= canopy_cover * sp +\
        canopy_cover * Evaporation_to_Rainfall_Ratio * \
        (total_precipitation_of_day - sp) + stem_flow * total_precipitation_of_day
    elif (total_precipitation_of_day >= sp 
    and 
    total_precipitation_of_day > ratio_of_trunk_Storage_Capacity_to_stem_flow):
        interception= canopy_cover * sp +\
        canopy_cover * Evaporation_to_Rainfall_Ratio *\
        (total_precipitation_of_day - sp) + trunk_Storage_Capacity
    return(interception)

   

