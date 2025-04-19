# Created by: Freek den Beer
# Created on: 2025-04-19
# Description: This class converts alt-azimuth coordinates to hour angle and declination.
# This class is adopted from the astrolibR library and converted for MicroPython.
# License: MIT

from math import sin, cos, asin, atan2, pi

class AltAz2HaDec:

    def __init__(self, az=0, alt=0, lat=0, ws=False):
        self.az = az
        self.alt = alt
        self.lat = lat
        self.ws = ws
    
    def convert_altaz2hadec(self):
        deg2rad = pi/180
        alt_r  = self.alt*deg2rad
        if self.ws == True:
            self.az = (self.az + 180) % 360
        az_r = self.az*deg2rad
        lat_r = self.lat*deg2rad
        ha = atan2( -sin(az_r)*cos(alt_r), -cos(az_r)*sin(lat_r)*cos(alt_r)+sin(alt_r)*cos(lat_r))
        ha = ha / deg2rad
        if ha < 0:
            ha = ha + 360
        ha = ha % 360
        sindec = sin(lat_r)*sin(alt_r) + cos(lat_r)*cos(alt_r)*cos(az_r)
        dec = asin(sindec)/deg2rad
        return(ha, dec)