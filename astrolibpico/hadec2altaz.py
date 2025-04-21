# Created by: Freek den Beer
# Created on: 2025-04-19
# Description: This class converts hour angle and declination to alt-azimuth coordinates.

from math import sin, cos, atan2, pi, sqrt
    
class HaDec2AltAz:

    def __init__(self, ha=0.0, dec=0.0, lat=0.0, ws=False):
        self.ha = ha
        self.dec = dec
        self.lat = lat
        self.ws = ws
    
    def convert_hadec2altaz(self):
        deg2rad = pi/180
        sh = sin(self.ha*deg2rad)
        ch = cos(self.ha*deg2rad)
        sd = sin(self.dec*deg2rad)
        cd = cos(self.dec*deg2rad)
        sl = sin(self.lat*deg2rad)
        cl = cos(self.lat*deg2rad)
        x = - ch * cd * sl + sd * cl
        y = - sh * cd
        z = ch * cd * cl + sd * sl
        r = sqrt(x**2 + y**2)
        alt = atan2(z,r) / deg2rad
        az = atan2(y,x) / deg2rad
        if az < 0:
            az = az + 360
        if self.ws == True:
            az = (az + 180) % 360
        az = round(az, 4)
        alt = round(alt, 4)
        return(alt, az)