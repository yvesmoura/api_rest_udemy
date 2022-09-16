from flask import Flask
from flask_restful import Api
from resources.hotel import *
from resources.usuario import *
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' #se precisar mudar o banco de dados só mudar a variavel
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
api = Api(app)
jwt = JWTManager(app)

# antes da primeira requisição eercutar funcao abaixo
@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Hoteis, '/hoteis' )
api.add_resource(Hotel, '/hoteis/<string:hotel_id>' )
api.add_resource(User, '/usuarios/<int:user_id>' )
api.add_resource(UserRegister, '/cadastro' )
api.add_resource(UserLogin, '/login' )

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
