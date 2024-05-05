from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

puppies = []

class PuppyNames(Resource):

    def get(self, name):
        for pup in puppies:
            if pup['name'] == name:
                return pup

        # If you request a puppy not yet in the puppies list
        return {'name': None}, 404

    def post(self, name):
        pup = {'name':name}
        puppies.append(pup)
        return pup

    def delete(self, name):

        for ind,pup in enumerate (puppies):
            if pup['name'] == name:
                delted_pup = puppies.pop(ind)
                return {'note': 'delete successful'}


class AllNames(Resource):

    def get(self):
        # return all the puppies :)
        return {'puppies': puppies}


api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')

if __name__ == '__main__':
    app.run(debug=True)