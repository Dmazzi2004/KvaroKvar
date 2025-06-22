from flask import Flask
from baza import db
from API import kvar_blueprint

app = Flask(__name__)
app.register_blueprint(kvar_blueprint)

db.bind(provider='sqlite', filename='kvarovi.db', create_db=True)
db.generate_mapping(create_tables=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')