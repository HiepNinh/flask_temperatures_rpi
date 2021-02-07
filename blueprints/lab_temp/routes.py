from flask import render_template, Blueprint
import board
import adafruit_dht


lab_temp = Blueprint('lab_temp', __name__)


@lab_temp.route("/lab_temp")
def show_lab_temp():
   try:
      dhtDevice = adafruit_dht.DHT22(board.D17)
      temperature = dhtDevice.temperature
      humidity = dhtDevice.humidity
      if humidity is not None and temperature is not None:
         return render_template("lab_temps/lab_temp.html",temp=temperature,hum=humidity)
      else:
       	 return render_template("errors/no_sensor.html")
   except:
      return render_template("errors/no_sensor.html")