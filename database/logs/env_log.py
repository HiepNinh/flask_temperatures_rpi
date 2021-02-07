import sqlite3
import sys
import board
import adafruit_dht

def log_values(sensor_id, temp, hum):
	conn=sqlite3.connect('/var/www/lab_app/database/data/lab_app.db')  #It is important to provide an
							     #absolute path to the database
							     #file, otherwise Cron won't be
							     #able to find it!
	# For the time-related code (record timestamps and time-date calculations) to work 
	# correctly, it is important to ensure that your Raspberry Pi is set to UTC.
	# This is done by default!
	# In general, servers are assumed to be in UTC.
	curs=conn.cursor()
	curs.execute("""INSERT INTO temperatures values(datetime(CURRENT_TIMESTAMP, 'localtime'),
         (?), (?))""", (sensor_id,temp))
	curs.execute("""INSERT INTO humidities values(datetime(CURRENT_TIMESTAMP, 'localtime'),
         (?), (?))""", (sensor_id,hum))
	conn.commit()
	conn.close()

try:
    dhtDevice = adafruit_dht.DHT22(board.D17, use_pulseio = False)
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity
    if humidity is not None and temperature is not None:
        log_values("1", temperature, humidity)
    else:
        log_values("0", -999, -999)
except Exception:
    log_values("0", -999, -999)