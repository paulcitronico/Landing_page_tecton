from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'tecton-secret-key-2025')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    nombre = data.get('nombre', '')
    email = data.get('email', '')
    telefono = data.get('telefono', '')
    mensaje = data.get('mensaje', '')

    # Acá podés integrar envío de email, base de datos, etc.
    print(f"Contacto recibido: {nombre} | {email} | {telefono} | {mensaje}")

    return jsonify({
        'status': 'success',
        'message': 'Mensaje recibido correctamente. Nos pondremos en contacto.'
    })


@app.errorhandler(404)
def not_found(e):
    return render_template('index.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)