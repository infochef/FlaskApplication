from flask import Flask
from flask_restful import Resource, Api

rest = Flask(__name__)

api = Api(rest)


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    rest.run(debug=True)
