## hadec2altaz: Convert hour angle and declination to horizon (Alt-Az)...

[back to index](/Readme.md)

#### Description

Convert hour angle and declination to horizon (Alt-Az) coordinates.

#### Usage

hadec2altaz(ha, dec, lat, ws)

#### Arguments

**ha** (local apparent hour angle, in degrees)

**dec** (local apparent declination, in degrees)

**latitude** (local geodetic latitude, in degrees)

**ws** (if False, the output azimuth is measured East from North. If True, the output azimuth is measured West from South. (default=False))

#### Details

For outputs, the hour angle is the time that right ascension of 0 hours crosses the local meridian.

#### Return values

**alt** (local apparent altitude, in degrees)

**az** (local apparent altitude, in degrees, measured east-of-north, if you have measured azimuth west-of-south (like the book MEEUS does), set *ws=True*)

#### Author(s)

Written by Chris O'Dell Univ. of Wisconsin-Madison May 2002

Micropython adaptation by Freek den Beer Apr 2025

#### Examples

altaz2hadec(336.9155, 17.54789,41.3)  

Example output

(59.0861, 133.3081)

#### See Also

[- altaz2hadec: Convert horizon (Alt-Az) coordinates to hour angle and declination](manpages/altaz2hadec.md)