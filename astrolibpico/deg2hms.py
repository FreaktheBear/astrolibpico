# Created by: Freek den Beer
# Created on: 2025-04-20
# Description: This class converts degrees to degrees-minutes-seconds.
# For convertion of hour angle, and right ascention.
# (time based)

from math import modf

class Deg2HMS:

    def __init__(self, deg=0.0):
        self.deg = deg

    def convert_deg2hms(self):
        decimalminutes , hours = modf(self.deg/15)
        hours = int(hours)
        minsec = decimalminutes*60
        decimalseconds, minutes = modf(minsec)
        minutes = int(minutes)
        seconds = round(decimalseconds*60,2)
        return (hours, minutes, seconds)
    