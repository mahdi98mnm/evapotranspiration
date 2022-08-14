from datetime import date

def correction_crop_coefficient_for_step_mid_and_end(
    crop_coefficient_mid : float,
    crop_coefficient_end : float,
    RH_min : float,
    Maximum_Crop_Height : float,
    Altitude_at_which_wind_speed_is_measured : float = None, 
    Measured_wind_speed : float = None,
    wind_speed_at_2m : float = None
) -> float:
    
    """
    Description
    -----------
    calculate correction_crop_coefficient_for_step_mid_and_end - eq 70 FAO56
    ----------
    crop_coefficient_mid : float
        crop_coefficient_mid - crop_coefficient in middle of step - Table 12 Page 110 FAO56
    crop_coefficient_end : float
        crop_coefficient_end - crop_coefficient in end of step - Table 12 Page 110 FAO56
    RH_min : float
        Minimum relative humidity in percent
    Maximum_Crop_Height : float - Table 12 Page 110 FAO56
        Maximum crop height in meter
    Altitude_at_which_wind_speed_is_measured : float
        Altitude at which wind speed is measured in meter
    Measured_wind_speed : float 
        Measured wind speed in meter / second
    wind_speed_at_2m : float
        Wind speed at 2m in meter / second
    

    Returns
    -------
    Modified crop coefficient : float
        Modified crop coefficient in No unit

    """
    if wind_speed_at_2m is None:
        wind_speed_at_2m = Wind_speed_at_2m_above_ground_surface.wind_speed_at_2m_above_ground_surface(
            Altitude_at_which_wind_speed_is_measured = Altitude_at_which_wind_speed_is_measured,
            Measured_wind_speed = Measured_wind_speed
        )
    else:
        wind_speed_at_2m = wind_speed_at_2m

    if crop_coefficient_mid >= 0.45 :
        cor_crop_coefficient_mid = crop_coefficient_mid + (0.04 * (wind_speed_at_2m - 2.0) - 0.004 * (
            RH_min - 45.0)) * (Maximum_Crop_Height / 3) ** 0.3
    elif wind_speed_at_2m != 2 or RH_min != 45 :
        cor_crop_coefficient_mid = crop_coefficient_mid + (0.04 * (wind_speed_at_2m - 2.0) - 0.004 * (
            RH_min - 45.0)) * (Maximum_Crop_Height / 3) ** 0.3
    else :
        cor_crop_coefficient_mid = crop_coefficient_mid
    

    if crop_coefficient_end >= 0.45 :
        cor_crop_coefficient_end = crop_coefficient_end + (0.04 * (wind_speed_at_2m - 2.0) - 0.004 * (
            RH_min - 45.0)) * (Maximum_Crop_Height / 3) ** 0.3
        
    elif wind_speed_at_2m != 2 or RH_min != 45 :
        cor_crop_coefficient_end = crop_coefficient_end + (0.04 * (wind_speed_at_2m - 2.0) - 0.004 * (
            RH_min - 45.0)) * (Maximum_Crop_Height / 3) ** 0.3
    else :
        cor_crop_coefficient_end = crop_coefficient_end
    


    return cor_crop_coefficient_mid, cor_crop_coefficient_end
   



def calculate_crop_coefficient_for_linear_changes_steps(
    crop_coefficient_ini : float,
    crop_coefficient_mid : float,
    crop_coefficient_end : float,
    length_ini_crop : int,
    length_dev_crop : int,
    length_mid_crop : int,
    length_late_crop : int,
    plant_date : str,
    modeling_date : str
) -> float:
    
    """
    Description
    -----------
    calculate crop_coefficient_for_linear_changes_steps in special day - eq 66 FAO56
    ----------
    crop_coefficient_ini : float
        crop_coefficient_ini - crop_coefficient in start of step - Table 12 Page 110 FAO56
    crop_coefficient_mid : float
        crop_coefficient_mid - crop_coefficient in middle of step - Table 12 Page 110 FAO56
    crop_coefficient_end : float
        crop_coefficient_end - crop_coefficient in end of step - Table 12 Page 110 FAO56
    length_ini_crop : int
        length_ini_crop - length of initial crop in day - Table 11 Page 104 FAO56
    length_dev_crop : int
        length_dev_crop - length of development crop in day - Table 11 Page 104 FAO56
    length_mid_crop : int
        length_mid_crop - length of middle crop in day - Table 11 Page 104 FAO56
    length_late_crop : int
        length_late_crop - length of late crop in day - Table 11 Page 104 FAO56
    plant_date : str
        plant_date - Date of planting in format YYYY-MM-DD - Table 11 Page 104 FAO56 according to Region
    modeling_date : str
        modeling_date - Date of modeling in format YYYY-MM-DD


    Returns
    -------
    crop_coefficient : float
        crop_coefficient in special day in No unit

    """
    plant_date = date(int(plant_date[:4]), int(plant_date[5:7]), int(plant_date[8:]))
    modeling_date = date(int(modeling_date[:4]), int(modeling_date[5:7]), int(modeling_date[8:]))
    n = modeling_date - plant_date
    n_day = n.days
    # n_day : Number of days since the beginning of crop cultivation

    if n_day <= length_ini_crop :
        crop_coefficient = crop_coefficient_ini

    elif length_ini_crop < n_day <= length_ini_crop + length_dev_crop :
        crop_coefficient = crop_coefficient_ini + ((n_day - length_ini_crop) / length_dev_crop) * (
            crop_coefficient_mid - crop_coefficient_ini)

    elif length_ini_crop + length_dev_crop < n_day <= length_ini_crop + length_dev_crop + length_mid_crop :
        crop_coefficient = crop_coefficient_mid

    elif length_ini_crop + length_dev_crop + length_mid_crop < n_day <= length_ini_crop + length_dev_crop + length_mid_crop + length_late_crop :
        crop_coefficient = crop_coefficient_mid + ((n_day - length_ini_crop - length_dev_crop - length_mid_crop) / length_late_crop) * (
            crop_coefficient_end - crop_coefficient_mid)
    
    return crop_coefficient

