# ---------------------------------- logger.py --------------------------------- #

# Con ayuda de: https://ricveal.com/blog/curso-python-5/

# Bibliotecas a usar
import logging  # http://flask.pocoo.org/docs/1.0/logging/

'''
Fichero que configura un único logger que maneja eventos de dos formas diferentes:
guardándolo en un archivo si la traza es de nivel DEBUG o superior y sacándolo
por pantalla en el mismo caso.
'''
def logger():

    # http://flask.pocoo.org/docs/0.12/errorhandling/
    # Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
    log = logging.Logger("app")

    # FileHandler
    # Guardar los logs en el archivo debug.log si la traza es de nivel DEBUG o superior
    filehandler = logging.FileHandler('debug.log')
    filehandler.setLevel(logging.DEBUG)

    # ConsoleHandler
    # Mostrar los logs por pantalla en el caso de que la traza sea de nivel DEBUG o superior
    consolehandler = logging.StreamHandler()
    consolehandler.setLevel(logging.DEBUG)

    # Modificar el formato (http://flask.pocoo.org/docs/1.0/logging/)
    # Para que aparezca la fecha, el nombre de la app, el nivel del mensaje y el mensaje
    format = logging.Formatter( '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler.setFormatter(format)
    consolehandler.setFormatter(format)

    # Añadimos los mensajes tanto a la consola como al archivo
    log.addHandler(filehandler)
    log.addHandler(consolehandler)

    return log
