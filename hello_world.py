from flask import Flask
app = Flask(__name__)


# Modify the function output to return <h1>Hello World :)</h1> and
# return the program by pressing Ctrl+F5.
@app.route('/')
def hello_world():
    # return 'Hello World!'
    return '<h1>Hello World :)</h1>'


# Type 'greet' as the function name and route name (these can be different,
# but we'll keep them the same). Replace 'pass' with a simple return "Hello" statement.
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


# Create a new route so that you can enter Celsius values in the URL and see the
# Fahrenheit values in the Web page, like below.
@app.route('/f')
@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius=float(0)):
    """Convert celsius to fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return "{} celsius is equal to {} fahrenheit.".format(celsius, fahrenheit)


if __name__ == '__main__':
    app.run()
