

def check_date_for_crop_coefficient(
    plant_date : str,
    modeling_date : str,
    n : int,
    length_ini_crop : int,
    length_dev_crop : int,
    length_mid_crop : int,
    length_late_crop : int
):
    
    if plant_date > modeling_date :
        raise ValueError('The modeling day should be more than the plant day')
    
    if n > length_ini_crop + length_dev_crop + length_mid_crop + length_late_crop :
        raise ValueError('You are out of growth period')


