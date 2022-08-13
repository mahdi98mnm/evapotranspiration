from Module.Check import *

class Convert():

    """
    Unit conversion class of required parameters
    """
    
    def changeUnitFeildCapacity(
        Feild_Capacity: float,
        Depth_Soil: float
    ) -> float:

        """
        Input:

            Feild_Capacity: Field capacity of the third layer of soil (% valume)
            DepthSoil: Depth of third layer soil (cm)

        Output: 

        Feild_Capacity: Field capacity of the third layer of soil (mm) 
        """
        Feild_Capacity = Check.feildCapacity(Feild_Capacity)
        Depth_Soil = Check.depthSoil(Depth_Soil)
        
        FeildCapacity = (Feild_Capacity / 100) * Depth_Soil * 10

        return FeildCapacity