


class Soil_heat_flux_density :
   
    # init method or constructor 
    def __init__(
        self,
        Soil_heat_capacity = None,
        Air_temperature_at_previous_step = None,
        Air_temperature_at_current_step = None,
        delta_time = None,
        Effective_soil_depth = None,
        method_Solar_or_shortwave_radiation = None,
        method_Net_longwave_radiation = None,
        Mean_air_temperature_of_current_month = None,
        Mean_air_temperature_of_next_month = None,
        Mean_air_temperature_of_previous_month = None,
        stddate = None,
        degree = None,
        minute = None,
        second = None,
        Altitude = None, 
        method_Actual_Vapour_Pressure = None,
        T_dew = None,
        T_max = None,
        T_min = None,
        T_mean = None,
        RH_max =None,
        RH_min = None,
        RH_mean = None,
        T_wet = None,
        T_dry = None,
        a_psy = None,
        Actual_duration_of_sunshine_in_a_day = None,
        Adjustment_coefficient_or_K_RS = None,
        e_a = None,
        mode = None,
        Monthly_average_sunshine_duration = None,
        mode_data = None
    ):
        
        




        self.Soil_heat_capacity = Soil_heat_capacity
        self.Air_temperature_at_previous_step = Air_temperature_at_previous_step
        self.Air_temperature_at_current_step = Air_temperature_at_current_step
        self.delta_time = delta_time
        self.Effective_soil_depth = Effective_soil_depth
        self.method_Solar_or_shortwave_radiation = method_Solar_or_shortwave_radiation
        self.method_Net_longwave_radiation = method_Net_longwave_radiation
        self.Mean_air_temperature_of_current_month = Mean_air_temperature_of_current_month
        self.Mean_air_temperature_of_next_month = Mean_air_temperature_of_next_month
        self.Mean_air_temperature_of_previous_month = Mean_air_temperature_of_previous_month
        self.stddate = stddate
        self.degree = degree
        self.minute = minute
        self.second = second
        self.Altitude = Altitude
        self.method_Actual_Vapour_Pressure = method_Actual_Vapour_Pressure
        self.T_dew = T_dew
        self.T_max= T_max
        self.T_min = T_min
        self.T_mean = T_mean
        self.RH_max = RH_max
        self.RH_min = RH_min
        self.RH_mean = RH_mean
        self.T_wet = T_wet
        self.T_dry = T_dry
        self.a_psy = a_psy
        self.Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day
        self.Adjustment_coefficient_or_K_RS= Adjustment_coefficient_or_K_RS
        self.e_a = e_a
        self.mode=mode
        self.Monthly_average_sunshine_duration = Monthly_average_sunshine_duration
        self.mode_data = mode_data
        
        # Sample Method 
    def With_Effective_soil_depth (
        Soil_heat_capacity : float,
        Air_temperature_at_previous_step : float,
        Air_temperature_at_current_step : float,
        delta_time : float,
        Effective_soil_depth : float 
    )-> float:


        """
    Description
    -----------
    calculate Soil_heat_flux_density with Effective soil depth - eq 41 FAO56
    ----------
    Soil_heat_capacity : float
        Soil heat capacity in MJ / m**3 / celsius
    Air_temperature_at_previous_step : float 
        Air temperature at previous step in celsius
    Air_temperature_at_current_step : float
        Air temperature at current step in celsius
    delta_time : float
        Length of time interval in day
    Effective_soil_depth : float
        Effective soil depth in meter

    Latitude:
    degree : int
        degree in degree - Positive for the Northern Hemisphere and negative for the Southern Hemisphere
    minute : int
        minute in minute - Positive
    second : int
        second in second - Positive
    stddate : str
        Date with the specified standard
    Altitude : float
        Altitude in meter - station elevation above sea level 
    method_Solar_or_shortwave_radiation : str
        Angstrom or Hargreaves for Solar or shortwave radiation
    method_Actual_Vapour_Pressure : str
        dew or RH_and_T_max_min or RH_max_and_T_min or RH_mean_T_max_min or T_wet_T_dry
    T_dew : float
        Dewpoint temperature in celsius
    RH_max and RH_min : float
        Maximum relative humidity and Minimum relative humidity in percent
    RH_mean : float
        Mean relative humidity in percent
    Maximum Tempreture and Minimum Tempreture : float
        Maximum Tempreture and Minimum Tempreture in celsius
    T_wet : float
        Wet Tempreture in celsius
    T_dry : float
        Dry Tempreture in celsius
    a_psy : float
        Coefficient of psychrometer in celsius**-1
        Coefficient of psychrometer for ventilated (Asmann type) psychrometers movement of some 5 m/s = 0.000662
        Coefficient of psychrometer for natural ventilated psychrometers (about 1 m/s)= 0.0008
        Coefficient of psychrometer for non-ventilated psychrometers installed indoors = 0.0012
    Stefan-Boltzmann constant : float
        Stefan-Boltzmann constant in MJ / K**4 m**2 day
    e_a : float
        Actual Vapour Pressure in kilo pascal
    Actual duration of sunshine in a day : float
        Actual duration of sunshine in a day in hour per day
    Adjustment_coefficient_or_K_RS : float
        Adjustment coefficient in C**-0.5 -- between 0.16 to 0.19
            for interior locations, where land mass dominates and air masses are not strongly
            influenced by a large water body, kRs ≅ 0.16;
            for coastal locations, situated on or adjacent to the coast of a large land mass and where
            air masses are influenced by a nearby water body, kRs ≅ 0.19
        
    Returns
    -------
    Soil_heat_flux_density : float
        Soil heat flux density in MJ / m**2 /day
    """
    
        return Soil_heat_capacity * ((Air_temperature_at_previous_step + Air_temperature_at_current_step) / delta_time ) * Effective_soil_depth


    def For_day_and_ten_day_periods (
    )-> float:
        """
    Description
    -----------
    calculate Soil_heat_flux_density for For day and ten-day periods - eq 43 & 44 FAO56
    ----------

    Returns
    -------
    Soil_heat_flux_density : float
        Soil heat flux density in MJ / m**2 /day
    """

        return 0

    def For_monthly_periods (
        Mean_air_temperature_of_previous_month : float,
        Mean_air_temperature_of_next_month = None,
        Mean_air_temperature_of_current_month = None
    )-> float:


        """
    Description
    -----------
    calculate Soil_heat_flux_density with Effective soil depth - eq 41 FAO56
    ----------
    Mean_air_temperature_of_previous_month : float 
        Mean air temperature of previous month in celsius
    Mean_air_temperature_of_next_month : float
        Mean air temperature of next month in celsius
    Mean_air_temperature_of_current_month : float
        Mean air temperature of current month in celsius
        
    Returns
    -------
    Soil_heat_flux_density : float
        Soil heat flux density in MJ / m**2 /day
    """

        if Mean_air_temperature_of_current_month == None :
            G = 0.07 * (Mean_air_temperature_of_next_month - Mean_air_temperature_of_previous_month)

        elif Mean_air_temperature_of_next_month == None :
            G = 0.14 * (Mean_air_temperature_of_current_month - Mean_air_temperature_of_previous_month)

        return G
    
    def For_hourly_or_shorter_periods(
        method_Solar_or_shortwave_radiation : str,
        method_Net_longwave_radiation : str,
        stddate : str,
        degree : int,
        minute : int,
        second : int,
        mode: str,
        Altitude = None, 
        method_Actual_Vapour_Pressure = None,
        T_dew = None,
        T_max = None,
        T_min = None,
        T_mean = None,
        RH_max =None,
        RH_min = None,
        RH_mean = None,
        T_wet = None,
        T_dry = None,
        a_psy = None,
        Actual_duration_of_sunshine_in_a_day = None,
        Adjustment_coefficient_or_K_RS = None,
        e_a = None,
        Monthly_average_sunshine_duration = None,
        mode_data = None
    )-> float:

        """
        Description
        -----------
        calculate Soil_heat_flux_density with Effective soil depth - eq 45 & 46 FAO56
        ----------
        mode : str 
            night or day
        Latitude:
        degree : int
            degree in degree - Positive for the Northern Hemisphere and negative for the Southern Hemisphere
        minute : int
             minute in minute - Positive
        second : int
            second in second - Positive
        stddate : str
            Date with the specified standard
        Altitude : float
            Altitude in meter - station elevation above sea level 
        method_Net_longwave_radiation : str 
            Without_have_e_a or With_have_e_a for Net longwave radiation
        method_Solar_or_shortwave_radiation : str
            Angstrom or Hargreaves for Solar or shortwave radiation
        Maximum Tempreture and Minimum Tempreture : float
            Maximum Tempreture and Minimum Tempreture in celsius
        e_a : float
            Actual Vapour Pressure in kilo pascal
        Actual duration of sunshine in a day : float
            Actual duration of sunshine in a day in hour per day
        Adjustment_coefficient_or_K_RS : float
            Adjustment coefficient in C**-0.5 -- between 0.16 to 0.19
                for interior locations, where land mass dominates and air masses are not strongly
                influenced by a large water body, kRs ≅ 0.16;
                for coastal locations, situated on or adjacent to the coast of a large land mass and where
                air masses are influenced by a nearby water body, kRs ≅ 0.19
        method_Actual_Vapour_Pressure : str
            dew or RH_and_T_max_min or RH_max_and_T_min or RH_mean_T_max_min or T_wet_T_dry
        T_dew : float
            Dewpoint temperature in celsius
        RH_max and RH_min : float
            Maximum relative humidity and Minimum relative humidity in percent
        RH_mean : float
            Mean relative humidity in percent
        Maximum Tempreture and Minimum Tempreture : float
            Maximum Tempreture and Minimum Tempreture in celsius
        T_wet : float
            Wet Tempreture in celsius
        T_dry : float
            Dry Tempreture in celsius
        a_psy : float
            Coefficient of psychrometer in celsius**-1
            Coefficient of psychrometer for ventilated (Asmann type) psychrometers movement of some 5 m/s = 0.000662
            Coefficient of psychrometer for natural ventilated psychrometers (about 1 m/s)= 0.0008
            Coefficient of psychrometer for non-ventilated psychrometers installed indoors = 0.0012
        T_max : float
            Maximum Temperature in celsius
        T_min : float
            Minimum Temperature in celsius
        T_mean : float 
            Mean Temperature in celsius
                
        Returns
        -------
        Soil_heat_flux_density : float
            Soil heat flux density in MJ / m**2 /day
        """
        if mode == 'day':
            G = 0.1 * Calculate_Net_radiation_at_the_crop_surface(
                method_Net_longwave_radiation,
                method_Solar_or_shortwave_radiation,
                stddate,
                degree,
                minute,
                second ,
                Altitude, 
                method_Actual_Vapour_Pressure ,T_dew ,T_max ,T_min , mode_data,
                T_mean ,RH_max ,RH_min ,RH_mean ,T_wet ,
                T_dry ,a_psy ,Actual_duration_of_sunshine_in_a_day ,Monthly_average_sunshine_duration ,
                Adjustment_coefficient_or_K_RS ,e_a)

        elif mode == 'night':
            G = 0.5 * Calculate_Net_radiation_at_the_crop_surface(
                method_Net_longwave_radiation,
                method_Solar_or_shortwave_radiation,
                stddate,
                degree,
                minute,
                second,
                Altitude, 
                method_Actual_Vapour_Pressure ,T_dew ,T_max ,T_min ,mode_data,
                T_mean, RH_max, RH_min, RH_mean, T_wet,
                T_dry, a_psy, Actual_duration_of_sunshine_in_a_day ,Monthly_average_sunshine_duration,
                Adjustment_coefficient_or_K_RS, e_a )

        return G

# Check_Calculate Soil heat flux density ----- page55 EX13 FAO56
# print(Soil_heat_flux_density.For_monthly_periods(Mean_air_temperature_of_previous_month=14.1 , Mean_air_temperature_of_next_month=18.8))
# print(Soil_heat_flux_density.For_monthly_periods(Mean_air_temperature_of_previous_month=14.1 , Mean_air_temperature_of_current_month=16.1))
