import Net_longwave_radiation
import Solar_or_shortwave_radiation


def net_radiation_at_the_crop_surface(
    method_Net_longwave_radiation : str,
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
) -> float:

        """
        Description
        -----------
        calculate Net radiation at the crop surface with Net solar or shortwave radiation and Net longwave radiation - eq 40 FAO56
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
            
        Returns
        -------
        Net longwave radiation : float
            Net longwave radiation in MJ / m**2 /day
        """

        if method_Net_longwave_radiation == 'Without_have_e_a':
            R_nl = Net_longwave_radiation.Net_longwave_radiation.Without_have_e_a (
                method_Solar_or_shortwave_radiation = method_Solar_or_shortwave_radiation,
                method_Actual_Vapour_Pressure = method_Actual_Vapour_Pressure,
                stddate = stddate,
                degree = degree,
                minute = minute,
                second = second,
                T_max = T_max,
                T_min = T_min,
                Adjustment_coefficient_or_K_RS = Adjustment_coefficient_or_K_RS,
                mode_data = mode_data,
                Monthly_average_sunshine_duration = Monthly_average_sunshine_duration,
                Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day,
                Altitude = Altitude,
                T_dew = T_dew,
                RH_max = RH_max,
                RH_min = RH_min,
                RH_mean = RH_mean,
                T_wet = T_wet,
                T_dry = T_dry,
                a_psy = a_psy
            )


        elif method_Net_longwave_radiation == 'With_have_e_a':
            R_nl = Net_longwave_radiation.Net_longwave_radiation.With_have_e_a (
                method_Solar_or_shortwave_radiation = method_Solar_or_shortwave_radiation,
                stddate = stddate,
                degree = degree,
                minute = degree,
                second = second,
                T_max = T_max,
                T_min = T_min,
                e_a = e_a,
                mode_data = mode_data,
                Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day,
                Monthly_average_sunshine_duration = Monthly_average_sunshine_duration,
                Altitude = Altitude,
                Adjustment_coefficient_or_K_RS = Adjustment_coefficient_or_K_RS
            )

        

        if method_Solar_or_shortwave_radiation == 'Angstrom':
            R_ns = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Angstrom(
                stddate = stddate,
                degree = degree, 
                minute = minute,
                second = second,
                mode_data = mode_data,
                Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day,
                Monthly_average_sunshine_duration = Monthly_average_sunshine_duration
            ) * 0.77


        elif method_Solar_or_shortwave_radiation == 'Hargreaves':
            R_ns = Solar_or_shortwave_radiation.Solar_or_shortwave_radiation.Hargreaves(
                stddate = stddate,
                degree = degree,
                minute = minute,
                second = second,
                T_max = T_max,
                T_min = T_min,
                Adjustment_coefficient_or_K_RS = Adjustment_coefficient_or_K_RS
            ) * 0.77 


        return R_ns - R_nl


# Check_Calculate Net radiation at the crop surface ----- page53 EX12 FAO56
# print(net_radiation_at_the_crop_surface(method_Net_longwave_radiation='With_have_e_a' , 
# method_Solar_or_shortwave_radiation='Angstrom' , stddate='2019-05-15',degree=-22 , minute=54 ,
# second= 0 , Actual_duration_of_sunshine_in_a_day = 220, T_max=25.1,
# T_min=19.1 ,e_a=2.1, mode_data = 'monthly'))
