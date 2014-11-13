import requests
from flask import Flask
import batalha
import pokemon
import ataque

def getBattle():
    return requests.get('http://127.0.0.1:5000/battle/').content

def getAttack():
    return requests.get('http://127.0.0.1:5000/battle/attack/2').content

def postBattle():
    return requests.post('http://127.0.0.1:5000/battle/', data='Sei la').content

def writeXML(pkmn):
	#Escreve um XML a partir de um pokemon

print(getBattle())
print(getAttack())
print(postBattle())