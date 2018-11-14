# ---------------------------------- app.py ---------------------------------- #

# Autora: Gema Correa Fernández

'''
Fichero que implementa la clase API REST haciendo uso del microframework Flask
'''


# Bibliotecas a usar
from flask import Flask     # importamos la clase Flask
from flask import jsonify   # https://pypi.org/project/Flask-Jsonpify/
from flask import request   # https://github.com/requests/requests

from util import *          # importar el fichero util.py

# Creación de una instancia de la clase Flask
app = Flask(__name__)


# Definimos nuestra clase
class TwitterData:

# ---------------------------------------------------------------------------- #

    # Ruta para comprobar que se ha desplegado de forma correcta
    @app.route('/')
    def index():
        return jsonify(status='OK') # devolvemos { "status": "OK" }

# ---------------------------------------------------------------------------- #

    # Mostrar un 404, cuando se ha desplegado de forma incorrecta
    # Código de estado HTTP: https://developer.mozilla.org/es/docs/Web/HTTP/Status
    @app.errorhandler(404)
    def not_found(error):
        data = {} # definimos un diccionario
        data['status'] = 'ERROR 404'

        # jsonify: convierte la salida JSON en un objeto Response con
        # la aplication/json mimetype
        result = jsonify(data)

        # Se modifica el código de estado de la respuesta a 404
        # 404: Recurso no encontrado, el servidor web no encuentra la página
        # http://docs.python-requests.org/en/master/user/quickstart/
        result.status_code = 404

        return result # devolvemos { "status": "ERROR 404" }

# ---------------------------------------------------------------------------- #

    # Función para visualizar todos los elementos (MÉTODO GET)
    # GET para obtener un recurso del servidor
    @app.route('/data_twitter', methods=['GET'])
    def get_all_data():
        data = {} # definimos un diccionario
        # No hace falta añadir al diccionario --> data['status'] = 'OK'
        data['ruta'] = request.url # obtener la url de la petición
        data['valor'] = get_data_twitter()

        # jsonify: convierte la salida JSON en un objeto Response con
        # la aplication/json mimetype
        result = jsonify(data)

        # Se modifica el código de estado de la respuesta a 200
        # 200: Respuesta estándar para peticiones correctas
        result.status_code = 200

        return result

# ---------------------------------------------------------------------------- #

    # Función para visualizar un solo un elemento del JSON (MÉTODO GET)
    # GET para obtener un recurso del servidor
    @app.route('/get_data', methods=['GET'])
    def get_data():
        if 'id' in request.args:

            # Si está el ID, muestra el elemento correspondiente
            if request.args['id'] in data_twitter:
                data = {} # definimos un diccionario
                # No hace falta añadir al diccionario --> data['status'] = 'OK'
                data['ruta'] = request.url # obtener la url de la petición
                data['valor'] = get_id_data_twitter(request.args['id'])

            else: # Si no está el ID
                data = "El ID no existe, tiene que ser GR, MDR o VLC"

        else: # Si no sabemos como escribirlo
            data = "Ejemplo: http://127.0.0.1:5000/get_data?id=GR"

        # jsonify: convierte la salida JSON en un objeto Response con
        # la aplication/json mimetype.
        result = jsonify(data)

        # Se modifica el código de estado de la respuesta a 200
        # 200: Respuesta estándar para peticiones correctas
        result.status_code = 200

        return result

# ---------------------------------------------------------------------------- #

    # Editar el nombre del usuario del JSON (MÉTODO PUT)
    # PUT para actualizar un recurso del servidor
    @app.route('/put_data', methods=['GET','PUT'])
    def put_data():
        if all (arg in request.args for arg in ('id', 'name', 'user')):

            # Si está el ID-name-user, edita el elemento correspondiente
            if request.args['id'] in data_twitter:
                update_data_twitter(request.args['id'], request.args['name'],
                                    request.args['user'])

                data = {} # definimos un diccionario
                # No hace falta añadir al diccionario --> data['status'] = 'OK'
                data['ruta'] = request.url # obtener la url de la petición
                data['valor'] = get_id_data_twitter(request.args['id'])

            else: # Si no está el ID
                data =  "El ID no existe, tiene que ser GR, MDR o VLC"

        else: # Si no sabemos como escribirlo
            data = "Ejemplo: http://127.0.0.1:5000/put_data?name=name&user=SEVILLA&id=GR"

        # jsonify: convierte la salida JSON en un objeto Response con
        # la aplication/json mimetype.
        result = jsonify(data)

        # Se modifica el código de estado de la respuesta a 200
        # 200: Respuesta estándar para peticiones correctas
        result.status_code = 200

        return result

# ---------------------------------------------------------------------------- #

    # Añadir un elemento al JSON (MÉTODO POST)
    # POST para actualizar un recurso del servidor
    @app.route('/post_data', methods=['GET','POST'])
    def post_data():
        # nos creamos un nuevo elemento
        new_data = {"ML": [{ "name":"@malaga",
                     "url_twitter":"https://twitter.com/malaga",
                     "user_twitter":"@malaga"
                    }]}

        # añadimos el nuevo elemento al conjunto de elementos
        new_data_twitter = add_data_twitter(new_data)

        data = {} # definimos un diccionario
        # No hace falta añadir al diccionario --> data['status'] = 'OK'
        data['ruta'] = request.url # obtener la url de la petición
        data['valor'] = new_data

        # jsonify: convierte la salida JSON en un objeto Response con
        # la aplication/json mimetype.
        result = jsonify(data)

        # Se modifica el código de estado de la respuesta a 200
        # 200: Respuesta estándar para peticiones correctas
        result.status_code = 200

        return result

# ---------------------------------------------------------------------------- #

    # Borrar un elemento del JSON (MÉTODO DELETE)
    # DELETE para eliminar un recurso del servidor
    @app.route('/delete_data', methods=['GET','DELETE'])
    def delete_data():
        if 'id' in request.args:

            # Si está el ID, borra el elemento correspondiente
            if request.args['id'] in data_twitter:
                remove_data_twitter(request.args['id'])
                data = {} # definimos un diccionario
                # No hace falta añadir al diccionario --> data['status'] = 'OK'
                data['ruta'] = request.url # obtener la url de la petición
                data['valor'] = get_id_data_twitter(request.args['id'])

            else: # Si no está el ID
                data =  "El ID no existe o se ha borrado, tiene que ser GR, MDR o VLC"

        else: # Si no sabemos como escribirlo
            data = "Ejemplo: http://127.0.0.1:5000/delete_data?id=GR"

        # jsonify: convierte la salida JSON en un objeto Response con
        # la aplication/json mimetype.
        result = jsonify(data)

        # Se modifica el código de estado de la respuesta a 200
        # 200: Respuesta estándar para peticiones correctas
        result.status_code = 200

        return result
# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host="0.0.0.0", port=port,debug=True)
    app.run(debug=True, port = 5000)
