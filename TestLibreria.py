import unittest
import json
import os
from libreria import Libreria


class TestLibreria(unittest.TestCase):

    def setUp(self):
        """Configura el entorno de prueba iniciando la librería y añadiendo libros."""
        self.libreria = Libreria()
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.libreria.anadir_libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela", 1985)
        self.test_file = 'test_libreria.json'

    def tearDown(self):
        """Limpia el entorno de prueba eliminando archivos creados durante las pruebas."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_anadir_libro(self):
        """Prueba la adición de un libro a la colección."""
        resultado = self.libreria.anadir_libro("1984", "George Orwell", "Distopía", 1949)
        self.assertEqual(resultado, "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 3)

    def test_buscar_libro(self):
        """Prueba la búsqueda de un libro por título."""
        libros = self.libreria.buscar_libro("Cien años de soledad")
        self.assertEqual(len(libros), 1)
        self.assertEqual(libros[0]['autor'], "Gabriel García Márquez")

    def test_buscar_por_autor(self):
        """Prueba la búsqueda de libros por autor."""
        libros = self.libreria.buscar_por_autor("Gabriel García Márquez")
        self.assertEqual(len(libros), 2)

    def test_eliminar_libro(self):
        """Prueba la eliminación de un libro de la colección."""
        resultado = self.libreria.eliminar_libro("Cien años de soledad")
        self.assertEqual(resultado, "Libro eliminado")
        self.assertEqual(len(self.libreria.libros), 1)

        resultado = self.libreria.eliminar_libro("No existe")
        self.assertEqual(resultado, "Libro no encontrado")

    def test_guardar_libros(self):
        """Prueba la funcionalidad de guardar la colección en un archivo."""
        resultado = self.libreria.guardar_libros(self.test_file)
        self.assertEqual(resultado, "Libros guardados")
        with open(self.test_file, 'r') as f:
            libros = json.load(f)
        self.assertEqual(len(libros), 2)

    def test_cargar_libros(self):
        """Prueba la funcionalidad de cargar la colección desde un archivo."""
        self.libreria.guardar_libros(self.test_file)
        nueva_libreria = Libreria()
        resultado = nueva_libreria.cargar_libros(self.test_file)
        self.assertEqual(resultado, "Libros cargados")
        self.assertEqual(len(nueva_libreria.libros), 2)

        resultado = nueva_libreria.cargar_libros('no_existe.json')
        self.assertEqual(resultado, "Archivo no encontrado")


if __name__ == '__main__':
    unittest.main()
