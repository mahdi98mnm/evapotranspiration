import Mean_Temperature_max_min
import Solar_or_shortwave_radiation
import Slope_Vapour_Pressure_Curve_With_Maen_Temperature as slope

class E_free_water : 

     # init method or constructor 
    def __init__(self,
        method_free_water_based_on_radiation : str = None,
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
    ):
        self.method_free_water_based_on_radiation = method_free_water_based_on_radiation
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

    
    
    




