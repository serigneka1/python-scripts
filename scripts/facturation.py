# Creer une facture
class Facture:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.pric = prix
        self.quantite = quantite
        self.produits = {}
    # self.produits = {
    #     'Cristaline': [1.75, 5] }
    
    # afficher produit
    def afficher_produits(self):
        print(self.produits)
    
    # ajouter produit
    def ajouter_produit(self):
        nom = input(" entrez le nom du produit: ")
        prix = int(input(" entrez le prix du produit: "))
        quantite = int(input(" entrez la quantite du produit: "))
        if nom in self.produits:
            for _, value in self.produits.items():
                value[0] += prix
                value[1] += quantite

        else:
            self.produits[nom] = [prix, quantite]
        return self.produits
        
    # vendre un produit
    def vendre(self):
        nom = input("Entrez le nom du produit à vendre? ")
        if nom in self.produits:
            quantite = int(input("Pour quelle quantité veux-tu acheter? "))
            if quantite > self.produits[nom][1]:
                print(f"La quantité  de {nom} dans le stock est insuffisante. Elle est de {self.produits[nom][1]}")
                print("Veuillez reprendre la vente !")
                return
            print(f"Le prix unitaire est à {self.produits[nom][0]} €. \nDonc la facture à régler est de {self.produits[nom][0]*quantite} €")
            self.produits[nom][1] -= quantite

if __name__ =="__main__":
    # 1- Voir la liste de produit
    # 2- Ajouter un produit
    # 3- Vendre un produit
    # 4- quitter
    Facture = Facture("Cristaline", 2.5, 10)
    while True:
        print("1- Voir la liste de produit \n2- Ajouter un produit \n3- Vendre un produit \n4- quitter")
        choix = input("Entrez un choix (1-4): ")
        if choix == "1":
            Facture.afficher_produits()
        elif choix =="2":
            Facture.ajouter_produit()
        elif choix == "3":
            Facture.vendre()
        else:
            quit()