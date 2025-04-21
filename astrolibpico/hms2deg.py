# Created by: Freek den Beer
# Created on: 2025-04-20
# Description: This class converts degrees-minutes-seconds to degrees.
# For convertion of hour angle, and right ascention.
# (time based)

class HMS2Deg:

    def __init__(self, hrs=0.0, min=0.0, sec=0.0):
        self.hrs = hrs
        self.min = min
        self.sec = sec

    def convert_hms2deg(self):
        degrees = round(15 * (self.hrs + self.min / 60 + self.sec / 3600),4)
        return degrees