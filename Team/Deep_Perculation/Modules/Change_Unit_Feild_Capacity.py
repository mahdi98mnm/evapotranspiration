from Modules.Check import *

class Convert():

    """
    Unit conversion class of required parameters
    """ 

    def changeUnitFeildCapacity(
        feildCapacity: float,
        depthSoil: float
    ) -> float:

        """
        Input:

            Feild_Capacity: Field capacity of the third layer of soil (% valume)
            DepthSoil: Depth of third layer soil (cm)

        Output: 

        Feild_Capacity: Field capacity of the third layer of soil (mm) 
        """
        
        Check.feildCapacity(feildCapacity)
        Check.depthSoil(depthSoil)

        feildCapacity = (feildCapacity / 100) * depthSoil * 10

        return feildCapacity