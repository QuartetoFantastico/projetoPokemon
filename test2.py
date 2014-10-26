import unittest
import leitorpkmn

class TestLeitor(unittest.TestCase):

    def setUp(self):
        self.leitor = leitorpkmn.Leitor()

    def testLeitorPokemonInputVazio(self):
    	x = self.leitor.leitorDePokemons()
    	self.assertEqual(x, [])

    def testLeitorPokemonInputErrado(self):
    	x = self.leitor.leitorDePokemons()
    	self.assertEqual(x, [])

if __name__ == '__main__':
    unittest.main()