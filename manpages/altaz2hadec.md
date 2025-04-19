## altaz2hadec: Convert horizon (Alt-Az) coordinates to hour angle and...

[back to index](/Readme.md)

#### Description

Convert horizon (Alt-Az) coordinates to hour angle and declination.

#### Usage

altaz2hadec(alt, az, lat, ws)

#### Arguments

**alt** (local apparent altitude, in degrees)

**az** (local apparent altitude, in degrees, measured east-of-north)

**latitude** (local geodetic latitude, in degrees)

**ws** (if you have measured azimuth west-of-south, like the book MEEUS does, set *ws=True*)

#### Details

For outputs, the hour angle is the time that right ascension of 0 hours crosses the local meridian.

#### Return values

**ha** (local apparent hour angle, in degrees)

**dec** (local apparent declination, in degrees)

#### Author(s)

Written by Chris O'Dell Univ. of Wisconsin-Madison May 2002

Micropython adaptation by Freek den Beer Apr 2025

#### Example(s)

altaz2hadec(59.0861, 133.3081, 41.3)  

Example output

(336.9155, 17.54789)

#### See also

[- hadec2altaz: Convert hour angle and declination to horizon (Alt-Az) coordinates](altaz2hadec.md)
