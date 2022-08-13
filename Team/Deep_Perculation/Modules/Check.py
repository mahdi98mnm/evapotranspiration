class Check():

    """
    Check class input parameters CalculationDeepPerculatoin
    """
        
    def soilWater(
        soilWater: float
    ) -> float:

        """
        Check the moisture content of the soil toxin layer that is greater than 0

        Input:

            Soil_Water: Moisture of the third layer of soil (mm)
        """

        # try:
        #     if Soil_Water >= 0:
        #         Soil_Water = Soil_Water
        # except TypeError:
        #     "You can not enter a negative number"
        if soilWater >= 0:
            soilWater = soilWater
        else:
            raise ValueError("You can not enter a negative value")

    def feildCapacity(
        feildCapacity: float
    ) -> float:

        """
        Check the field capacity of the third layer of soil that is between 0 and 100 percent
        
        Input:

            Feild_Capacity: Field capacity of the third layer of soil (% valume)
        """

        if 0 <= feildCapacity <= 100:
            feildCapacity = feildCapacity
        else:
            raise ValueError("The value entered must be between 0 and 100%")    

    def geologyPermeability(
        geologyPermeability: float
    ) -> float:

        """
        Check the Geology Permeability between 0 and 1

        Input

            Geology_Permeability: Permeability coefficient which is a number between 0 and 1
        """

        if 0 <= geologyPermeability <= 1:
            geologyPermeability = geologyPermeability
        else:
            raise ValueError("The value entered must be between 0 and 1")

    def depthSoil(
        depthSoil: float
    ) -> float:

        """
        Check the depth of the third soil layer that is greater than 0

        Input
            Depth_Soil:  Depth of third layer soil (cm)
        """

        if depthSoil >= 0:
            depthSoil = depthSoil
        else:
            raise ValueError("You can not enter a negative value")