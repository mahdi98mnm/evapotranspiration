import crop

print(crop.correction_crop_coefficient_for_step_mid_and_end(
    crop_coefficient_mid = 1.15,
    crop_coefficient_end = 0.35,
    RH_min = 30,
    Maximum_Crop_Height = 0.4,
    wind_speed_at_2m = 2.2))


cor = crop.correction_crop_coefficient_for_step_mid_and_end(
    crop_coefficient_mid = 1.15,
    crop_coefficient_end = 0.35,
    RH_min = 30,
    Maximum_Crop_Height = 0.4,
    wind_speed_at_2m = 2.2)

crop_coefficient_mid =cor[0]

crop_coefficient_end =cor[1]

print(crop.calculate_crop_coefficient_for_linear_changes_steps(
    crop_coefficient_ini = 0.15,
    crop_coefficient_mid = crop_coefficient_mid,
    crop_coefficient_end = crop_coefficient_end,
    length_ini_crop = 25,
    length_dev_crop = 25,
    length_mid_crop = 30,
    length_late_crop = 20,
    plant_date = '2019-06-01',
    modeling_date = '2019-06-21'))
