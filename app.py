from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')
    client_ip = request.remote_addr

    # Get the location of the client
    location_response = requests.get(f'http://ip-api.com/json/{client_ip}')
    location_data = location_response.json()
    city = location_data.get('city', 'Unknown location')

    # Get the weather information
    api_key = 'd5cc5e9db07426b3722c819726b11853'
    weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
    weather_data = weather_response.json()
    temperature = weather_data['main']['temp']

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"

    return jsonify({
        'client_ip': client_ip,
        'location': city,
        'greeting': greeting
    })

if __name__ == '__main__':
    app.run(debug=True)
