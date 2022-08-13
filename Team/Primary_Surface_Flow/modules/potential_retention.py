from .check import check_curve_number

def calculate_potential_retention(
    curve_number: float
) -> float:
    """
    Description
    -----------
    Calculate potential retention known as "S"
    **Reference**: National Resources Conservation Service, National Engineering Handbook, Section 4 "Hydrology" (1985)

    Parameters
    ----------
    curve_number : float
        An index of the land condition as indicated by soils, cover, land use - Between 0 to 100 - dimensionless

    Returns
    -------
    - potential_retention : float
        Maximum depth of storm rainfall that could potentially be abstracted by a given site - Starts from 0 - mm
    """

    check_curve_number(curve_number)

    # Constant 25.4, convert inch to mm
    return (1000/curve_number - 10)*25.4