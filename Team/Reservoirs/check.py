
from typing import NoReturn


def check_not_negative(
    Height : float
) -> NoReturn:
    """
    Description
    -----------
    Check Height value is greater than 0
    Parameters
    ----------
    Height : float
        Height in m
    """

    if Height < 0 :
        raise ValueError("Height should be grater than zero")
        
def check_max_min(
    Height_max : float,
    Height_min : float
) -> NoReturn:
    """
    Description
    -----------
    Check maximum Height value be greater than minimum value
    Parameters
    ----------
    Height_max : float
        maximum Height in m
    Height_min : float
        minimum Height in m
       
    """

    if Height_max < Height_min :
        raise ValueError("maximum height must be greater than minimum height")


def check_Value_p(
    p : float
) -> NoReturn:
    
    """
    Description
    -----------
    Check p value is greater than 1
    Parameters
    ----------
    p : float
       a constant parameter
    """
    
    if not 1 < p :
        raise ValueError(
            f'p value must be greater than 1: {p}'
        )

def check_Value_a(
    a : float
) -> NoReturn:
    
    """
    Description
    -----------
    Check a value is greater than 0
    Parameters
    ----------
    a : float
        a constant parameter
    """
    
    if not 0 < a :
        raise ValueError(
            f'a value must be greater than 0: {a}'
        )

