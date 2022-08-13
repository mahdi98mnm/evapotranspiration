class Check():

    """
    Check class input parameters CalculationDeepPerculatoin
    """
        
    def soilWater(
        Soil_Water: float
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
        if Soil_Water >= 0:
            Soil_Water = Soil_Water
        else:
            raise TypeError("You can not enter a negative value")

        return Soil_Water

    def feildCapacity(
        Feild_Capacity: float
    ) -> float:

        """
        Check the field capacity of the third layer of soil that is between 0 and 100 percent
        
        Input:

            Feild_Capacity: Field capacity of the third layer of soil (% valume)
        """

        if 0 <= Feild_Capacity <= 100:
            Feild_Capacity = Feild_Capacity
        else:
            raise TypeError("The value entered must be between 0 and 100%")
            
        return Feild_Capacity    

    def geologyPermeability(
        Geology_Permeability: float
    ) -> float:

        """
        Check the Geology Permeability between 0 and 1

        Input

            Geology_Permeability: Permeability coefficient which is a number between 0 and 1
        """

        if 0 <= Geology_Permeability <= 1:
            Geology_Permeability = Geology_Permeability
        else:
            raise TypeError("The value entered must be between 0 and 1")

        return Geology_Permeability

    def depthSoil(
        Depth_Soil: float
    ) -> float:

        """
        Check the depth of the third soil layer that is greater than 0

        Input
            Depth_Soil:  Depth of third layer soil (cm)
        """

        if Depth_Soil >= 0:
            Depth_Soil = Depth_Soil
        else:
            raise TypeError("You can not enter a negative value")

        return Depth_Soil