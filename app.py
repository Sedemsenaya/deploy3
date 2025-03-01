from flask import Flask, send_from_directory
from flask_cors import CORS,cross_origin

app = Flask(__name__, static_folder='my-app/build', static_url_path='')
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})


@app.route('/api', methods=['GET'])
@cross_origin()
def index():
    return {
        "tutorial": "Flask React Heroku Deployment from Backend"
    }


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()