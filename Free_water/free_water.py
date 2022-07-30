import Mean_Temperature_max_min
import Solar_or_shortwave_radiation
import Slope_Vapour_Pressure_Curve_With_Maen_Temperature as slope
import Wind_speed_at_2m_above_ground_surface
import Saturation_Vapour_Pressure_With_Temperature
import Actual_Vapour_Pressure

class E_free_water : 

     # init method or constructor 
    def __init__(self,
        method_free_water_based_on_radiation : str = None,
        method_ws_and_vp : str = None,
        T_max : float = None,
        T_min : float = None,
        T_mean : float = None,
        delta : float = None,
        stddate : str = None,
        degree : float = None,
        minute : float = None,
        second : float = None,
        Actual_duration_of_sunshine_in_a_day : float = None,
        Monthly_average_sunshine_duration : float = None,
        mode_data : float = None,
        Adjustment_coefficient_or_K_RS : float = None,
        R_S : float = None,
        method_Solar_or_shortwave_radiation : str = None,
        latent_heat_of_vaporization : float = None,
        water_area_of_a_lake_or_reservoir : float = None,
        wind_speed_at_2m : float = None,
        e_s : float = None,
        e_a : float = None,
        Altitude_at_which_wind_speed_is_measured : float = None, 
        Measured_wind_speed : float = None,
        method_Actual_Vapour_Pressure : str = None,
        T_dew : float  = None,
        RH_max : float  = None,
        RH_min : float  = None,
        RH_mean : float  = None,
        T_wet : float  = None,
        T_dry : float  = None,
        a_psy : float  = None,
        Altitude : float = None
    ):
        self.method_free_water_based_on_radiation = method_free_water_based_on_radiation
        self.method_ws_and_vp = method_ws_and_vp
        self.T_max = T_max
        self.T_min = T_min
        self.T_mean= T_mean
        self.delta = delta
        self.stddate= stddate
        self.degree= degree
        self.minute=minute
        self.second = second
        self.Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day
        self.Monthly_average_sunshine_duration = Monthly_average_sunshine_duration
        self.mode_data = mode_data
        self.Adjustment_coefficient_or_K_RS = Adjustment_coefficient_or_K_RS
        self.R_S = R_S
        self.method_Solar_or_shortwave_radiation = method_Solar_or_shortwave_radiation
        self.latent_heat_of_vaporization = latent_heat_of_vaporization
        self.water_area_of_a_lake_or_reservoir = water_area_of_a_lake_or_reservoir
        self.wind_speed_at_2m = wind_speed_at_2m
        self.e_s = e_s
        self.e_a = e_a
        self.Altitude_at_which_wind_speed_is_measured = Altitude_at_which_wind_speed_is_measured
        self.Measured_wind_speed = Measured_wind_speed
        self.method_Actual_Vapour_Pressure = method_Actual_Vapour_Pressure
        self.T_dew = T_dew
        self.RH_max = RH_max
        self.RH_min = RH_min
        self.RH_mean = RH_mean
        self.T_wet = T_wet
        self.T_dry = T_dry
        self.a_psy = a_psy
        self.Altitude = Altitude
   
    # Sample Method 
    def based_on_radiation(
        method_free_water_based_on_radiation : str,
        T_max : float = None,
        T_min : float = None,
        T_mean : float = None,
        stddate : str = None,
        degree : float = None,
        minute : float = None,
        second : float = None,
        Actual_duration_of_sunshine_in_a_day : float = None,
        Monthly_average_sunshine_duration : float = None,
        mode_data : float = None,
        Adjustment_coefficient_or_K_RS : float = None,
        R_S : float = None,
        method_Solar_or_shortwave_radiation : str = None
    )-> float:
    
        """
        Description
        -----------
        calculate Actual Vapour Pressure With Dewpoint temperature - eq 14 FAO56
        ----------
        Dewpoint temperature : float
            Dewpoint temperature in celsius

        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """
        if T_mean is None:
            T_mean = Mean_Temperature_max_min.mean_temperature_max_min(
                T_max = T_max,
                T_min = T_max
            )
        else:
            T_mean = T_mean

        if R_S is None:
            if method_Solar_or_shortwave_radiation == 'Angstrom':
                R_S = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Angstrom(
                    stddate = stddate,
                    degree = degree, 
                    minute = minute,
                    second = second,
                    mode_data = mode_data,
                    Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day,
                    Monthly_average_sunshine_duration = Monthly_average_sunshine_duration
                )


            elif method_Solar_or_shortwave_radiation == 'Hargreaves':
                R_S = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Hargreaves(
                    stddate = stddate,
                    degree = degree,
                    minute = minute,
                    second = second,
                    T_max = T_max,
                    T_min = T_min,
                    Adjustment_coefficient_or_K_RS = Adjustment_coefficient_or_K_RS
                )
        else:
            R_S = R_S
        
        if method_free_water_based_on_radiation == 'Jensen':
            E = 0.03523 * R_S * ((0.014 * T_mean) - 0.37) 
        elif method_free_water_based_on_radiation == 'Stuart':
            E = 0.03495 * R_S * ((0.0082 * T_mean) - 0.19)

        return E


    def making(
        T_max : float = None,
        T_min : float = None,
        T_mean : float = None,
        delta : float = None,
        stddate : str = None,
        degree : float = None,
        minute : float = None,
        second : float = None,
        Actual_duration_of_sunshine_in_a_day : float = None,
        Monthly_average_sunshine_duration : float = None,
        mode_data : float = None,
        Adjustment_coefficient_or_K_RS : float = None,
        R_S : float = None,
        method_Solar_or_shortwave_radiation : str = None,
        latent_heat_of_vaporization : float = None
    )-> float:
    
        """
        Description
        -----------
        calculate Actual Vapour Pressure With Dewpoint temperature - eq 14 FAO56
        ----------
        Dewpoint temperature : float
            Dewpoint temperature in celsius

        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """
        if T_mean is None:
            T_mean = Mean_Temperature_max_min.mean_temperature_max_min(
                T_max = T_max,
                T_min = T_max
            )
        else:
            T_mean = T_mean

        if R_S is None:
            if method_Solar_or_shortwave_radiation == 'Angstrom':
                R_S = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Angstrom(
                    stddate = stddate,
                    degree = degree, 
                    minute = minute,
                    second = second,
                    mode_data = mode_data,
                    Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day,
                    Monthly_average_sunshine_duration = Monthly_average_sunshine_duration
                )


            elif method_Solar_or_shortwave_radiation == 'Hargreaves':
                R_S = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Hargreaves(
                    stddate = stddate,
                    degree = degree,
                    minute = minute,
                    second = second,
                    T_max = T_max,
                    T_min = T_min,
                    Adjustment_coefficient_or_K_RS = Adjustment_coefficient_or_K_RS
                )
        else:
            R_S = R_S
        
        if delta is None:
            delta = slope.slope_vapour_pressure_curve_with_maen_temperature(
                T_mean = T_mean
            )
        else:
            delta = delta
        
        return 52.6 * (delta / (delta + latent_heat_of_vaporization)) * (R_S / latent_heat_of_vaporization) - 0.12 


    def based_on_wind_speed_and_vapor_pressure(
        method_ws_and_vp : str,
        water_area_of_a_lake_or_reservoir : float,
        wind_speed_at_2m : float = None,
        e_s : float = None,
        e_a : float = None,
        Altitude_at_which_wind_speed_is_measured : float = None, 
        Measured_wind_speed : float = None,
        T_max : float = None,
        T_min : float = None,
        method_Actual_Vapour_Pressure : str = None,
        T_dew : float  = None,
        T_mean : float  = None,
        RH_max : float  = None,
        RH_min : float  = None,
        RH_mean : float  = None,
        T_wet : float  = None,
        T_dry : float  = None,
        a_psy : float  = None,
        Altitude : float = None
    )-> float:
    
        """
        Description
        -----------
        calculate Actual Vapour Pressure With Dewpoint temperature - eq 14 FAO56
        ----------
        Dewpoint temperature : float
            Dewpoint temperature in celsius

        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """
        if e_s is None :
            e_s = total_saturation_vapour_pressure(
                T_max = T_max,
                T_min = T_min
            )
        else:
            e_s = e_s
        

        if e_a is None :
            if method_Actual_Vapour_Pressure == 'dew':
                e_a = Actual_Vapour_Pressure.Actual_Vapour_Pressure.dew(
                    T_dew = T_dew
                )

            elif method_Actual_Vapour_Pressure == 'RH_and_T_max_min':
                e_a = Actual_Vapour_Pressure.Actual_Vapour_Pressure.RH_and_T_max_min(
                    T_max = T_max,
                    T_min = T_min,
                    RH_max = RH_max,
                    RH_min = RH_min
                )

            elif method_Actual_Vapour_Pressure == 'RH_max_and_T_min':
                e_a = Actual_Vapour_Pressure.Actual_Vapour_Pressure.RH_max_and_T_min(
                    T_min = T_min,
                    RH_max = RH_max
                )

            elif method_Actual_Vapour_Pressure == 'RH_mean_T_max_min':
                e_a = Actual_Vapour_Pressure.Actual_Vapour_Pressure.RH_mean_T_max_min(
                    T_max =T_max,
                    T_min = T_min,
                    RH_max = RH_max,
                    RH_min = RH_min,
                    RH_mean = RH_mean
                )

            elif method_Actual_Vapour_Pressure == 'T_wet_T_dry':
                e_a = Actual_Vapour_Pressure.Actual_Vapour_Pressure.T_wet_T_dry(
                    T_wet = T_wet,
                    T_dry = T_dry,
                    a_psy = a_psy,
                    Altitude = Altitude
                )
            else:
                e_a = e_a

        e_s_minus_e_a = e_s - e_a

        if wind_speed_at_2m is None : 
            wind_speed_at_2m = Wind_speed_at_2m_above_ground_surface.wind_speed_at_2m_above_ground_surface(
                Altitude_at_which_wind_speed_is_measured = Altitude_at_which_wind_speed_is_measured, 
                Measured_wind_speed = Measured_wind_speed
            )
        else:
            wind_speed_at_2m = wind_speed_at_2m
        
        if method_ws_and_vp == 'Harbeck' :
            E = 2.909 * (water_area_of_a_lake_or_reservoir**(-0.05)) * wind_speed_at_2m * e_s_minus_e_a
        elif method_ws_and_vp == 'Shuttleworth' :
            E = 3.623 * (water_area_of_a_lake_or_reservoir**(-0.066)) * wind_speed_at_2m * e_s_minus_e_a
        

        return E





