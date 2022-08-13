
"""
internal Validation Function.
copyright:2022 by sakineh amiri.

"""           
        
def check_precipitation (
        precipitation_value:float 
        ):
    if precipitation_value < 0 :
        raise ValueError(f'value of  precipitation must be  postive : { precipitation_value}')
            
            