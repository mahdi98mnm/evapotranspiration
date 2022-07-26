
def pressure_with_altitudes(
    Altitude : float
) -> float:
    
    """
    Description
    -----------
    calculate pressure with Altitudes - eq 7 FAO56
    ----------
    Altitude : float
        Height in meter
    
    Returns
    -------
    Pressure : float
        pressure in Kilo pascal
    """
    
    return 101.3 * ((293 - (0.0065 * Altitude))/293)**5.26

# Check_Calculate_Pressure_With_Altitudes----- page32 EX2 FAO56
# print(pressure_with_altitudes(1800))