import pokemon
import random
import batalha
import ataque
import unittest
import leitorpkmn
import server
import cliente
import xml.etree.ElementTree as ET

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

#Obs: 15 pokemons necessários para testar ^

class TestAtaque(unittest.TestCase):

    def setUp(self):
        self.atk = ataque.Ataque()

    def testPp(self):
        pp = random.randint(1,50)
        self.atk.setPp(pp)
        self.assertEqual(self.atk._pp, pp)

        r = self.atk.getPp()
        self.assertEqual(r, pp)

    def testTyp(self):
        typ = random.randint(0,16)
        self.atk.setTyp(typ)
        self.assertEqual(self.atk._typ, typ)

        r = self.atk.getTyp()
        self.assertEqual(r, typ)

    def testNome(self):
        nome = 'Teste'
        l = list(nome)
        random.shuffle(l)
        nome = ''.join(l)
        self.atk.setNome(nome)
        self.assertEqual(self.atk._nome, nome)

        r = self.atk.getNome()
        self.assertEqual(r, nome)

    def testAcu(self):
        acu = random.randint(0,100)
        self.atk.setAcu(acu)
        self.assertEqual(self.atk._acu, acu)

        r = self.atk.getAcu()
        self.assertEqual(r, acu)

    def testPwr(self):
        pwr = random.randint(10,120)
        self.atk.setPwr(pwr)
        self.assertEqual(self.atk._pwr, pwr)

        r = self.atk.getPwr()
        self.assertEqual(r, pwr)

    def testPpAtual(self):
        ppAtual = random.randint(1,50)
        self.atk.setPpAtual(ppAtual)
        self.assertEqual(self.atk._ppAtual, ppAtual)

        r = self.atk.ppCheck()
        self.assertEqual(r, True)

        r = self.atk.getPpAtual()
        self.assertEqual(r, ppAtual)

        self.atk.setPpAtual(0)
        r = self.atk.ppCheck()
        self.assertEqual(r, False)

    def testDecreasePp(self):
        ppAtual = random.randint(1,50)
        self.atk.setPpAtual(ppAtual)
        self.atk.decreasePp()
        self.assertEqual(self.atk._ppAtual, ppAtual - 1)

        self.atk._nome = 'Struggle'
        self.atk.setPpAtual(ppAtual)
        self.atk.decreasePp()
        self.assertEqual(self.atk._ppAtual, ppAtual)

    def testIsSpecial(self):
        typ = random.randint(9,15)
        self.atk.setTyp(typ)
        r = self.atk.isSpecial()
        self.assertEqual(r, True)

        typ = random.randint(0,8)
        self.atk.setTyp(typ)
        r = self.atk.isSpecial()
        self.assertEqual(r, False)

        self.atk.setTyp(16)
        r = self.atk.isSpecial()
        self.assertEqual(r, False)


class TestBatalha(unittest.TestCase):
  
    def setUp(self):
        self.batalha = batalha.Batalha()
        self.batalha.display.toggle()

    def testIniciaTurno(self):
        x = random.randint(1,254)
        self.batalha.pkmn[0].setSpd(x)
        self.batalha.pkmn[1].setSpd(x + 1)
        r = self.batalha.IniciaTurno()
        self.assertEqual(r, 1)

        self.batalha.pkmn[1].setSpd(x - 1)
        r = self.batalha.IniciaTurno()
        self.assertEqual(r, 0)

        self.batalha.pkmn[1].setSpd(x)
        r = self.batalha.IniciaTurno()
        self.assertGreaterEqual(r, 0)
        self.assertLessEqual(r, 1)

    def testAlternaTurno(self):
        turno = self.batalha.turno
        self.batalha.AlternaTurno()
        self.assertNotEqual(turno,self.batalha.turno)

        self.batalha.AlternaTurno()
        self.assertEqual(turno,self.batalha.turno)

    def testEscolheAtaque(self):
        r = self.batalha.EscolheAtaque()
        self.assertEqual(r, 2)

        self.batalha.AlternaTurno()
        r = self.batalha.EscolheAtaque()
        self.assertEqual(r, 4)

        self.batalha.AlternaTurno()
        r = self.batalha.EscolheAtaque()
        self.assertEqual(r, 0)

    def testTypeChart(self):
        tabReal = [ [1,   1,   1,   1,   1,  .5,   1,   1,   0,   1,   1,   1,   1,   1,   1,   1,   1],
                    [2,   1,  .5,  .5,   1,   2,   1,  .5,   0,   1,   1,   1,   1,  .5,   2,   1,   1],
                    [1,   2,   1,   1,   1,  .5,   1,   2,   1,   1,   1,   2,  .5,   1,   1,   1,   1],
                    [1,   1,   1,  .5,  .5,  .5,   1,   2,  .5,   1,   1,   2,   1,   1,   1,   1,   1],
                    [1,   1,   0,   2,   1,   2,   1,  .5,   1,   2,   1,  .5,   2,   1,   1,   1,   1],
                    [1,  .5,   2,   1,  .5,   1,   1,   2,   1,   2,   1,   1,   1,   1,   2,   1,   1],
                    [1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1],
                    [1,  .5,  .5,   2,   1,   1,   1,   1,  .5,  .5,   1,   2,   1,   2,   1,   1,   1],
                    [0,   1,   1,   1,   1,   1,   1,   1,   2,   1,   1,   1,   1,   0,   1,   1,   1],
                    [1,   1,   1,   1,   1,  .5,   1,   2,   1,  .5,  .5,   2,   1,   1,   2,  .5,   1],
                    [1,   1,   1,   1,   2,   2,   1,   1,   1,   2,  .5,  .5,   1,   1,   1,  .5,   1],
                    [1,   1,  .5,  .5,   2,   2,   1,  .5,   1,  .5,   2,  .5,   1,   1,   1,  .5,   1],
                    [1,   1,   2,   1,   0,   1,   1,   1,   1,   1,   2,  .5,  .5,   1,   1,  .5,   1],
                    [1,   2,   1,   2,   1,   1,   1,   1,   1,   1,   1,   1,   1,  .5,   1,   1,   1],
                    [1,   1,   2,   1,   2,   1,   1,   1,   1,   1,  .5,   2,   1,   1,  .5,   2,   1],
                    [1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1],
                    [1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1]]

        tab = self.batalha.TypeChart('tabela.txt')
        for i in range (0, 17):
            for j in range (0, 17):
                self.assertEqual(tab[i][j], tabReal[i][j])

    def testStabBonus(self):
        atk = ataque.Ataque()
        atk._typ = 12
        r = self.batalha.StabBonus(atk)
        self.assertEqual(r, 1.5)

        atk._typ = 16
        r = self.batalha.StabBonus(atk)
        self.assertEqual(r, 1.5)

        atk._typ = 9
        r = self.batalha.StabBonus(atk)
        self.assertEqual(r, 1)

    def testCriticalHit(self):
        self.batalha.turno = 0
        cont = 0
        for i in range (0, 100000):
            r = self.batalha.CriticalHit()
            if (r != 1): cont += 1
        self.assertAlmostEqual(cont / 100000, self.batalha.pkmn[0]._spd / 512, places=2)

    def testIsHit(self):
        atk = ataque.Ataque()
        atk._acu = random.randint(70,100)
        self.batalha.turno = 0
        cont = 0
        for i in range (0, 100000):
            r = self.batalha.isHit(atk)
            if (r == 1): cont += 1
        self.assertAlmostEqual(cont / 100000, atk._acu / 100, places=2)

    def testIsOver(self):
        r = self.batalha.isOver()
        self.assertEqual(r, False)

        self.batalha.pkmn[0]._hpAtual = 0
        r = self.batalha.isOver()
        self.assertEqual(r, True)

        self.batalha.pkmn[1]._hpAtual = 0
        r = self.batalha.isOver()
        self.assertEqual(r, True)

        self.batalha.pkmn[1]._hpAtual = 1
        self.batalha.pkmn[0]._hpAtual = 0
        r = self.batalha.isOver()
        self.assertEqual(r, True)

    def testCalculaDano(self):
        atk = ataque.Ataque()
        atk._acu = 100
        self.batalha.turno = 0
        hpAtacando = self.batalha.pkmn[0]._hpAtual
        hpDefendendo = self.batalha.pkmn[1]._hpAtual
        self.batalha.CalculaDano(atk)
        self.assertLess(self.batalha.pkmn[1]._hpAtual, hpDefendendo)
        self.assertEqual(self.batalha.pkmn[0]._hpAtual, hpAtacando)

        hpDefendendo = self.batalha.pkmn[1]._hpAtual
        self.batalha.pkmn[0]._struggle = 1
        self.batalha.CalculaDano(atk)
        self.assertLessEqual(self.batalha.pkmn[0]._hpAtual, hpAtacando)
        self.assertLess(self.batalha.pkmn[1]._hpAtual, hpDefendendo)

#Obs: 18 pokemons e 3 escolhas de ataques necessários para testar^

class TestLeitor(unittest.TestCase):

    # O que testar?
    #
    # Se cada coisa está no seu lugar (ou mais ou menos isso).
    #Se falta alguma informação. Se ele devolve erro para entradas erradas.
    #
    def setUp(self):
        self.leitor = leitorpkmn.Leitor()

    def testLeitorPokemonInputOk(self):
        x = self.leitor.leitorDePokemons()
        y = ['Pikachu', 100, 274, 229, 174, 306, 50, 12, 16, 4, []]
        self.assertEqual(x[0], y[0])
        self.assertEqual(x[1], y[1])
        self.assertEqual(x[2], y[2])
        self.assertEqual(x[3], y[3])
        self.assertEqual(x[4], y[4])
        self.assertEqual(x[5], y[5])
        self.assertEqual(x[6], y[6])
        self.assertEqual(x[7], y[7])
        self.assertEqual(x[8], y[8])
        self.assertEqual(x[9], y[9])

    def testLeitorAtaqueInputOk(self):
        atk = self.leitor.leitorDeAtk()
        self.assertEqual(atk._nome, 'Rock Smash')
        self.assertEqual(atk._typ, 1)
        self.assertEqual(atk._acu, 100)
        self.assertEqual(atk._pwr, 40)
        self.assertEqual(atk._pp, 15)
        self.assertEqual(atk._ppAtual, 15)

class testServer(unittest.TestCase):

     def testLePokemonXML(self):
        serv = server.Server()
        serv.battle_state = 'battle_state.xml'
        pkmn = serv.lePokemonXML()
        self.assertEqual(pkmn._nome, 'Pikachu')
        self.assertEqual(pkmn._lvl, 56)
        self.assertEqual(pkmn._hp, 178)
        self.assertEqual(pkmn._hpAtual, 178)
        self.assertEqual(pkmn._atk, 167)
        self.assertEqual(pkmn._defe, 96)
        self.assertEqual(pkmn._spd, 200)
        self.assertEqual(pkmn._spc, 167)
        self.assertEqual(pkmn._typ1, 12)
        self.assertEqual(pkmn._typ2, 16)
        self.assertEqual(pkmn._atks[0]._nome, 'Tackle')
        self.assertEqual(pkmn._atks[0]._typ, 0)
        self.assertEqual(pkmn._atks[0]._pwr, 40)
        self.assertEqual(pkmn._atks[0]._acu, 100)
        self.assertEqual(pkmn._atks[0]._pp, 30)
        self.assertEqual(pkmn._atks[0]._ppAtual, 30)
        self.assertEqual(pkmn._atks[1], None)
        self.assertEqual(pkmn._atks[2], None)
        self.assertEqual(pkmn._atks[3], None)
        self.assertEqual(pkmn._atks[4]._nome, 'Struggle')

class testCliente(unittest.TestCase):
    def testWriteXML(self):
        atk = ataque.Ataque(['Tackle', 0, 40, 100, 30])
        atk2 = ataque.Ataque(['Quick Attack', 0, 50, 100, 20])
        pkmn = pokemon.Pokemon(["Pikachu", 56, 178, 167, 96, 200, 167, 12, 16, [atk, None, atk2, None]])
        s = cliente.writeXML(pkmn)
        root = ET.fromstring(s)
        poke = root[0]
        poke_att = poke.find('attributes')
        tipos = poke.findall('type')

        self.assertEqual(poke.find('name').text, pkmn._nome)
        self.assertEqual(poke.find('level').text, str(pkmn._lvl))
        self.assertEqual(poke_att.find('health').text, str(pkmn._hp))
        self.assertEqual(poke_att.find('attack').text, str(pkmn._atk))
        self.assertEqual(poke_att.find('defense').text, str(pkmn._defe))
        self.assertEqual(poke_att.find('speed').text, str(pkmn._spd))
        self.assertEqual(poke_att.find('special').text, str(pkmn._spc))
        self.assertTrue((tipos[0].text == str(pkmn._typ1) and tipos[1].text == str(pkmn._typ2)) or 
                        (tipos[0].text == str(pkmn._typ2) and tipos[1].text == str(pkmn._typ1)))
        self.assertEqual(len(tipos), 2)

        atks = poke.findall('attacks')
        self.assertEqual(len(atks), 2)

        for j in range(0, 2):
            i = int(atks[j].find('id').text) - 1
            self.assertEqual(atks[j].find('name').text, pkmn._atks[i]._nome)
            self.assertEqual(atks[j].find('type').text, str(pkmn._atks[i]._typ))
            self.assertEqual(atks[j].find('power').text, str(pkmn._atks[i]._pwr))
            self.assertEqual(atks[j].find('accuracy').text, str(pkmn._atks[i]._acu))
            self.assertEqual(atks[j].find('power_points').text, str(pkmn._atks[i]._pp))

#Obs: 1 pokemon necessário para testar ^
if __name__ == '__main__':
    unittest.main()
