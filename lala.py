import pokemon
import server
import ataque

serv = server.Server()
f = open('battle_state.xml', 'r')
serv.battle_state = f.read()
f.close()
atk = ataque.Ataque(['Thunder', 12, 110, 70, 10])
atk2 = ataque.Ataque(['Electro Ball', 12, 100, 80, 10])
atk3 = ataque.Ataque(['Quick Attack', 0, 100, 40, 30])
atk4 = ataque.Ataque(['Rock Smash', 1, 100, 40, 15])
pkmn = ["Pikachu", 56, 178, 167, 96, 200, 167, 12, 16, [atk, atk2, atk3, atk4]]
pkmn2 = ["Raichu", 57, 179, 168, 97, 201, 168, 12, 16, [atk, atk2, atk3, atk4]]
serv.battle_state = serv.criaBatalha(serv.battle_state, pkmn2)

#Verifica batalha
pkmn = [pokemon.Pokemon(pkmn), pokemon.Pokemon(pkmn2)]
pokemon.Equals(pkmn[0], serv.batalha.pkmn[0])
pokemon.Equals(pkmn[1], serv.batalha.pkmn[1])
