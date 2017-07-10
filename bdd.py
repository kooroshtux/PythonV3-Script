#### AJOUTER PRODUIT INFORMATIQUE
import ast

ajouterCATH=input("Entrer une catégorie: ")
ajouterC=input("Entrer un composant pour l'enregistrer dans la BDD: ")
ajouterP=input("Entrer le prix de ce composant: ")

print("Vous avez inséré le composant {0} avec un tarif de {1}€" .format(ajouterC,ajouterP))

bdd={}
if ajouterCATH in  bdd.keys():
    if True:
        print("Element déjà présent dans la BDD")
        print(bdd)
    else:
        print("pas present")
        bdd.keys=ast.literal_eval(ajouterCATH)
        print(bdd.keys)

