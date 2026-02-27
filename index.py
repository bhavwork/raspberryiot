from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

LED = 17  # BCM pin number

# GPIO setup
GPIO.setwarnings(False)  # ignore warnings
GPIO.setmode(GPIO.BCM)   # use BCM numbering
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)  # LED starts OFF

# Home page with buttons
@app.route('/')
def home():
    return '''
    <h1>LED Control</h1>
    <a href="/on"><button>ON</button></a>
    <a href="/off"><button>OFF</button></a>
    <a href="/toggle"><button>TOGGLE</button></a>
    '''

# Turn LED ON
@app.route('/on')
def led_on():
    GPIO.output(LED, True)
    return "LED ON"

# Turn LED OFF
@app.route('/off')
def led_off():
    GPIO.output(LED, False)
    return "LED OFF"

# Toggle LED state
@app.route('/toggle')
def led_toggle():
    GPIO.output(LED, not GPIO.input(LED))
    return f"LED is now {'ON' if GPIO.input(LED) else 'OFF'}"

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()  # reset pins on exit
