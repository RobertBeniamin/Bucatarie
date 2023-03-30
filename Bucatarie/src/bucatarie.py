class Bucatarie:
    def __init__(self, numeIngredient):
        self.numeIngredient = numeIngredient
        self.inventar = {}

    def adaugaIngredient(self, ingredient, cantitate):
    #     # adaugam dintr-o lista de cumparaturi sau manual in inventar
    #     # in lista de cumparaturi ingredientele sunt trecute pe cate o linie, ingredient si cantitatea
    #     # cantitatea poate fi exprimata in grame, sau in numar de bucati - fara a specifica explicit acest lucru, ca ne incurca :))
    #     # ar fi frumos sa pot salva cumva intr-un fisier inventarul.

        self.inventar[ingredient] = cantitate




    #     request = eval(input("Alegeti:\n 1 - Adaugati din lista de cumparaturi\n 2 - Adaugati ingrediente manual\n>>>"))
    #     if request == 1:
    #         listaCumparaturi = input("Intoduceti lista sub format 'file.txt'\n>>>")
    #         cale = "data/"+listaCumparaturi
    #         with open(cale, 'r') as f:
    #             lines = f.read().splitlines()
    #             for line in lines:
    #                 l = line.split(' ')
    #                 if l[0] in inventar:
    #                     inventar[l[0]] = int(inventar[l[0]]) + l[1]
    #                 else:
    #                     inventar[l[0]] = l[1]
    #     elif request == 2:
    #         ingredientCantitate = ' '
    #         while ' ' in ingredientCantitate:
    #             ingredientCantitate = input("Intoduceti ingredientul si cantiatatea exprimata in grame, sau nr de bucati\n >>>")
    #             l = ingredientCantitate.split(' ')
    #             if len(l) == 2:
    #                 if l[0] in inventar:
    #                     inventar[l[0]] = int(inventar[l[0]]) + int(l[1])
    #                 else:
    #                     inventar[l[0]] = l[1]
    #             else:
    #                 print("Am terminat adaugarea ingredientelor.")
    #     else:
    #         print("Selectie invalida.")
    #
    #
    # def scadeInventar(nume, cantitate, inventar):
    #     # scade din inventar elementele necesare unei retete, dupa ce se face produs final
    #     if cantitate <= int(inventar[nume]):
    #         inventar[nume] = int(inventar[nume]) - cantitate
    #     else:
    #         print(f'Nu aveti cantitatea suficienta de {nume}')
    #
    #
    # def adaugaReteta(nume, **ingredient):
    #     print(nume)
    #     reteta = {}

