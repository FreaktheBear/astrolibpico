import time
import unittest
from astrolibpico.altaz2hadec import AltAz2HaDec
from astrolibpico.hadec2altaz import HaDec2AltAz
from astrolibpico.deg2dms import Deg2DMS
from astrolibpico.deg2hms import Deg2HMS
from astrolibpico.dms2deg import DMS2Deg
from astrolibpico.hms2deg import HMS2Deg
from astrolibpico.localsiderealtime import LocalSiderealTime

now_utc = time.gmtime()
''' time.localtime([secs])
    Convert the time secs expressed in seconds since the Epoch (see above) into an 8-tuple which contains:
    (year, month, mday, hour, minute, second, weekday, yearday)
    If secs is not provided or None, then the current time from the RTC is used.
    The gmtime() function returns a date-time tuple in UTC, and localtime() returns a date-time tuple in local time.
    The format of the entries in the 8-tuple are:
        year includes the century (for example 2014).
        month is 1-12
        mday is 1-31
        hour is 0-23
        minute is 0-59
        second is 0-59
        weekday is 0-6 for Mon-Sun
        yearday is 1-366

'''

class TestAltaz2Hadec(unittest.TestCase):
    def setUp(self):
        # Set up any necessary data or state before each test
        self.altitude = 5.1078  # degrees
        self.azimuth =  275.1336  # degrees
        self.latitude = -36.8540804  # degrees
        self.hour_angle = 82.8359  # degrees
        self.declination = 1.0272 # degrees
        self.ha_hms = (5, 31, 20.61)
        self.dec_dms = (1, 1, 37.9)
        self.ws = False
        self.year = now_utc[0]
        self.month = now_utc[1]
        self.day = now_utc[2]
        self.utc = now_utc[3] + now_utc[3]/60 + now_utc[5]/3600
        self.long = 0 

    def test_altaz2hadec(self):
        # Test the conversion from Alt/Az to HA/Dec
        hadec_venus = AltAz2HaDec(self.altitude, self.azimuth, self.latitude, self.ws)
        ha_venus, dec_venus = hadec_venus.convert_altaz2hadec()
        self.assertIsInstance(ha_venus, float)
        self.assertIsInstance(dec_venus, float)
        self.assertAlmostEqual(ha_venus, 82.8359, 2)
        self.assertAlmostEqual(dec_venus, 1.0272, 2)
    
    def test_hadec2altaz(self):
        # Test the conversion from HA/Dec to Alt/Az
        altaz_venus = HaDec2AltAz(self.hour_angle, self.declination, self.latitude, self.ws)
        alt_venus, az_venus = altaz_venus.convert_hadec2altaz()
        self.assertIsInstance(alt_venus, float)
        self.assertIsInstance(az_venus, float)
        self.assertAlmostEqual(alt_venus, 5.1078, 2)
        self.assertAlmostEqual(az_venus, 275.1336, 2)

    def test_deg2dms_conversion(self):
        # Test the conversion from degrees to DMS
        dms_converter = Deg2DMS(self.declination)
        degrees, minutes, seconds = dms_converter.convert_deg2dms()
        self.assertIsInstance(degrees, int)
        self.assertIsInstance(minutes, int)
        self.assertIsInstance(seconds, float)
        self.assertAlmostEqual(degrees, 1)
        self.assertAlmostEqual(minutes, 1)
        self.assertAlmostEqual(seconds, 37.9, 1)

    def test_deg2hms_conversion(self):
        # Test the conversion from degrees to HMS
        hms_converter = Deg2HMS(self.hour_angle)
        hours, minutes, seconds = hms_converter.convert_deg2hms()
        self.assertIsInstance(hours, int)
        self.assertIsInstance(minutes, int)
        self.assertIsInstance(seconds, float)
        self.assertAlmostEqual(hours, 5)
        self.assertAlmostEqual(minutes, 31)
        self.assertAlmostEqual(seconds, 20.61, 1)

    def test_dms2deg_conversion(self):
        # Test the conversion from DMS to degrees
        dms_converter = DMS2Deg(self.dec_dms[0], self.dec_dms[1], self.dec_dms[2])
        degrees = dms_converter.convert_dms2deg()
        self.assertIsInstance(degrees, float)
        self.assertAlmostEqual(degrees, 1.0272, 2)
    
    def test_hms2deg_conversion(self):
        # Test the conversion from HMS to degrees
        hms_converter = HMS2Deg(self.ha_hms[0], self.ha_hms[1], self.ha_hms[2])
        degrees = hms_converter.convert_hms2deg()
        self.assertIsInstance(degrees, float)
        self.assertAlmostEqual(degrees, 82.8359, 2)

    def test_sidereal_time(self):
        # Test the julian date and local mean sidereal time for UTC and GMT longitude
        # Check against any online sidereal time calculator
        lst = LocalSiderealTime(self.year, self.month, self.day, self.utc, self.long)
        jd, lmst = lst.sidereal_time()
        self.assertIsInstance(jd, float)
        self.assertIsInstance(lmst, float)
        lmst_h = int(lmst)
        lmst_m = int((lmst - lmst_h)*60)
        lmst_s = int((lmst - lmst_h - lmst_m/60)*3600)
        print(f"{lmst_h}h{lmst_m}m{lmst_s}s, Check against any online sidereal time calculator")
        print(f"With this UTC time and 0deg longitude, {now_utc[0]}y{now_utc[1]}m{now_utc[2]}d - {now_utc[3]}h{now_utc[4]}m{now_utc[3]}s")


if __name__ == '__main__':
    unittest.main()

'''
Venus values according to Stellarium:
2025-04-21 15:34:35 UTC+12:00
ws = False
lat = -36.8540804
Venus Altitude: 5.1078°
Venus Azimuth: 275.1336°
Venus Altitude in DMS: 5deg06m28.2s
Venus Azimuth in DMS: 275deg08m01.1s
Venus HA: 82.8359°
Venus DEC: 1.0272°
Venus HA in HMS: 5h31m20.61s
Venus DEC in DMS: 1deg1m37.9s

deg_alt = DMS2Deg(5, 6, 28.2)
alt = deg_alt.convert_dms2deg()
deg_az = DMS2Deg(275, 8, 1.1)
az = deg_az.convert_dms2deg()
deg_ha = HMS2Deg(5, 31, 20.61)
ha = deg_ha.convert_hms2deg()
deg_dec = DMS2Deg(1, 1, 37.9)
dec = deg_dec.convert_dms2deg()

print(f"alt: {alt} az: {az} ha: {ha} dec: {dec}")
# alt: 5.1078 az: 275.1331 ha: 82.9851 dec: 1.0272
'''