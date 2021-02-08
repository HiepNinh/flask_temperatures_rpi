from flask import render_template, Blueprint
import board
import adafruit_dht


lab_temp = Blueprint('lab_temp', __name__)


@lab_temp.route("/latest_measure")
def latest_measure():
   try:
      dhtDevice = adafruit_dht.DHT22(board.D17, use_pulseio = False)
      temperature = dhtDevice.temperature
      humidity = dhtDevice.humidity
      if humidity is not None and temperature is not None:
         return render_template("lab_temps/lab_temp.html",temp=temperature,hum=humidity, title="Lab Conditions by RPi")
      else:
            return render_template("errors/no_sensor.html")
   except:
      return render_template("errors/no_sensor.html")


@lab_temp.route("/monitor_history")
def monitor_history():
	conn=sqlite3.connect('/var/www/lab_app/database/data/lab_app.db')
	curs=conn.cursor()
	curs.execute("SELECT * FROM temperatures where sensorID != 0")
	temperatures = curs.fetchall()
	curs.execute("SELECT * FROM humidities where sensorID != 0")
	humidities = curs.fetchall()
	conn.close()
	return render_template("lab_env_db.html",temp=temperatures,hum=humidities)
