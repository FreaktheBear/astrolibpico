# Created by: Freek den Beer
# Created on: 2025-04-19
# Description: This class converts alt-azimuth coordinates to hour angle and declination.

from math import sin, cos, asin, atan2, pi

class AltAz2HaDec:

    def __init__(self, alt=0.0, az=0.0, lat=0.0, ws=False):
        self.alt = alt
        self.az = az
        self.lat = lat
        self.ws = ws

    def convert_altaz2hadec(self):
        # Convert degrees to radians
        deg2rad = pi/180
        alt_r  = self.alt*deg2rad
        az_r = self.az*deg2rad
        if self.ws == True:
            az_r = (az_r + 180) % 360
        lat_r = self.lat*deg2rad

        # Find local HOUR ANGLE (in degrees, from 0. to 360.)
        ha = atan2( -sin(az_r)*cos(alt_r), -cos(az_r)*sin(lat_r)*cos(alt_r)+sin(alt_r)*cos(lat_r))
        ha = ha / deg2rad
        if ha < 0:
            ha = ha + 360
        ha = round(ha % 360, 4)

        # Find declination (positive if north of Celestial Equator, negative if south)
        sindec = sin(lat_r)*sin(alt_r) + cos(lat_r)*cos(alt_r)*cos(az_r)
        dec = round(asin(sindec)/deg2rad, 4)

        return(ha, dec)

