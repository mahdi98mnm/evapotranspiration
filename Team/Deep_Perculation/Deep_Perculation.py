from Modules.Change_Unit_Feild_Capacity import *
from Modules.Check import *

class CalculationDeepPerculatoin():

    """
    Calculation Deep Perculation By Class CalculationDeepPerculatoin

    Input:

        Soil_Water: Moisture of the third layer of soil (mm)
        Feild_Capacity: Field capacity of the third layer of soil (% valume)
        Geology_Permeability: Permeability coefficient which is a number between 0 and 1
        Depth_Soil:  Depth of third layer soil (cm)
    """
    
    def __init__(
        self,
        soilWater: float,
        feildCapacity: float,
        geologyPermeability: float,
        depthSoil: float
    ):

        self.soilWater = soilWater
        self.feildCapacity = feildCapacity
        self.geologyPermeability = geologyPermeability
        self.depthSoil = depthSoil

        Check.soilWater(self.soilWater)
        Check.feildCapacity(self.feildCapacity)
        Check.geologyPermeability(self.geologyPermeability)
        Check.depthSoil(self.depthSoil)

    def calculationDeepPerculation(
        self,
    ) -> float:

        """
        Claculation Deep Perculation (mm) By comparing the moisture of layer 3 of 
        the soil with its field capacity (%) and if the moisture (mm/day) of layer 3 is greater 
        than its field capacity, the amount of deep penetration will be equal to its difference.

        Deep_Perculation0 = Soil_Water - Feild_Capacity_Corrected
        
        Input:

            Soil_Water :  Moisture of the third layer of soil (mm)
            Feild_Capacity : Field capacity of the third layer of soil (% valume)
            Depth_Soil : Depth of third layer soil (cm)

        Output:

            return 1: Soil_Water:  Moisture of the third layer of soil (mm)
            return 2: Deep_Perculation0 : Deep penetration of the third layer of soil (mm)
        """
        
        FeildCapacityCorrected = Convert.changeUnitFeildCapacity(
            self.feildCapacity,
            self.depthSoil
        )
        
        if self.soilWater >= FeildCapacityCorrected:

            DeepPerculation0 = self.soilWater - FeildCapacityCorrected
            SoilWater = FeildCapacityCorrected

        else:

            DeepPerculation0 = 0
            SoilWater = self.soilWater


        return DeepPerculation0, SoilWater


    def correctionDeepPerculation(
        self,        
    ) -> float:

        """
        Deep penetration (mm) correction is calculated using a
        deep penetration coefficient with a value between 0 and 1,
        which is considered to be 0.1 for the mountains and 1 for the plains.

        Deep_Perculation = Deep_Perculation0 * (1 - Geology_Permeability)

        Input:

            Deep_Perculation0: Unmodified deep penetration (mm)
            Geology_Permeability: Permeability coefficient which is a number between 0 and 1

        Output:

            Deep penetration: Modified deep penetration (mm)
        """

        ValueDeepPerculation = self.calculationDeepPerculation()

        DeepPerculation = ValueDeepPerculation[0] * (1 - self.geologyPermeability)

        return DeepPerculation

    def calculationLateRunoff(
        self,
    ) -> float:

        """
        Delayed runoff (mm) calculation using depth penetration (mm) calculated
        from the function calculationdeepperculation based on depth permeability coefficient

        LaterRunoff = Deep_Perculation0 * Geology_Permeability

        Input:

            Deep_Perculation0: Unmodified deep penetration (mm)
            Geology_Permeability: Permeability coefficient which is a number between 0 and 1
            
        Output:

           LaterRunoff: Ronab is late (mm)
        """

        ValueDeepPerculation = self.calculationDeepPerculation()

        LaterRunoff = ValueDeepPerculation[0] * self.geologyPermeability

        return LaterRunoff