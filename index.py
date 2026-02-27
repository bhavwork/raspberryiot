from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

LED1 = 17   # First LED
LED2 = 27   # Second LED

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)

@app.route('/')
def home():
    return '''
    <h1>2 LED Control</h1>
    <h2>LED 1</h2>
    <a href="/led1/on"><button>LED1 ON</button></a>
    <a href="/led1/off"><button>LED1 OFF</button></a>
    <a href="/led1/toggle"><button>LED1 TOGGLE</button></a>
    
    <h2>LED 2</h2>
    <a href="/led2/on"><button>LED2 ON</button></a>
    <a href="/led2/off"><button>LED2 OFF</button></a>
    <a href="/led2/toggle"><button>LED2 TOGGLE</button></a>
    '''

# -------- LED 1 --------
@app.route('/led1/on')
def led1_on():
    GPIO.output(LED1, True)
    return "LED1 ON"

@app.route('/led1/off')
def led1_off():
    GPIO.output(LED1, False)
    return "LED1 OFF"

@app.route('/led1/toggle')
def led1_toggle():
    GPIO.output(LED1, not GPIO.input(LED1))
    return f"LED1 is now {'ON' if GPIO.input(LED1) else 'OFF'}"


# -------- LED 2 --------
@app.route('/led2/on')
def led2_on():
    GPIO.output(LED2, True)
    return "LED2 ON"

@app.route('/led2/off')
def led2_off():
    GPIO.output(LED2, False)
    return "LED2 OFF"

@app.route('/led2/toggle')
def led2_toggle():
    GPIO.output(LED2, not GPIO.input(LED2))
    return f"LED2 is now {'ON' if GPIO.input(LED2) else 'OFF'}"


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()
