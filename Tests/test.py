import random
import unittest

class TestLeitorDePokemon(unittest.TestCase):

    # O que testar?
    #
    # Se cada coisa está no seu lugar (ou mais ou menos isso).
    #Se falta alguma informação. Se ele devolve erro para entradas erradas.
    #
    #
    #<NOME>
    #<LVL>
    #<HP>
    #<ATK>
    #<DEF>
    #<SPD>
    #<SPC>
    #<TYP1>
    #<TYP2>
    #<NUM ATKS>
    #<NOME>
    #<TYP>
    #<ACU>
    #<PWR>
    #<PP>
    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

class TestPokemon(unittest.TestCase):
    
    # O que testar?
    #
    # Se o Pokemon possui todos os atributos necessários.
    # Se o número de ataques corresponde ao tamanho da lista
    #
    def setUp(self):
      pass

class TestAtaque(unittest.TestCase):
    
    # O que testar?
    #

class TestBatalha(unittest.TestCase):
  

if __name__ == '__main__':
    unittest.main()
