import pokemon
import random
import ataque
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
    
    def setUp(self):
      self.pkmn = pokemon.Pokemon()

    def testStruggle(self):
        n = random.randint(1,4)
        lista = []
        for i in range(0, n):
            atk = ataque.Ataque()
            atk._ppAtual = 0
            lista.append(atk)
        for j in range(i, 4):
            lista.append(None)
        self.pkmn._atks = lista
        self.pkmn.setStruggle()
        r = self.pkmn.isStruggling()
        self.assertEqual(r, True)

        n = random.randint(1,4)
        lista = []
        for i in range(0, n):
            atk = ataque.Ataque()
            atk._ppAtual = 1
            lista.append(atk)
        for j in range(i, 4):
            lista.append(None)
        self.pkmn._atks = lista
        self.pkmn.setStruggle()
        r = self.pkmn.isStruggling()
        self.assertEqual(r, False)

    def testIsAlive(self):
        self.pkmn._hpAtual = 0 
        r = self.pkmn.isAlive()
        self.assertEqual(r, False)
        self.pkmn._hpAtual = random.randint(-500, -1) 
        r = self.pkmn.isAlive()
        self.assertEqual(r, False)
        self.pkmn._hpAtual = random.randint(1, 255) 
        r = self.pkmn.isAlive()
        self.assertEqual(r, True)

    def testNome(self):
        nome = 'Teste'
        l = list(nome)
        random.shuffle(l)
        nome = ''.join(l)
        self.pkmn.setNome(nome)
        self.assertEqual(self.pkmn._nome, nome)
        r = self.pkmn.getNome()
        self.assertEqual(r, nome)

    def testHp(self):
        hp = random.randint(1,255)
        self.pkmn.setHp(hp)
        self.assertEqual(self.pkmn._hp, hp)
        r = self.pkmn.getHp()
        self.assertEqual(r, hp)

    def testAtk(self):
        atk = random.randint(1,255)
        self.pkmn.setAtk(atk)
        self.assertEqual(self.pkmn._atk, atk)
        r = self.pkmn.getAtk()
        self.assertEqual(r, atk)

    def testAtk(self):
        atk = random.randint(1,255)
        self.pkmn.setAtk(atk)
        self.assertEqual(self.pkmn._atk, atk)
        r = self.pkmn.getAtk()
        self.assertEqual(r, atk)

    def testDefe(self):
        defe = random.randint(1,255)
        self.pkmn.setDefe(defe)
        self.assertEqual(self.pkmn._defe, defe)
        r = self.pkmn.getDefe()
        self.assertEqual(r, defe)

    def testSpd(self):
        spd = random.randint(1,255)
        self.pkmn.setSpd(spd)
        self.assertEqual(self.pkmn._spd, spd)
        r = self.pkmn.getSpd()
        self.assertEqual(r, spd)

    def testSpc(self):
        spc = random.randint(1,255)
        self.pkmn.setSpc(spc)
        self.assertEqual(self.pkmn._spc, spc)
        r = self.pkmn.getSpc()
        self.assertEqual(r, spc)

    def testTyp1(self):
        typ1 = random.randint(1,255)
        self.pkmn.setTyp1(typ1)
        self.assertEqual(self.pkmn._typ1, typ1)
        r = self.pkmn.getTyp1()
        self.assertEqual(r, typ1)

    def testTyp2(self):
        typ2 = random.randint(1,255)
        self.pkmn.setTyp2(typ2)
        self.assertEqual(self.pkmn._typ2, typ2)
        r = self.pkmn.getTyp2()
        self.assertEqual(r, typ2)

    def testHpAtual(self):
        hpatual = random.randint(1,255)
        self.pkmn.setHpAtual(hpatual)
        self.assertEqual(self.pkmn._hpAtual, hpatual)
        r = self.pkmn.getHpAtual()
        self.assertEqual(r, hpatual)

    def testDefe(self):
        defe = random.randint(1,255)
        self.pkmn.setDefe(defe)
        self.assertEqual(self.pkmn._defe, defe)
        r = self.pkmn.getDefe()
        self.assertEqual(r, defe)

    def testgetNatks(self):
        n = random.randint(1,4)
        lista = []
        for i in range(0, n):
            atk = ataque.Ataque()
            lista.append(atk)
        for j in range(i, 4):
            lista.append(None)
        self.pkmn._atks = lista
        r = self.pkmn.getNatks()
        self.assertEqual(r, n)

    def testLvl(self):
        lvl = random.randint(1,100)
        self.pkmn._lvl = lvl
        r = self.pkmn.getLvl()
        self.assertEqual(r, lvl)



# class TestAtaque(unittest.TestCase):
    
#     # O que testar?
#     #

# class TestBatalha(unittest.TestCase):
  

if __name__ == '__main__':
    unittest.main()
