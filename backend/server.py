from flask import Flask
from runner import Connection

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    return "{'positioning_system': {'speed': 44, 'location': {'lat': 57.71118333, 'lng': 11.64737}, 'heading': 126}, 'battery_level': 0, 'cooling': {'coolant_temp': 64}, 'locks': {'hood': True, 'trunk': True, 'doors': True}, 'instrument': {'vehicle_speed': 40}, 'fuel_system': {'fuel_level': 0, 'fuel_consumption_avg': 9.6, 'fuel_consumption_journey': 0}, 'lighting': {'exterior': {'signal_right': False, 'reverse': False, 'signal_left': False, 'fog': False, 'side': False, 'main': False}}, 'engine': {'rpm': 1610, 'intake': {'air_temp': 2, 'air_flow_rate': 45}, 'ecu_voltage': 14, 'mil': {'status': 'off'}, 'runtime': 187, 'ignition': 'on', 'load': 0, 'throttle_position': 20}}"


if __name__ == '__main__':
    app.run(threaded=True)
    c = Connection()
    c.start()
