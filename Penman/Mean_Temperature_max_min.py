
def mean_temperature_max_min(
    T_max : float,
    T_min : float
) -> float:
    
    """
    Description
    -----------
    calculate Mean Temperature With Tmax and Tmin - eq 9 FAO56
    ----------
    T_max : float
        Maximum Temperature in celsius
    T_min : float
        Minimum Temperature in celsius
    
    Returns
    -------
    Mean Temperature : float
        Mean Temperature in celsius
    """
    
    return (T_max + T_min)/2