# Autora: Gema Correa Fernández
# http://blog.luisrei.com/articles/flaskrest.html


# Enlaces de interés

# 1. How to return a success status code:
#  https://stackoverflow.com/questions/26079754/flask-how-to-return-a-success-status-code-for-ajax-call
# https://blog.nearsoftjobs.com/crear-un-api-y-una-aplicación-web-con-flask-6a76b8bf5383

# Bibliotecas a importar
from flask import Flask     # para usar el microframework Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

class Twitter:

    # Check that it has been deployed correctly
    @app.route('/')
    def index():
        return jsonify(status='OK')

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
