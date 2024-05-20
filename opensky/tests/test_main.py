import unittest
from main import main

class TestMain(unittest.TestCase):
    def test_main_runs(self):
        # Simplemente prueba si la función main se ejecuta sin errores (necesitarás mockear las funciones de red y db)
        self.assertIsNone(main())

if __name__ == '__main__':
    unittest.main()
