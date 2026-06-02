from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'city parameter required'}), 400
    
    # Фейковые данные о погоде
    return jsonify({
        'city': city,
        'temperature': 22.5,
        'feels_like': 20.0,
        'humidity': 65,
        'description': 'Солнечно',
        'wind_speed': 3.2,
        'pressure': 1012,
        'mock': True
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)