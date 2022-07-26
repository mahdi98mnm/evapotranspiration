
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import datetime
from calendar import monthrange

def standard_date_to_Julian_day (
    stddate: str
    ) -> int:
       
    """
    Description
    -----------
    calculate Julian Day with standard date
    Ref:https://rafatieppo.github.io/post/2018_12_01_juliandate/
    ----------
    stddate : str
        Date with the specified standard

    Returns
    -------
    Julian Day : int
        Number of days of the year taking into account the leap year
    """
        
    fmt='%Y-%m-%d'
    sdtdate = datetime.datetime.strptime(stddate, fmt)
    sdtdate = sdtdate.timetuple()
    jdate = sdtdate.tm_yday
    return(jdate)

# Check_standard_date_to_Julian_day----- Mentioned on the site
# print(standard_date_to_Julian_day('2018-11-01'))