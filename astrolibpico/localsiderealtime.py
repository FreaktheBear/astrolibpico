# Created by: Freek den Beer
# Created on: 2025-04-22
# Description: This class calculates and returns julian date, and sidereal time.
# Adopted from https://www.nies.ch/doc/astro/sternzeit.en.php

class LocalSiderealTime:
    def __init__(self, year=0, month=0, day=0, utc=0, long=0):
        self.year = year
        self.month = month
        self.day = day
        self.utc = utc
        self.long = long

    def sidereal_time(self):
        """
        Returns the Julian date, number of days since 1 January 4713 BC 12:00.
        utc is UTC in decimal hours. If utc=0, returns the date at 12:00 UTC.
        """
        if self.month > 2:
            y = self.year
            m = self.month
        else:
            y = self.year - 1
            m = self.month + 12
        d = self.day
        h = self.utc/24
        if self.year <= 1582 and self.month <= 10 and self.day <= 4:
            # Julian calendar
            b = 0
        elif self.year == 1582 and self.month == 10 and self.day > 4 and self.day < 15:
            # Gregorian calendar reform: 10 days (5 to 14 October 1582) were skipped.
            # In 1582 after 4 October follows the 15 October.
            d = 15
            b = -10
        else:
            # Gregorian Calendar
            a = int(y/100)
            b = 2 - a + int(a/4)
        jd = int(365.25*(y+4716)) + int(30.6001*(m+1)) + d + h + b - 1524.5

        """
        Returns the sidereal time in decimal hours. Longitude (long) is in 
        decimal degrees. If long=0, return value is Greenwich Mean Sidereal Time 
        (GMST).
        """
        t = (jd - 2451545.0)/36525
        # Greenwich siderial time at 0h UTC (hours)
        st = (24110.54841 + 8640184.812866 * t +
            0.093104 * t**2 - 0.0000062 * t**3) / 3600
        # Greenwich sidereal time at given UTC
        st = st + 1.00273790935*self.utc
        # Local sidereal time at given UTC (longitude in degrees)
        st = st + self.long/15
        st = st % 24
        return(jd, st)
