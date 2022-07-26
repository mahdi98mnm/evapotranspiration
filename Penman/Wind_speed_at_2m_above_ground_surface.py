import math


def wind_speed_at_2m_above_ground_surface(
    Altitude_at_which_wind_speed_is_measured : float, 
    Measured_wind_speed : float
) -> float:

        """
        Description
        -----------
        calculate Wind speed at 2m above ground surface with Measured speed and height - eq 47 FAO56
        ----------
        
        Altitude_at_which_wind_speed_is_measured : float
            Altitude at which wind speed is measured in meter
        Measured_wind_speed : float 
            Measured wind speed in meter / second
            
        Returns
        -------
        Wind speed at 2m above ground surface : float
            Wind speed at 2m above ground surface in meter / second
        """
        
        return Measured_wind_speed * (4.87 / (math.log((67.8 *Altitude_at_which_wind_speed_is_measured) - 5.42)))


# Check_Calculate Wind speed at 2m above ground surface ----- page56 EX14 FAO56
# print(wind_speed_at_2m_above_ground_surface(Altitude_at_which_wind_speed_is_measured = 10 ,Measured_wind_speed = 3.2))
