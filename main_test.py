# -------------------------------- app_test.py ------------------------------- #

# Autora: Gema Correa Fernández

'''
Fichero que testea la clase de app.py
'''


# Bibliotecas a usar
import unittest     # https://docs.python.org/3/library/unittest.html
# https://www.blog.pythonlibrary.org/2016/07/07/python-3-testing-an-intro-to-unittest/
import requests     # https://www.pythonforbeginners.com/requests/using-requests-in-python

#from main import *
import main
from util import *

class TestTwitterData(unittest.TestCase):

# ---------------------------------------------------------------------------- #
    # Si el método setUp() hace una excepción mientras se ejecuta la prueba,
    # el framework considerará que la prueba ha sufrido un error y el método
    # de prueba no se ejecutará.
    def setUp(self):
        # self.twitter_data = TwitterData()
        # Creamos el cliente que se va a utilizar.
        self.app = main.app.test_client()
# ---------------------------------------------------------------------------- #
    # Testear que se ha desplegado correctamente
    def test_index(self):
        #result = requests.get('http://127.0.0.1:5000/')
        result = self.app.get("/")
        self.assertEqual(result.status_code, 200)
        pass
# ---------------------------------------------------------------------------- #
    # Testear que se ha desplegado de forma incorrecta
# ---------------------------------------------------------------------------- #
    # Testear que se visualizan todos los elementos
    def test_get_all_data(self):
        #result = requests.get('http://localhost:5000/data_twitter')
        result = self.app.get("/data_twitter")
        self.assertEqual(result.status_code, 200)
        self.assertTrue(get_data_twitter(), "The list is empty")
        pass
# ---------------------------------------------------------------------------- #
    # Testear que se visualiza uno de los elementos
    def test_get_data(self):
        #result = requests.get('http://127.0.0.1:5000/get_data?id=GR')
        result = self.app.get("/get_data?id=GR")
        self.assertEqual(result.status_code, 200)
        self.assertIsInstance(get_id_data_twitter("VLC"), list, "It's not a list")
        pass
# ---------------------------------------------------------------------------- #
    # Testear que se modifica el usuario de uno de los elementos
    def test_put_data(self):
        #result = requests.put('http://127.0.0.1:5000/put_data?name=name&user=SEVILLA&id=GR')
        result = self.app.put("/put_data?name=name&user=SEVILLA&id=GR")
        #result = requests.post('http://127.0.0.1:5000/data_twitter_update?name=name&user=hola&id=GR')
        self.assertEqual(result.status_code, 200)
        #add_data_twitter("Canarias")
        update_data_twitter("MDR", "name", "Canarias")
        get_id_data_twitter("MDR")
        self.assertIn("MDR",get_data_twitter())
        #self.assertTrue("GR" in get_data_twitter(), "No se ha añadido la lista")
        pass
# ---------------------------------------------------------------------------- #
    def test_post_data(self):
        new_data = {"G": [{ "name":"@hol",
                     "url_twitter":"https://twitter.com/aytog",
                     "user_twitter":"@y"
                    }]}
        # result = requests.post('http://localhost:5000/post_data', data=new_data)
        result = self.app.put("/post_data")
        self.assertEqual(result.status_code, 200)
        add_data_twitter(new_data)
        self.assertTrue(get_data_twitter(), "No se ha añadido la lista")
        pass
# ---------------------------------------------------------------------------- #
    # Testear que se elimina uno de los elementos
    def test_delete_data(self):
        # result = requests.delete('http://127.0.0.1:5000/delete_data?id=GR')
        result = self.app.put("/delete_data?id=GR")
        
        self.assertEqual(result.status_code, 200)
        remove_data_twitter("GR")
        #self.assertTrue("GR" not in get_data_twitter(), "No se ha eliminado la lista")
        self.assertNotIn("GR",get_data_twitter())
        pass
# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    unittest.main()
