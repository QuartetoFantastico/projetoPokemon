import xml.etree.ElementTree as ET

root = ET.Element('battle_state')
ET.SubElement(root, "pokemon")
poke = root.find('pokemon')

ET.SubElement(poke, "name")
poke.find('name').text = pkmn.getNome()

ET.SubElement(poke, "level")
poke.find('level').text = str(pkmn.getLvl())

ET.SubElement(poke, "attributes")
poke_att = poke.find('attributes')

ET.SubElement(poke_att, "health")
poke_att.find('health').text = str(pkmn.getHp())

ET.SubElement(poke_att, "attack")
poke_att.find('attack').text = str(pkmn.getAtk())

ET.SubElement(poke_att, "defense")
poke_att.find('defense').text = str(pkmn.getDefe())

ET.SubElement(poke_att, "speed")
poke_att.find('speed').text = str(pkmn.getSpd())

ET.SubElement(poke_att, "special")
poke_att.find('special').text = str(pkmn.getSpc())


ET.SubElement(poke, "type")
ET.SubElement(poke, "type")
tipos = ET.findall('type')
tipos[0].text = str(pkmn.getTyp1())
tipos[1].text = str(pkmn.getTyp2())

for i in range(0, pkmn.nAtks()):
    atk = pkmn.getAtks(i)
    if (atk is not None):
        ET.SubElement(poke, "attacks")
        poke_atk = poke.find('attacks')

        ET.SubElement(poke_atk, "id")
        poke_atk.find('id').text = str(i + 1)

        ET.SubElement(poke_atk, "name")
        poke_atk.find('name').text = atk.getNome()

        ET.SubElement(poke_atk, "type")
        poke_atk.find('type').text = str(atk.getTyp())

        ET.SubElement(poke_atk, "power")
        poke_atk.find('power').text = str(atk.getPwr())

        ET.SubElement(poke_atk, "accuracy")
        poke_atk.find('accuracy').text = str(atk.getAcu())

        ET.SubElement(poke_atk, "power_points")      
        poke_atk.find('power_points').text = str(atk.getPp())


s = ET.tostring(root)
print(s)
