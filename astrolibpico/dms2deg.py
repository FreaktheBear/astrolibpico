# Created by: Freek den Beer
# Created on: 2025-04-20
# Description: This class converts degrees-minutes-seconds to degrees.
# For convertion of Altitude, Azimuth, Declination, and Latitude/longitude.
# (arc min and arc sec, not time based)

from math import modf

class DMS2Deg:

    def __init__(self, deg=0.0, min=0.0, sec=0.0):
        self.deg = deg
        self.min = min
        self.sec = sec

    def convert_dms2deg(self):
        sign = -1 if self.deg < 0 else 1
        degrees = round(sign * (abs(self.deg) + self.min / 60 + self.sec / 3600),4)
        return degrees
    

        
