from flask import Flask, jsonify, abort
from flask_restful import Resource, Api
import csv, json

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return '''This is an API of all programming languages ever existed

Go to api/v1/programming_languages to view whole API
Go to api/v1/programming_languages/<name> to view the wiki link of the specified programming languages
'''

class LanguageList(Resource):
    def get(self):
        languages = csv.DictReader(open("languages.csv"))
        if languages==0:
            abort(404)
        return json.dumps(list(languages))

class Languages(Resource):
    def get(self, name):
        languages = csv.DictReader(open("languages.csv"))
        language = [language for language in languages if language['name'].lower()==name.lower()]
        if len(language)==0:
            abort(404)
        return jsonify({"languages":language})

api.add_resource(LanguageList,'/api/v1/programming_languages')    
api.add_resource(Languages,'/api/v1/programming_languages/<string:name>')
if __name__ == '__main__':
    app.run(debug=True)