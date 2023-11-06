import unittest
from OrdenamientoExterno import*
import os
class TestOrdenamientoExterno(unittest.TestCase):
    
    def test_ordenamiento(self):
        """
        Compruebo que el tamaño del archivo sea el mismo y que los datos
        sean de valor creciente.
        """
        generar_numeros_aleatorios("datos_test.txt", 10)
        #generar_numeros_aleatorios("datos_test.txt", 100)  #probar para 100 MB (modificar cantidad de cifras para ahorrar tiempo)
        tamano_original = os.path.getsize("datos_test.txt")
   
        ordenar('datos_test.txt')
        
        tamano_despues_de_ordenar = os.path.getsize('datos_test.txt')
        es_creciente = True
        num_anterior=0
        with open('datos_test.txt', 'r') as f:
            for linea in f:
                num_actual=int(linea)
                if (num_actual>=num_anterior):
                
                    num_anterior=num_actual
                 
                else:
                    
                    es_creciente=False
                    break
                    
        self.assertEqual(es_creciente, True)
        self.assertEqual(tamano_original, tamano_despues_de_ordenar)

if __name__ == '__main__':
    unittest.main()
