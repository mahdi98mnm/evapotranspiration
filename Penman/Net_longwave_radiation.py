import Solar_or_shortwave_radiation
import Constant
import Actual_Vapour_Pressure
import Convert
import math
import Clear_sky_solar_or_clear_sky_shortwave_radiation

class Net_longwave_radiation :
   
    # init method or constructor 
    def __init__(
        self, 
        method_Solar_or_shortwave_radiation : str,
        stddate : str,
        degree : int,
        minute : int,
        second : int,
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
        Monthly_average_sunshine_duration = None,
        Adjustment_coefficient_or_K_RS = None,
        e_a = None,
        mode_data = None
    ):
        self.degree = degree
        self.minute = minute
        self.second = second
        self.stddate = stddate
        self.Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day
        self.T_min = T_min
        self.T_max= T_max
        self.Adjustment_coefficient_or_K_RS= Adjustment_coefficient_or_K_RS
        self.Altitude = Altitude
        self.method_Actual_Vapour_Pressure = method_Actual_Vapour_Pressure
        self.method_Solar_or_shortwave_radiation = method_Solar_or_shortwave_radiation
        self.T_dew = T_dew
        self.T_mean = T_mean
        self.RH_max = RH_max
        self.RH_min = RH_min
        self.RH_mean = RH_mean
        self.T_wet = T_wet
        self.T_dry = T_dry
        self.a_psy = a_psy
        self.e_a = e_a
        self.Monthly_average_sunshine_duration = Monthly_average_sunshine_duration
        self.mode_data = mode_data 

        # Sample Method 
    def Without_have_e_a (
        method_Solar_or_shortwave_radiation :str,
        method_Actual_Vapour_Pressure : str,
        stddate :str,
        degree : int,
        minute : int,
        second : int,
        T_max : float,
        T_min : float,
        Adjustment_coefficient_or_K_RS : float,
        mode_data = None,
        Monthly_average_sunshine_duration = None,
        Actual_duration_of_sunshine_in_a_day = None,
        Altitude = None,
        T_dew =None,
        RH_max = None,
        RH_min = None,
        RH_mean = None,
        T_wet = None,
        T_dry = None,
        a_psy = None
    )-> float:

        """
    Description
    -----------
    calculate Net longwave radiation with Tempreture and Actual Vapour Pressure - eq 39 FAO56
    ----------
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
    Net longwave radiation : float
        Net longwave radiation in MJ / m**2 /day
    """
        if method_Solar_or_shortwave_radiation == 'Angstrom':
            R_s = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Angstrom(
                stddate = stddate,
                degree = degree, 
                minute = minute,
                second = second,
                mode_data = mode_data,
                Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day,
                Monthly_average_sunshine_duration = Monthly_average_sunshine_duration
            )
        elif method_Solar_or_shortwave_radiation == 'Hargreaves':
            R_s = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Hargreaves(
                stddate = stddate,
                degree = degree,
                minute = minute,
                second = second,
                T_max = T_max,
                T_min = T_min,
                Adjustment_coefficient_or_K_RS = Adjustment_coefficient_or_K_RS
            )
        

        if method_Actual_Vapour_Pressure == 'dew':
            e_a = Actual_Vapour_Pressure.Actual_Vapour_Pressure.dew(T_dew = T_dew)

        elif method_Actual_Vapour_Pressure == 'RH_and_T_max_min':
            e_a = Actual_Vapour_Pressure.Actual_Vapour_Pressure.RH_and_T_max_min(T_max = T_max, T_min = T_min, RH_max = RH_max,
            RH_min = RH_min)

        elif method_Actual_Vapour_Pressure == 'RH_max_and_T_min':
            e_a = Actual_Vapour_Pressure.Actual_Vapour_Pressure.RH_max_and_T_min(T_min = T_min, RH_max = RH_max)

        elif method_Actual_Vapour_Pressure == 'RH_mean_T_max_min':
            e_a = Actual_Vapour_Pressure.Actual_Vapour_Pressure.RH_mean_T_max_min(T_max = T_max, T_min = T_min,
            RH_max = None, RH_min = None, RH_mean = None)

        elif method_Actual_Vapour_Pressure == 'T_wet_T_dry':
            e_a = Actual_Vapour_Pressure.Actual_Vapour_Pressure.T_wet_T_dry(T_wet = T_wet, T_dry = T_dry,
            a_psy = a_psy, Altitude = Altitude)
        
        temp_1 = Constant.STEFAN_BOLTZMANN_CONSTANT * (((Convert.temperature_celsius_To_kelvin(
            Temperature = T_max)**4) + (Convert.temperature_celsius_To_kelvin(Temperature = T_min)**4)) / 2 )
        temp_2 = 0.34 - (0.14 * math.sqrt(e_a))
        temp_3 = (1.35 * (R_s / Clear_sky_solar_or_clear_sky_shortwave_radiation.clear_sky_solar_or_clear_sky_shortwave_radiation(
                degree, minute, second, stddate, Altitude = None))) - 0.35

        R_nl = temp_1 * temp_2 * temp_3

        return R_nl


    def With_have_e_a (
        method_Solar_or_shortwave_radiation :str,
        stddate :str,
        degree : int,
        minute : int,
        second : int,
        T_max : float,
        T_min : float,
        e_a : float,
        mode_data = None,
        Actual_duration_of_sunshine_in_a_day = None,
        Monthly_average_sunshine_duration = None,
        Altitude = None,
        Adjustment_coefficient_or_K_RS = None
    )-> float:

        """
    Description
    -----------
    calculate Net longwave radiation with Tempreture and Actual Vapour Pressure - eq 39 FAO56
    ----------
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
    Maximum Tempreture and Minimum Tempreture : float
        Maximum Tempreture and Minimum Tempreture in celsius
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
    Net longwave radiation : float
        Net longwave radiation in MJ / m**2 /day
    """
        if method_Solar_or_shortwave_radiation == 'Angstrom':
            R_s = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Angstrom(
                stddate = stddate,
                degree = degree, 
                minute = minute,
                second = second,
                mode_data = mode_data,
                Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day,
                Monthly_average_sunshine_duration = Monthly_average_sunshine_duration
            )

        elif method_Solar_or_shortwave_radiation == 'Hargreaves':
            R_s = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Hargreaves(
                stddate = stddate,
                degree = degree,
                minute = minute,
                second = second,
                T_max = T_max,
                T_min = T_min,
                Adjustment_coefficient_or_K_RS = Adjustment_coefficient_or_K_RS
            )
        
        temp_1 = Constant.STEFAN_BOLTZMANN_CONSTANT * (((Convert.temperature_celsius_To_kelvin(
            Temperature = T_max)**4) + (Convert.temperature_celsius_To_kelvin(Temperature = T_min)**4)) / 2 )
        temp_2 = 0.34 - (0.14 * math.sqrt(e_a))
        temp_3 = (1.35 * (R_s / Clear_sky_solar_or_clear_sky_shortwave_radiation.clear_sky_solar_or_clear_sky_shortwave_radiation(
                degree, minute, second, stddate, Altitude = None))) - 0.35

        R_nl =  temp_1 * temp_2 * temp_3


        return R_nl


# Check_Net longwave radiation ----- page52 EX11 FAO56
# print(Net_longwave_radiation.With_have_e_a(method_Solar_or_shortwave_radiation='Angstrom' , stddate='2019-05-15' , degree=-22 , minute=54 , second=0 , Actual_duration_of_sunshine_in_a_day=220 , T_max=25.1 , T_min=19.1 ,e_a=2.1 , mode_data = 'monthly'))
