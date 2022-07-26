from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import datetime
from calendar import monthrange


def number_of_days_in_month(
    stddate: str
) -> int:
    
    """
    Description
    -----------
    Calculate the number of days in a month - https://techoverflow.net/2019/05/16/how-to-get-number-of-days-in-month-in-python/
    ----------
    stddate : str
        Date with the specified standard
   
    Returns
    -------
    Number of days in month : int
        Number of days in month in Number
    """
        
    return monthrange(int(stddate[:4]), int(stddate[5:7]))[1]

# Check_Calculate Number of days in month -----
# print(number_of_days_in_month('2019-05-15'))