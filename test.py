import unittest
from romanos import romano_a_entero

class RomanosTest(unittest.TestCase):

    def test_una_sola_letra(self):
        self.assertEqual(romano_a_entero('I'), 1, 'I debe valer 1')
        self.assertEqual(romano_a_entero('V'), 5, 'V debe valer 5')
        self.assertEqual(romano_a_entero('X'), 10, 'X debe valer 10')
        self.assertEqual(romano_a_entero('L'), 50, 'L debe valer 50')
        self.assertEqual(romano_a_entero('C'), 100, 'C debe valer 100')
        self.assertEqual(romano_a_entero('D'), 500, 'D debe valer 500')
        self.assertEqual(romano_a_entero('M'), 1000, 'M debe valer 1000')

    def test_no_mas_de_tres_simbolos_consecutivos(self):
        self.assertEqual(romano_a_entero('IIII'), 'ERROR: no se puede repetir un símbolo más de tres veces')

    def test_no_repetir_letras_con_valor_5(self):
        self.assertEqual(romano_a_entero('VV'), 'ERROR: no 5 repetidos')
        self.assertEqual(romano_a_entero('LL'), 'ERROR: no 5 repetidos')
        self.assertEqual(romano_a_entero('DD'), 'ERROR: no 5 repetidos')
        self.assertEqual(romano_a_entero('XVV'), 'ERROR: no 5 repetidos')
        self.assertEqual(romano_a_entero('CVV'), 'ERROR: no 5 repetidos')
        self.assertEqual(romano_a_entero('MDVV'), 'ERROR: no 5 repetidos')

    def test_no_cadena_vacia(self):
        self.assertRaises(ValueError, romano_a_entero, '')
    
    def test_entrada_es_una_cadena(self):
        self.assertRaises(TypeError, romano_a_entero, 33)

unittest.main()