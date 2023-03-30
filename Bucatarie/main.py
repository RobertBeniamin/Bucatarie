from src.bucatarie import Bucatarie

inventar = {}
a = Bucatarie("Alexabdra")
Bucatarie.adaugaIngredient("oua", 7)
print(inventar)


Bucatarie.scadeInventar('oua', 7)
print(inventar)

Bucatarie.adaugaReteta("Clatite", faina = 200, oua = 4, lapte = 200)
