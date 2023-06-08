from characters.ninja import Ninja
from characters.pet import Pet

Poro = Pet("Poro", "Fluffball", "Roll Around")
Zed = Ninja("Zed", "Slayer", "Potions", "Biscuits", Poro)
# print(Zed.pet)

Zed.walk().feed().bathe()