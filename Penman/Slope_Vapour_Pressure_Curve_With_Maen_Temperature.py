import Mean_Temperature_max_min
import math

def slope_vapour_pressure_curve_with_maen_temperature(
    **kwargs)-> float:
  

    T_max = kwargs.get('T_max', None)
    T_min = kwargs.get('T_min', None)
    T_mean = kwargs.get('T_mean', None)

    """
    Description
    -----------
    calculate Slope Vapour Pressure Curve With Maen Temperature - eq 13 FAO56
    ----------
    T_max : float
        Maximum Temperature in celsius
    T_min : float
        Minimum Temperature in celsius
    T_mean : float
        Mean Temperature in celsius

    Returns
    -------
    Slope Vapour Pressure Curve : float
        Slope Vapour Pressure Curve in Kilo pascal per celsius
    """
    if T_mean == None:
        T_mean = Mean_Temperature_max_min.mean_temperature_max_min(T_max, T_min)
    
    

    return 4098 * (0.6108 * math.exp((17.27 * T_mean) / (T_mean + 237.3))) / ((T_mean + 237.3)**2)

# Check_Calculate_Slope_Vapour_Pressure_Curve_With_Maen_Temperature----- page216 Table2.4 FAO56
# print(slope_vapour_pressure_curve_with_maen_temperature(T_max=5,T_min=2,T_mean=2))
# print(slope_vapour_pressure_curve_with_maen_temperature(T_mean=1))
# print(slope_vapour_pressure_curve_with_maen_temperature(T_max=5,T_min=2))
# print(slope_vapour_pressure_curve_with_maen_temperature(T_max=5,T_mean=2))