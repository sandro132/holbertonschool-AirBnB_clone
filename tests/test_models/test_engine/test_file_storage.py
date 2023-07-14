import unittest
import os
from models.base_model import BaseModel
from models import storage

class FileStorageTestCase(unittest.TestCase):

    def setUp(self):
        # Antes de cada prueba, se asegura de que no exista el archivo file.json
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        # Después de cada prueba, se elimina el archivo file.json si existe
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_and_reload(self):
        # Crear una instancia de BaseModel
        base_model = BaseModel()
        base_model.name = "Test"

        # Agregar la instancia a storage
        storage.new(base_model)

        # Guardar en el archivo
        storage.save()

        # Limpiar el almacenamiento de objetos
        storage.__objects = {}

        # Recargar los objetos desde el archivo
        storage.reload()

        # Obtener el objeto del almacenamiento
        loaded_model = storage.all()["BaseModel.{}".format(base_model.id)]

        # Verificar si los atributos son iguales
        self.assertEqual(base_model.id, loaded_model.id)
        self.assertEqual(base_model.name, loaded_model.name)

if __name__ == '__main__':
    unittest.main()
