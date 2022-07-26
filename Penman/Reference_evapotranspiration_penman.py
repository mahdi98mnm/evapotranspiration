import Wind_speed_at_2m_above_ground_surface
import Soil_heat_flux_density
import Mean_Temperature_max_min
import Actual_Vapour_Pressure
import Saturation_Vapour_Pressure_With_Temperature
import Slope_Vapour_Pressure_Curve_With_Maen_Temperature
import Net_radiation_at_the_crop_surface
import Psychrometric_constant_With_Altitudes

def Calculate_Reference_evapotranspiration_penman(
    method_Net_longwave_radiation : str,
    method_Solar_or_shortwave_radiation : str,
    method_Soil_heat_flux_density : str,
    stddate : str,
    degree : int,
    minute : int,
    second : int,
    mode_data : str,
    Altitude_at_which_wind_speed_is_measured = None, 
    Measured_wind_speed = None,
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
    Soil_heat_capacity = None,
    Air_temperature_at_previous_step = None,
    Air_temperature_at_current_step = None,
    delta_time = None,
    Effective_soil_depth = None,
    Mean_air_temperature_of_previous_month = None,
    Mean_air_temperature_of_next_month = None,
    Mean_air_temperature_of_current_month = None,
    mode = None,
    u_2 = None
) -> float:

        """
        Description
        -----------
        calculate Wind speed at 2m above ground surface with Measured speed and height - eq 47 FAO56
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
        Actual duration of sunshine in a day : float
            Actual duration of sunshine in a day in hour per day
        Altitude_at_which_wind_speed_is_measured : float
            Altitude at which wind speed is measured in meter
        Measured_wind_speed : float 
            Measured wind speed in meter / second
            
        Returns
        -------
        Wind speed at 2m above ground surface : float
            Wind speed at 2m above ground surface in meter / second
        """

        if method_Soil_heat_flux_density == 'With_Effective_soil_depth':
            
            G = Soil_heat_flux_density.Soil_heat_flux_density.With_Effective_soil_depth(
                Soil_heat_capacity = Soil_heat_capacity,
                Air_temperature_at_previous_step = Air_temperature_at_previous_step,
                Air_temperature_at_current_step = Air_temperature_at_current_step,
                delta_time = delta_time,
                Effective_soil_depth = Effective_soil_depth
            )

        elif method_Soil_heat_flux_density == 'For_day_and_ten_day_periods':
            G = Soil_heat_flux_density.Soil_heat_flux_density.For_day_and_ten_day_periods(
            )

        elif method_Soil_heat_flux_density == 'For_monthly_periods':
            G = Soil_heat_flux_density.Soil_heat_flux_density.For_monthly_periods(
                Mean_air_temperature_of_previous_month = Mean_air_temperature_of_previous_month,
                Mean_air_temperature_of_next_month = Mean_air_temperature_of_next_month,
                Mean_air_temperature_of_current_month = Mean_air_temperature_of_current_month
            )

        elif method_Soil_heat_flux_density == 'For_hourly_or_shorter_periods':
            G = Soil_heat_flux_density.Soil_heat_flux_density.For_hourly_or_shorter_periods(
                mode,
                method_Net_longwave_radiation,
                method_Solar_or_shortwave_radiation,
                stddate,
                degree,
                minute,
                second,
                Altitude, 
                method_Actual_Vapour_Pressure,
                mode_data,
                T_dew,
                T_max,
                T_min,
                T_mean,
                RH_max,
                RH_min,
                RH_mean,
                T_wet,
                T_dry,
                a_psy,
                Actual_duration_of_sunshine_in_a_day,
                Monthly_average_sunshine_duration,
                Adjustment_coefficient_or_K_RS,
                e_a
            )
        
        if T_mean == None:
            T = Mean_Temperature_max_min.mean_temperature_max_min(
                T_max = T_max,
                T_min = T_min
            )
        
        if e_a == None :
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
        
        e_s_minus_e_a = Saturation_Vapour_Pressure_With_Temperature.total_saturation_vapour_pressure(
            T_max = T_max,
            T_min = T_min) - e_a

        if u_2 == None :
            u_2 = Wind_speed_at_2m_above_ground_surface.wind_speed_at_2m_above_ground_surface(Altitude_at_which_wind_speed_is_measured, Measured_wind_speed)
        #  BUG I have to make the R_n (Calculate_Net_radiation_at_the_crop_surface) variable then print page 72 ,EX18 
        # print(Solar_or_shortwave_radiation.Angstrom(stddate,degree , minute , second ,
        # Actual_duration_of_sunshine_in_a_day ))
        
        return (0.408 * Slope_Vapour_Pressure_Curve_With_Maen_Temperature.slope_vapour_pressure_curve_with_maen_temperature(
            T_max = T_max,
            T_min = T_min,
            T_mean = T_mean) * (Net_radiation_at_the_crop_surface.net_radiation_at_the_crop_surface(
            method_Net_longwave_radiation = method_Net_longwave_radiation,
            method_Solar_or_shortwave_radiation = method_Solar_or_shortwave_radiation,
            stddate = stddate,
            degree = degree,
            minute = minute,
            second = second,
            Altitude = Altitude, 
            method_Actual_Vapour_Pressure = method_Actual_Vapour_Pressure,
            T_dew = T_dew,
            T_max = T_max,
            T_min = T_min,
            T_mean = T_mean,
            RH_max = RH_max,
            RH_min = RH_min,
            RH_mean = RH_mean,
            T_wet = T_wet,
            T_dry = T_dry,
            a_psy = a_psy,
            Actual_duration_of_sunshine_in_a_day = Actual_duration_of_sunshine_in_a_day,
            Monthly_average_sunshine_duration = Monthly_average_sunshine_duration,
            Adjustment_coefficient_or_K_RS = Adjustment_coefficient_or_K_RS,
            e_a = e_a,
            mode_data = mode_data) - G) + Psychrometric_constant_With_Altitudes.psychrometric_constant_with_altitudes(Altitude = Altitude) * (900 / (T + 273)) 
            * u_2 *
            e_s_minus_e_a ) / (Slope_Vapour_Pressure_Curve_With_Maen_Temperature.slope_vapour_pressure_curve_with_maen_temperature(
            T_max = T_max,
            T_min = T_min,
            T_mean = T_mean) + Psychrometric_constant_With_Altitudes.psychrometric_constant_with_altitudes(Altitude = Altitude) * 
            (1 + (0.34 * u_2)))

# page 70 ,EX17
# print(Calculate_Reference_evapotranspiration_penman(method_Net_longwave_radiation = 'With_have_e_a',
#         method_Solar_or_shortwave_radiation = 'Angstrom',
#         method_Soil_heat_flux_density ='For_monthly_periods',
#         stddate='2019-04-15',
#         degree = 13,
#         minute = 44,
#         second = 0 ,
#         Altitude = 2,
#         T_max=34.8,
#         T_min=25.6,
#         e_a=2.85,
#         u_2=2,
#         Monthly_average_sunshine_duration=8.5,
#         Mean_air_temperature_of_current_month = 30.2,
#         Mean_air_temperature_of_previous_month=29.2,
#         mode_data = 'monthly'))

# print(Calculate_maximum_possible_sunshine_duration_in_a_day(degree=13 , minute=44 , second=0 , stddate='2019-04-15'))

# page 72 ,EX18 
print(Calculate_Reference_evapotranspiration_penman(method_Net_longwave_radiation = 'Without_have_e_a',
        method_Solar_or_shortwave_radiation = 'Angstrom',
        method_Soil_heat_flux_density ='For_day_and_ten_day_periods',
        stddate='2019-07-06',
        degree = 50,
        minute = 48,
        second = 0 ,
        Altitude = 100,
        T_max=21.5,
        T_min=12.3,
        RH_max=84,
        RH_min=63,
        Altitude_at_which_wind_speed_is_measured =10, 
        Measured_wind_speed = 2.78,
        Actual_duration_of_sunshine_in_a_day=9.25,
        method_Actual_Vapour_Pressure = 'RH_and_T_max_min',
        mode_data = 'daily'
        ))