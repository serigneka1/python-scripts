# produits = {
#     "coca" : [1.75, 30],
#     "cristaline" : [2.50, 10],
#     "redbull": [1.25, 50]
#     }

class Facture:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.pric = prix
        self.quantite = quantite
        self.produits = {"carotte": [2, 10]}

    # self.produits = {
    #     'Cristaline': [1.75, 5],
    #     'Couscous': [2.50, 10],
    #     'Sel': [.99, 24]
    # }
    
    # afficher produit
    def afficher_produits(self):
        print(self.produits)
    
    # ajouter produit
    def ajouter_produit(self):
        nom = input(" entrez le nom du produit: ")
        prix = int(input(" entrez le prix du produit: "))
        quantite = int(input(" entrez la quantite du produit: "))
        if nom in self.produits:
            for key, value in self.produits.items():
                value[0] += prix
                value[1] += quantite
            

Facture = Facture("carotte", 2, 40)

# Facture.afficher_produits()
Facture.ajouter_produit()
Facture.afficher_produits()