# Created by: Freek den Beer
# Created on: 2025-04-20
# Description: This class converts degrees to degrees-minutes-seconds.
# For convertion of Altitude, Azimuth, Declination, and Latitude/longitude.
# (arc min and arc sec, not time based)

from math import modf

class Deg2DMS:

    def __init__(self, deg=0.0):
        self.deg = deg

    def convert_deg2dms(self):
        decimalminutes , degrees = modf(self.deg)
        degrees = int(degrees)
        minsec = decimalminutes*60
        decimalseconds, minutes = modf(minsec)
        minutes = int(minutes)
        seconds = round(decimalseconds*60,1)
        return (degrees, minutes, seconds)