import Saturation_Vapour_Pressure_With_Temperature
import Pressure_With_Altitudes


class Actual_Vapour_Pressure:
   
    # init method or constructor 
    def __init__(self,
     T_dew = None,
     T_max = None,
     T_min = None,
     T_mean = None,
     RH_max =None,
     RH_min = None,
     RH_mean = None,
     T_wet = None,
     T_dry = None,
     a_psy = None
     ):
        self.T_dew = T_dew
        self.T_max = T_max
        self.T_min = T_min
        self.T_mean= T_mean
        self.RH_max= RH_max
        self.RH_min= RH_min
        self.RH_mean=RH_mean
        self.T_wet = T_wet
        self.T_dry = T_dry
        self.a_psy = a_psy


   
    # Sample Method 
    def dew(T_dew:float)-> float:
    
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
        
        return Saturation_Vapour_Pressure_With_Temperature.saturation_vapour_pressure_with_temperature(Temperature = T_dew)
    
    def RH_and_T_max_min(
        T_max:float,
        T_min:float,
        RH_max:float,
        RH_min:float
        )-> float:
        
        """
        Description
        -----------
        calculate Actual Vapour Pressure With Maximum relative humidity and Minimum relative humidity and 
        Maximum Tempreture and Minimum Tempreture - eq 17 FAO56
        ----------
        Maximum relative humidity and Minimum relative humidity : float
            Maximum relative humidity and Minimum relative humidity in percent
        Maximum Tempreture and Minimum Tempreture : float
            Maximum Tempreture and Minimum Tempreture in celsius

        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """
        
        return ((Saturation_Vapour_Pressure_With_Temperature.saturation_vapour_pressure_with_temperature(Temperature = T_min) * (
            RH_max/100)) + (Saturation_Vapour_Pressure_With_Temperature.saturation_vapour_pressure_with_temperature(
                Temperature = T_max) * (RH_min/100))) / 2
    
    def RH_max_and_T_min(
        T_min : float,
        RH_max : float
        )-> float:
        
        """
        Description
        -----------
        calculate Actual Vapour Pressure With Maximum relative humidity and Minimum Tempreture - eq 18 FAO56
        ----------
        Maximum relative humidity : float
            Maximum relative humidity in percent
        Minimum Tempreture : float
            Minimum Tempreture in celsius

        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """

        return Saturation_Vapour_Pressure_With_Temperature.saturation_vapour_pressure_with_temperature(
            Temperature = T_min) * (RH_max/100)
    

    def RH_mean_T_max_min(
        T_max,
        T_min,
        RH_max = None,
        RH_min = None,
        RH_mean = None
        )-> float:
        
        """
        Description
        -----------
        calculate Actual Vapour Pressure With Mean relative humidity and Maximum Tempreture and Minimum Tempreture - eq 19 FAO56
        ----------
        Mean relative humidity : float
            Mean relative humidity in percent
        Maximum Tempreture and Minimum Tempreture : float
            Maximum Tempreture and Minimum Tempreture in celsius

        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """

        if RH_mean == None :
            RH_mean = (RH_max + RH_min) / 2


        return ((Saturation_Vapour_Pressure_With_Temperature.saturation_vapour_pressure_with_temperature(
                Temperature = T_max) + Saturation_Vapour_Pressure_With_Temperature.saturation_vapour_pressure_with_temperature(
                Temperature = T_min))/2) * (RH_mean/100)
    

    def T_wet_T_dry(
        T_wet : float,
        T_dry : float,
        a_psy : float,
        Altitude : float
        )-> float:

        """
        Description
        -----------
        calculate Actual Vapour Pressure With Wet Tempreture and Dry Tempreture and Coefficient of psychrometer - eq 15 and 16 FAO56
        ----------
        Wet Tempreture : float
            Wet Tempreture in celsius
        Dry Tempreture : float
            Dry Tempreture in celsius
        Coefficient of psychrometer : float
            Coefficient of psychrometer in celsius**-1
            Coefficient of psychrometer for ventilated (Asmann type) psychrometers movement of some 5 m/s = 0.000662
            Coefficient of psychrometer for natural ventilated psychrometers (about 1 m/s)= 0.0008
            Coefficient of psychrometer for non-ventilated psychrometers installed indoors = 0.0012
        Altitude : float
            Height in meter
        Returns
        -------
        Actual Vapour Pressure : float
            Actual Vapour Pressure in Kilo pascal
        """
        gama_psy = a_psy * Pressure_With_Altitudes.pressure_with_altitudes(Altitude)

        return Saturation_Vapour_Pressure_With_Temperature.saturation_vapour_pressure_with_temperature(
            Temperature = T_wet) - (gama_psy * (T_dry - T_wet))


# Check_calculate Actual_Vapour_Pressure ----- page39 EX5 FAO56
# print(f'e_a2 is : {Actual_Vapour_Pressure.RH_and_T_max_min(T_max = 25, T_min = 18, RH_max = 82, RH_min = 54)}')
# print(f'e_a4_1 is : {Actual_Vapour_Pressure.RH_mean_T_max_min(T_max=25 , T_min=18 , RH_max=82 , RH_min=54)}')
# print(f'e_a4_2 is : {Actual_Vapour_Pressure.RH_mean_T_max_min(T_max=25 , T_min=18 , RH_mean=68)}')
# print(f'e_a4_3 is : {Actual_Vapour_Pressure.RH_mean_T_max_min(T_max=25 , T_min=18 , RH_max=82 , RH_min=40 , RH_mean=68)}')
# print(f'e_a5 is : {Actual_Vapour_Pressure.T_wet_T_dry(T_wet = 19.5 , T_dry = 25.6 , a_psy = 0.000662 , Altitude = 1200 )}')
