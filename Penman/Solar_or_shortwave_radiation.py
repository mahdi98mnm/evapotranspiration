import Maximum_Possible_Sunshine_Duration_In_A_Day
import Extraterrestrial_Radiation
import math
import Number_of_days_in_month

class Solar_or_shortwave_radiation  :
   
    # init method or constructor 
    def __init__(self,
        stddate : str,
        degree,
        minute,
        second,
        Actual_duration_of_sunshine_in_a_day = None,
        Monthly_average_sunshine_duration = None,
        mode_data = None,
        T_max = None,
        T_min = None,
        Adjustment_coefficient_or_K_RS = None
    ):
        self.degree = degree
        self.minute = minute
        self.second = second
        self.stddate = stddate
        self.Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day
        self.T_min = T_min
        self.T_max= T_max
        self.Adjustment_coefficient_or_K_RS= Adjustment_coefficient_or_K_RS
        self.Monthly_average_sunshine_duration = Monthly_average_sunshine_duration
        self.mode_data = mode_data


   
    # Sample Method 
    def Angstrom (
        stddate :str,degree : int,
        minute : int,
        second : int,
        mode_data : str,
        Actual_duration_of_sunshine_in_a_day = None, 
        Monthly_average_sunshine_duration = None
    )-> float:
    
        """
        Description
        -----------
        calculate Solar or shortwave radiation with Relative sunshine duration - eq 35 FAO56
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
        Actual duration of sunshine in a day : float
            Actual duration of sunshine in a day in hour
        Monthly_average_sunshine_duration : float
            Monthly average sunshine duration in hour per day
        mode_data : str 
            monthly or daily

        Returns
        -------
        Solar or shortwave radiation : float
            Solar or shortwave radiation in MJ/m**2/day
        """
        if mode_data == 'monthly':
            if Monthly_average_sunshine_duration != None:
                Monthly_average_sunshine_duration = Monthly_average_sunshine_duration

            elif Monthly_average_sunshine_duration == None:
                Monthly_average_sunshine_duration = Actual_duration_of_sunshine_in_a_day / Number_of_days_in_month.number_of_days_in_month(stddate)
            
        elif mode_data == 'daily':
            Monthly_average_sunshine_duration = Actual_duration_of_sunshine_in_a_day
        
        N = Maximum_Possible_Sunshine_Duration_In_A_Day.maximum_possible_sunshine_duration_in_a_day(degree, minute , second, stddate) 
        temp_1 = Extraterrestrial_Radiation.extraterrestrial_radiation(degree, minute , second, stddate)

        return (0.25 + (0.5 * (Monthly_average_sunshine_duration / N ))) * temp_1
        
    
    def Hargreaves(
        stddate : str,
        degree : int,
        minute : int,
        second : int,
        T_max : float,
        T_min : float,
        Adjustment_coefficient_or_K_RS : float
    )-> float:
        
        """
        Description
        -----------
        calculate Solar or shortwave radiation with max and min Tempreture - eq 50 FAO56
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
        T_max : float
            Maximum Temperature in celsius
        T_min : float
            Minimum Temperature in celsius
        Adjustment_coefficient_or_K_RS : float
            Adjustment coefficient in C**-0.5 -- between 0.16 to 0.19
                for interior locations, where land mass dominates and air masses are not strongly
                influenced by a large water body, kRs ≅ 0.16;
                for coastal locations, situated on or adjacent to the coast of a large land mass and where
                air masses are influenced by a nearby water body, kRs ≅ 0.19

        Returns
        -------
        Solar or shortwave radiation : float
            Solar or shortwave radiation in MJ/m**2/day
        """
        temp_1 = Extraterrestrial_Radiation.extraterrestrial_radiation(degree, minute , second, stddate)


        return Adjustment_coefficient_or_K_RS * math.sqrt(T_max - T_min) * temp_1


# Check_Solar or shortwave radiation ----- page50 EX10 FAO56
# print(Solar_or_shortwave_radiation.Angstrom(stddate='2019-05-15',degree=-22 , minute=54 , second= 0 , Actual_duration_of_sunshine_in_a_day = 220 , mode_data = 'monthly'))
# print(Solar_or_shortwave_radiation.Angstrom(stddate='2019-05-15',degree=-22 , minute=54 , second= 0 , Monthly_average_sunshine_duration = 7.1 , mode_data = 'monthly'))
# print(Solar_or_shortwave_radiation.Angstrom(stddate='2019-05-15',degree=-22 , minute=54 , second= 0 , Actual_duration_of_sunshine_in_a_day = 220, Monthly_average_sunshine_duration = 7.1 , mode_data = 'monthly'))

# Check_Solar or shortwave radiation ----- page61 EX15 FAO56
# print(Solar_or_shortwave_radiation.Hargreaves(stddate='2019-07-15' , degree=45 , minute=43 , second=0 , T_max=26.6 , T_min=14.8 , Adjustment_coefficient_or_K_RS =0.16))
