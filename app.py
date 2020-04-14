from flask_restful import Resource, Api
from flask import Flask, Response, json, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/crud_flask'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

#saeful Imam Gunawan - 18090039 - 4A

# Awal Pertemuan 3

@app.route('/')
def hello_world():
    return 'Nama Saya Saeful Saya tinggal tegal'


@app.route('/admin')
def admin_page():
    return 'Selamat Datand di halaman admin, ada yang bisa saya bantu?'


# Akhir Pertemuan 3


# Awal Pertemuan 4

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/helloworld')


# Akhir Pertemuan 4

# Awal Pertemuan 5
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.String(8), unique=True)
    nama_mahasiswa = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, nim, nama_mahasiswa, email):
        self.nim = nim
        self.nama_mahasiswa = nama_mahasiswa
        self.email = email

    @staticmethod
    def get_all_users():
        return User.query.all()


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('nim', 'nama_mahasiswa', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.get_all_users()
    result = users_schema.dump(all_users)
    return jsonify(result)


# Akhir Pertemuan 5

if __name__ == '__main__':
    app.run()
