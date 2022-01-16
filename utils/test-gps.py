import time, os, datetime
import board
import busio
import adafruit_gps
import sqlalchemy as db

UPDATE_RATE = os.environ.get('UPDATE_RATE', 1)
DATABASE_URL = os.getenv("DATABASE_URL")
engine = db.create_engine(DATABASE_URL)
connection = engine.connect()
metadata = db.MetaData()
activities = db.Table('activities', metadata, autoload=True, autoload_with=engine)
gps_readings = db.Table('gps_readings', metadata, autoload=True, autoload_with=engine)

# If using I2C, we'll create an I2C interface to talk to using default pins
i2c = board.I2C()

# Create a GPS module instance.
gps = adafruit_gps.GPS_GtopI2C(i2c, debug=False)  # Use I2C interface

# Initialize the GPS module by changing what data it sends and at what rate.
# Turn on everything (not all of it is parsed!)
gps.send_command(b'PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0')

# Set update rate to once a second (1hz) which is what you typically want.
gps.send_command(b"PMTK220,1000")

# Main loop runs forever printing the location, etc. every second.
last_print = time.monotonic()
while True:
    # Make sure to call gps.update() every loop iteration and at least twice
    # as fast as data comes from the GPS unit (usually every second).
    gps.update()
    # Every second print out current location details if there's a fix.
    current = time.monotonic()
    if current - last_print >= UPDATE_RATE:
        last_print = current
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print("Waiting for GPS fix...")
            continue
        # We have a fix! (gps.has_fix is true)
        # Print out details about the fix like location, date, etc.
        print("=" * 40)  # Print a separator line.
        print(
            "Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(
                gps.timestamp_utc.tm_mon,  # Grab parts of the time from the
                gps.timestamp_utc.tm_mday,  # struct_time object that holds
                gps.timestamp_utc.tm_year,  # the fix time.  Note you might
                gps.timestamp_utc.tm_hour,  # not get all data like year, day,
                gps.timestamp_utc.tm_min,  # month!
                gps.timestamp_utc.tm_sec,
            )
        )
        print("Latitude: {0:.6f} degrees".format(gps.latitude))
        print("Longitude: {0:.6f} degrees".format(gps.longitude))
        print("Fix quality: {}".format(gps.fix_quality))
        # Some attributes beyond latitude, longitude and timestamp are optional
        # and might not be present.  Check if they're None before trying to use!
        if gps.satellites is not None:
            print("# satellites: {}".format(gps.satellites))
        if gps.altitude_m is not None:
            print("Altitude: {} meters".format(gps.altitude_m))
        if gps.speed_knots is not None:
            print("Speed: {} knots".format(gps.speed_knots))
        if gps.track_angle_deg is not None:
            print("Track angle: {} degrees".format(gps.track_angle_deg))
        if gps.horizontal_dilution is not None:
            print("Horizontal dilution: {}".format(gps.horizontal_dilution))
        if gps.height_geoid is not None:
            print("Height geoid: {} meters".format(gps.height_geoid))
        
        query = db.select([activities]).where(activities.columns.active == True)
        result = connection.execute(query)
        current_activity = result.fetchone()
        
        if current_activity is not None:
            print("Current activity: {}".format(current_activity['id']))
            query = db.insert(gps_readings).values(
                activity_id=current_activity['id'],
                latitude=gps.latitude,
                longitude=gps.longitude,
                timestamp=datetime.datetime.now(),
                speed=gps.speed_knots*1.852,
                altitude=gps.altitude_m,
            )
            connection.execute(query)
        else:
            print("No active activity")