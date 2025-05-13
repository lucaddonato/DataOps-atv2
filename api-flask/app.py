from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger UI config
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={})
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Rota para soma
@app.route('/soma', methods=['POST'])
def soma():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({'error': 'Faltando número(s)'}), 400
    result = num1 + num2
    return jsonify({'result': result})

# Rota para multiplicação
@app.route('/multiplicacao', methods=['POST'])
def multiplicacao():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({'error': 'Faltando número(s)'}), 400
    result = num1 * num2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)