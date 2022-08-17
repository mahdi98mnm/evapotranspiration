from Modules.Check import *


class GroundWaterBalance:

    """
    Calculation Ground Water Blance By Class GroundWaterBalance

    Input:

    DP: Deep perculation caused by rain
    G_i: Entrance to Ground water
    G_o: Exit from underground water
    E_upw: Evaporation from groundwater
    DP_fws: Penetration from the free surface of water
    DP_alv: Penetration in the alluvial cone
    DP_art: Infiltration by artificial feeding projects
    R_dm: The rate of water leakage from underground water to surface water
    Sigma_dis: Total withdrawals from underground water including springs, aqueducts and wells
    R_fg:
    W_g:
    d_Gw: Groundwater depth
    Q_springs_i: The discharge of the spring in time i
    Q_springs_i1: The discharge of the spring in time i+1

    Output:

    delta_Sg: Groundwater changes
    """

    def __init__(
        self,
        DP: float,
        G_i: float,
        G_o: float,
        E_upw: float,
        DP_fws: float,
        DP_alv: float,
        DP_art: float,
        R_dm: float,
        springs: float,
        aqueducts: float,
        wells: float,
        R_fg: float,
        W_g: float,
        d_Gw: float,
        Q_springs_i: float,
        Q_springs_i1: float
    ):

        self.DP = DP
        self.G_i = G_i
        self.G_o = G_o
        self.E_upw = E_upw
        self.DP_fws = DP_fws
        self.DP_alv = DP_alv
        self.DP_art = DP_art
        self.R_dm = R_dm
        self.springs = springs
        self.aqueducts = aqueducts
        self.wells = wells
        self.R_fg = R_fg
        self.W_g = W_g
        self.d_Gw = d_Gw
        self.Q_springs_i = Q_springs_i
        self.Q_springs_i1 = Q_springs_i1

        Check.DeepPerculation(self.DP)
        Check.EntranceGroundWater(self.G_i)
        Check.ExitGroundWater(self.G_o)
        Check.EvaporationGroundWater(self.E_upw)
        Check.PenetrationFreeSurfaceWater(self.DP_fws)
        Check.PenetrationAlluvialCone(self.DP_alv)
        Check.InfiltrationArtificialFeedingProjects(self.DP_art)
        Check.RateWaterLeakageGroundWaterSurfaceWater(self.R_dm)
        Check.WithdrawalSprings(self.springs)
        Check.Withdrawalaqueducts(self.aqueducts)
        Check.WithdrawalWells(self.wells)
        Check.FunctionR_fg(self.R_fg)
        Check.FunctionW_g(self.W_g)
        Check.Groundwaterdepth(self.d_Gw)
        Check.DischargeSpringTimei(self.Q_springs_i)
        Check.DischargeSpringTimei1(self.Q_springs_i1)

    def ClaculationEvaporationGroundwater(
        self,
    ) -> float:
        """
        If the depth of the underground water is less than 5 meters, the volume
        of evaporation from the underground water is calculated, otherwise,
        the evaporation from the underground water is 0.
        """

        if self.d_Gw > 5:

            E_upw = self.E_upw

        else:

            E_upw = 0

        return E_upw

    def CheckDubaisprings(
        self,
        # Volume_i,
        # Volume_i1,
    ) -> bool:
        """
        If the flow rate of the spring at time i is higher than
        at time i+1, it means that the underground water tank has been
        fed and the volume of the underground water tank has increased  return True and conversely return False.

        Input:

        Q_springs_i: The discharge of the spring in time i
        Q_springs_i1: The discharge of the spring in time i+1

        Output:

        Volume_i: The volume of underground water in time i
        Volume_i1: The volume of underground water in time i+1
        """

        if self.Q_springs_i1 > self.Q_springs_i:

            # Volume_i1 > Volume_i
            return True

        else:

            # Volume_i1 < Volume_i
            return False

    def ClaculationGroundWaterBalance(
        self,
    ):

        delta_Sg = (self.DP + (self.G_i - self.G_o) + self.R_fg - self.W_g -
                    self.ClaculationEvaporationGroundwater +
                    self.DP_fws + self.DP_alv + self.DP_art
                    - self.R_dm - (self.springs + self.wells + self.aqueducts))

        return delta_Sg
