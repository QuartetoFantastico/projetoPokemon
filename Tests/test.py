import pokemon
import unittest

# class TestLeitorDePokemon(unittest.TestCase):

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
    # def setUp(self):
    #     self.seq = range(10)

    # def test_shuffle(self):
    #     # make sure the shuffled sequence does not lose any elements
    #     random.shuffle(self.seq)
    #     self.seq.sort()
    #     self.assertEqual(self.seq, range(10))

    #     # should raise an exception for an immutable sequence
    #     self.assertRaises(TypeError, random.shuffle, (1,2,3))

    # def test_choice(self):
    #     element = random.choice(self.seq)
    #     self.assertTrue(element in self.seq)

    # def test_sample(self):
    #     with self.assertRaises(ValueError):
    #         random.sample(self.seq, 20)
    #     for element in random.sample(self.seq, 5):
    #         self.assertTrue(element in self.seq)

class TestPokemon(unittest.TestCase):
    
    # O que testar?
    #
    # Se o Pokemon possui todos os atributos necessários.
    # Se o número de ataques corresponde ao tamanho da lista
    #
    def setUp(self):
      pkmn = pokemon.Pokemon()

    def testIsStruggling(self):
        pkmn._struggle = 0
        r = pkmn.isStruggling()
        self.assertEqual(r, 0)
        pkmn._struggle = 1
        r = pkmn.isStruggling()
        self.assertEqual(r, 1)

    def testIsAlive(self):
        pkmn._getHpAtual = 0 
        r = pkmn.isAlive()
        self.assertEqual(r, 0)
        pkmn._getHpAtual = random.randint(-500, -1) 
        r = pkmn.isAlive()
        self.assertEqual(r, 0)
        pkmn._getHpAtual = random.randint(1, 255) 
        r = pkmn.isAlive()
        self.assertEqual(r, 1)

    def testNome(self):
        nome = 'Teste'
        l = list(nome)
        random.shuffle(l)
        nome = l.join('')
        pkmn.setNome(nome)
        self.assertEqual(pkmn._nome, nome)
        r = pkmn.getNome()
        self.assertEqual(r, nome)


    def testIsOver(self):
        pkmn[0]._getHpAtual = 0 
        pkmn[1]._getHpAtual = 0
        p = pkmn.isOver()
        self.assertEqual(p, 1)
        pkmn[0]._getHpAtual = 1 
        pkmn[1]._getHpAtual = 0
        p = pkmn.isOver()
        self.assertEqual(p, 0)
        pkmn[0]._getHpAtual = 0 
        pkmn[1]._getHpAtual = 1
        p = pkmn.isOver()
        self.assertEqual(r, 0)
        pkmn[0]._getHpAtual = 1 
        pkmn[1]._getHpAtual = 1
        p = pkmn.isOver()
        self.assertEqual(p, 0)



# class TestAtaque(unittest.TestCase):
    
#     # O que testar?
#     #

# class TestBatalha(unittest.TestCase):
  

if __name__ == '__main__':
    unittest.main()
