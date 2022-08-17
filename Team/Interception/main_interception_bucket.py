"""
library of functions for estimating intrception Bucket method
copyright:2022 by sakineh amiri

"""
from errors_interception_bucket import check_precipitation
    

def interception_bucket_method(
     type_of_basin_canopy : str,
     precipitation_value : float,
     season : bool
)-> float :
   
     """
     Description
     -----------
     calculate interception from precipitation value and type of basin canopy
     **reference**based on researches of alizade (1391) & fasihi payan name

     parameters
     -----------
     type input :
     basin canopy : str
     precipitation : float
     season : bool
     type output :
     interception : float
     -----------
     inputs are limited :
     type of basin canopy : ['Forest' , 'mixed' , 'Evergreen forest']
     precipitation : zero or postive value
     season = ['growing' , 'none growing']
     ------------
     unit:
     unit of precipitation and interception are the same.
     -----------------
     season = True = growing
     season = False = none growing

     """  
  
     check_precipitation(precipitation_value)
 

     if (type_of_basin_canopy == 'Forest & mixed') and (season == True)  :
          interception = 0.06 * precipitation_value
        
     elif (type_of_basin_canopy == 'Forest & mixed') and (season == False) :
          interception = 0.03 * precipitation_value
          
     elif type_of_basin_canopy == 'Evergreen forest' :
          interception = 0.1 * precipitation_value
          
     else :
          interception = 0
                    
          
     return(interception)

 


