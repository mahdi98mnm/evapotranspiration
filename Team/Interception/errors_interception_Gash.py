"""
internal Validation Function.
copyright:2022 by sakineh amiri.

"""

def check_Evaporation_to_Rainfall_Ratio (
    Evaporation_to_Rainfall_Ratio
):
    
    if not Evaporation_to_Rainfall_Ratio < 1:
        raise ValueError(f'Evaporation_to_Rainfall_Ratio Must be less than one : {Evaporation_to_Rainfall_Ratio}')
"""
Discribtion
in equation of saturated precipitation ;
the value of (1-Evaporation_to_Rainfall_Ratio)
shoud not be nagetive beacause of ln

"""
def check_precipitation (
    total_precipitation_of_day:float 
):
    if total_precipitation_of_day < 0 :
        raise ValueError(f'value of  precipitation must be  postive : { total_precipitation_of_day}')