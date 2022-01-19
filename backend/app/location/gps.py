import time, sys, os, datetime
import app.api.gps_crud as gps_crud
import app.api.activity_crud as activity_crud
from app.api.models import GpsReadingSchema
import sqlalchemy as db

try:
    import board
    import adafruit_gps
except RuntimeError as e:
    print("GPS not available: {}".format(e))
    sys.exit(1)

UPDATE_RATE = os.environ.get('UPDATE_RATE', 1)

def format_dop(dop):
    # https://en.wikipedia.org/wiki/Dilution_of_precision_(navigation)
    if dop > 20:
        msg = "Poor"
    elif dop > 10:
        msg = "Fair"
    elif dop > 5:
        msg = "Moderate"
    elif dop > 2:
        msg = "Good"
    elif dop > 1:
        msg = "Excellent"
    else:
        msg = "Ideal"
    return f"{dop} - {msg}"

def _format_datetime(datetime):
    return "{:02}/{:02}/{} {:02}:{:02}:{:02}".format(
        datetime.tm_mon,
        datetime.tm_mday,
        datetime.tm_year,
        datetime.tm_hour,
        datetime.tm_min,
        datetime.tm_sec,
    )

class Location:
    def __init__(self):
        self.fix = False
        self.fix_3d = False
        self.latitude = None
        self.longitude = None
        self.altitude = None
        self.speed = None
        self.timestamp = time.localtime()
        DATABASE_URL = os.getenv("DATABASE_URL")
        engine = db.create_engine(DATABASE_URL)
        self.connection = engine.connect()
        metadata = db.MetaData()
        self.activities = db.Table('activities', metadata, autoload=True, autoload_with=engine)
        self.gps_readings = db.Table('gps_readings', metadata, autoload=True, autoload_with=engine)

        # Todo: make i2c bus configurable
        i2c = board.I2C()
        # Create a GPS module instance.
        self.gps = adafruit_gps.GPS_GtopI2C(i2c, debug=False)  # Use I2C interface
        # Turn on everything (not all of it is parsed!)
        self.gps.send_command(b"PMTK314,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        # Set update rate to once a second (1hz) which is what you typically want.
        self.gps.send_command(b"PMTK220,1000")
    
    def get(self):
        '''Getter for the location attributes'''
        return {"fix": self.fix, "fix_3d": self.fix_3d, "latitude": self.latitude, "longitude": self.longitude, "altitude": self.altitude}

    def monitor_gps(self, event):
        '''Read in NMEA sentences and update location instance attributes'''
        last_print = time.monotonic()
        while True:
            if event.is_set():
                print("GPS event set")
                break
            # Make sure to call gps.update() every loop iteration and at least twice
            # as fast as data comes from the GPS unit (usually every second).
            # This returns a bool that's true if it parsed new data
            if not self.gps.update(): #or not self.gps.has_fix:
                time.sleep(0.2)
                continue
            # print(self.gps.nmea_sentence)
            # Every second print out current location details if there's a fix.
            current = time.monotonic()
            if current - last_print >= UPDATE_RATE:
                last_print = current
                if self.gps.has_fix:
                    if self.gps.nmea_sentence[3:6] == "GSA":
                        print(f"{self.gps.latitude:.6f}, {self.gps.longitude:.6f} {self.gps.altitude_m}m")
                        print(f"2D Fix: {self.gps.has_fix}  3D Fix: {self.gps.has_3d_fix}")
                        print(f"  PDOP (Position Dilution of Precision): {format_dop(self.gps.pdop)}")
                        print(f"  HDOP (Horizontal Dilution of Precision): {format_dop(self.gps.hdop)}")
                        print(f"  VDOP (Vertical Dilution of Precision): {format_dop(self.gps.vdop)}")
                        # Time & date from GPS informations
                        print("Fix timestamp: {}".format(_format_datetime(self.gps.timestamp_utc)))
                        self.fix = self.gps.has_fix
                        self.fix_3d = self.gps.has_3d_fix
                        self.latitude = self.gps.latitude
                        self.longitude = self.gps.longitude
                        self.altitude = self.gps.altitude_m
                        self.timestamp = self.gps.timestamp_utc
                        # self.speed = self.gps.speed_knots * 1.852
    
                        print("Reading GPS")
                        # Check that we have an active ride going on
                        query = db.select([self.activities]).where(self.activities.columns.active == True)
                        result = self.connection.execute(query)
                        current_activity = result.fetchone()
                        if current_activity is None:
                            print("No active ride. Not recording")
                        else:
                            current_activity_id = current_activity['id']
                            print("Current Activity ID: ", current_activity_id)
                            # Insert into DB with raw sqlachemy query because couldn't get it to
                            # work with the asyncio crud stuff.
                            query = db.insert(self.gps_readings).values(
                                activity_id=current_activity['id'],
                                latitude=self.gps.latitude,
                                longitude=self.gps.longitude,
                                timestamp=datetime.datetime.now(),
                                speed= self.gps.speed_knots*1.852 if self.gps.speed_knots is not None else 0,
                                altitude=self.gps.altitude_m,
                            )
                            self.connection.execute(query)
                else:
                    print("No GPS fix")
                    self.fix = False
            
        print("GPS thread stopped")