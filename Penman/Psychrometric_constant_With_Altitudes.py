import Pressure_With_Altitudes

def psychrometric_constant_with_altitudes(
    Altitude : float
) -> float:
    
    """
    Description
    -----------
    calculate Psychrometric constant with Altitudes - eq 8 FAO56
    ----------
    Altitude : float
        Height in meter
    
    Returns
    -------
    Psychrometric constant : float
        Psychrometric constant in Kilo pascal per celsius
    """
    P = Pressure_With_Altitudes.pressure_with_altitudes(Altitude)
    return 0.665 * (10**-3) * P

# Check_Calculate_Calculate_Psychrometric_constant_With_Altitudes----- page214 Table2.2 FAO56
# print(psychrometric_constant_with_altitudes(100))