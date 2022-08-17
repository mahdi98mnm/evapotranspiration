class Check():

    """
    Check class input parameters CalculationGroundWaterBalance
    """

    def DeepPerculation(
        DP: float
    ) -> float:

        """
        Investigating the depth penetration caused by rain that is greater than 0.

        Input:

            DP: Deep perculation caused by rain (m^3)
        """

        if DP >= 0:
            DP = DP
        else:
            raise ValueError("You can not enter a negative value")

    def EntranceGroundWater(
        G_i: float
    ) -> float:

        """
        Checking the input from the underground water, which should be greater than 0.

        Input:

            G_i: Entrance to Ground water (m^3)
        """

        if G_i >= 0:
            G_i = G_i
        else:
            raise ValueError("You can not enter a negative value")

    def ExitGroundWater(
        G_o: float
    ) -> float:

        """
         Checking the output of underground water, which should be greater than 0.

        Input:

            G_o: Exit from underground water (m^3)
        """

        if G_o >= 0:
            G_o = G_o
        else:
            raise ValueError("You can not enter a negative value")

    def EvaporationGroundWater(
        E_upw: float
    ) -> float:

        """
        Investigation of evaporation from underground water, which should be greater than 0.

        Input:

            E_upw: Evaporation from groundwater (m^3)
        """

        if E_upw >= 0:
            E_upw = E_upw
        else:
            raise ValueError("You can not enter a negative value")

    def PenetrationFreeSurfaceWater(
        DP_fws: float
    ) -> float:

        """
        Investigating penetration from the free surface of water, which must be greater than 0.

        Input:

            DP_fws: Penetration from the free surface of water (m^3)
        """

        if DP_fws >= 0:
            DP_fws = DP_fws
        else:
            raise ValueError("You can not enter a negative value")
        
    def PenetrationAlluvialCone(
        DP_alv: float
    ) -> float:

        """
        Investigation of evaporation from underground water, which should be greater than 0.

        Input:

            DP_alv: Penetration in the alluvial cone (m^3)
        """

        if DP_alv >= 0:
            DP_alv = DP_alv
        else:
            raise ValueError("You can not enter a negative value")
    
    def InfiltrationArtificialFeedingProjects(
        DP_art: float
    ) -> float:

        """
        Investigating infiltration by artificial feeding projects should be greater than 0.

        Input
        
            DP_art: Infiltration by artificial feeding projects (m^3)
        """

        if DP_art >= 0:
            DP_art = DP_art
        else:
            raise ValueError("You can not enter a negative value")
    
    def RateWaterLeakageGroundWaterSurfaceWater(
        R_dm: float
    ) -> float:

        """
        Checking the amount of water leakage from underground water
        to surface water, which should be greater than 0.

        Input:

            R_dm: The rate of water leakage from underground water to surface water (m^3)
        """

        if R_dm >= 0:
            R_dm = R_dm
        else:
            raise ValueError("You can not enter a negative value")

    def WithdrawalSprings(
        springs: float
    ) -> float:

        """
        Checking the withdrawal from springs, which should be greater than 0.

        Input:

            springs: withdrawal from springs (m^3)
        """

        if springs >= 0:
            springs = springs
        else:
            raise ValueError("You can not enter a negative value")

    def Withdrawalaqueducts(
        aqueducts: float
    ) -> float:

        """
        Checking the withdrawal from the aqueducts, which must be greater than 0.

        Input:

            aqueducts: Evaporation from groundwater (m^3)
        """

        if aqueducts >= 0:
            aqueducts = aqueducts
        else:
            raise ValueError("You can not enter a negative value")

    def WithdrawalWells(
        wells: float
    ) -> float:

        """
        Checking the withdrawal from the wells, which should be greater than 0.

        Input:

            wells: Evaporation from groundwater (m^3)
        """

        if wells >= 0:
            wells = wells
        else:
            raise ValueError("You can not enter a negative value")

    def FunctionR_fg(
        R_fg: float
    ) -> float:
    
        """
        Check R_fg that must be greater than 0.

        Input
            R_fg: (m^3)
        """

        if R_fg >= 0:
            R_fg = R_fg
        else:
            raise ValueError("You can not enter a negative value")

    def FunctionW_g(
        W_g: float
    ) -> float:
    
        """
        Check W_g that must be greater than 0.

        Input
            W_g: (m^3)
        """

        if W_g >= 0:
            W_g = W_g
        else:
            raise ValueError("You can not enter a negative value")

    def Groundwaterdepth(
        d_Gw: float
    ) -> float:
    
        """
        Checking the depth of underground water, which should be greater than 0.

        Input
            d_Gw: Groundwater depth (m)
        """

        if d_Gw >= 0:
            d_Gw = d_Gw
        else:
            raise ValueError("You can not enter a negative value")

    def DischargeSpringTimei (
        Q_springs_i: float
    ) -> float:
    
        """
        Checking the discharge from the spring at time i, which must be greater than 0.

        Input
            Q_springs_i: The discharge of the spring in time i (m^3/s)
        """

        if Q_springs_i >= 0:
            Q_springs_i = Q_springs_i
        else:
            raise ValueError("You can not enter a negative value")

    def DischargeSpringTimei1(
        Q_springs_i1: float
    ) -> float:
    
        """
        Checking the discharge from the spring at time i+1, which must be greater than 0.

        Input
            Q_springs_i1: The discharge of the spring in time i+1 (m^3/s)
        """

        if Q_springs_i1 >= 0:
            Q_springs_i1 = Q_springs_i1
        else:
            raise ValueError("You can not enter a negative value")