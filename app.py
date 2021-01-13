from flask import Flask
#from apis.covid import covid
from flask_restful import Api
from routes import initialize_routes
from flask_cors import CORS
#.register_blueprint(covid)

app = Flask(__name__)
api = Api(app)
CORS(app)


#@app.route('/')
#def hello_world():
#   return 'Hola'

initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
