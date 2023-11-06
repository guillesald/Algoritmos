import unittest
from OrdenamientoExterno import*
class TestOrdenamientoExterno(unittest.TestCase):
    
    def test_ordenamiento(self):
        """
        Compruebo que la cantidad de de datos sea la misma y que los datos
        sean de valor creciente.
        """
        
        generar_numeros_aleatorios("datos_test.txt", 10)
        #generar_numeros_aleatorios("datos_test.txt", 100)  #probar para 100 MB (modificar cantidad de cifras para ahorrar tiempo)
        numero_lineas_originales = 0
        with open("datos_test.txt", 'r') as f:
            for linea in f:
                numero_lineas_originales += 1
                
                
        ordenar('datos_test.txt')
        
        numero_lineas_luego_de_ordenar=0
        es_creciente = True
        num_anterior=0
        with open('datos_test.txt', 'r') as f:
            for linea in f:
                numero_lineas_luego_de_ordenar+=1
                linea.strip()
                num_actual=int(linea)
                if (num_actual>=num_anterior):
                
                    num_anterior=num_actual
                 
                else:
                    
                    es_creciente=False
                    break
                    
        self.assertEqual(es_creciente, True)
        self.assertEqual(numero_lineas_originales, numero_lineas_luego_de_ordenar)
    
if __name__ == '__main__':
    unittest.main()
