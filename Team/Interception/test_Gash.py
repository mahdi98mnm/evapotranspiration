
"""
library of functions for testing  intrception Gush method
copyright:2022/5/6 by sakineh amiri

"""

from main_interception_Gash import (saturated_precipitation ,
                                     ratio_of_trunk_Storage_Capacity_to_stem_flow,
                                     interception_Gash_model)

#equation 2
Psat2 = saturated_precipitation(canopy_storage_capacity = 0.252,
                                canopy_cover = 0.5,
                                Evaporation_to_Rainfall_Ratio = 0.02)

I2=interception_Gash_model(
      total_precipitation_of_day = 0.4,
      canopy_storage_capacity = 0.252,
      canopy_cover = 0.5,
      Evaporation_to_Rainfall_Ratio = 0.02,
      ratio_of_trunk_Storage_Capacity_to_stem_flow = 0.14,
      trunk_Storage_Capacity = 0.157,
      stem_flow = 1.12
     )

#equation 4
Psat4 = saturated_precipitation(canopy_storage_capacity = 0.252,
                                canopy_cover = 0.5,
                                Evaporation_to_Rainfall_Ratio = 0.02)

kp4= ratio_of_trunk_Storage_Capacity_to_stem_flow(trunk_Storage_Capacity = 0.157,stem_flow =1.12)

I4=interception_Gash_model(
       total_precipitation_of_day = 1.38,
       canopy_storage_capacity = 0.252,
       canopy_cover = 0.5,
       Evaporation_to_Rainfall_Ratio = 0.02 ,
       ratio_of_trunk_Storage_Capacity_to_stem_flow = 0.14,
       trunk_Storage_Capacity = 0.157,
       stem_flow = 1.12,
     )

#equation 3
Psat3 = saturated_precipitation(canopy_storage_capacity = 0.252,
                                canopy_cover = 0.5,
                                Evaporation_to_Rainfall_Ratio = 0.02)

kp3= ratio_of_trunk_Storage_Capacity_to_stem_flow(trunk_Storage_Capacity = 0.24,stem_flow =0.12)

I3=interception_Gash_model(
      total_precipitation_of_day = 1.38,
      canopy_storage_capacity = 0.252,
      canopy_cover = 0.5,
      Evaporation_to_Rainfall_Ratio = 0.02,
      ratio_of_trunk_Storage_Capacity_to_stem_flow = 2,
      trunk_Storage_Capacity = 0.24,
      stem_flow = 0.12,
     )
