"""
    Convertir des cm en pouce et vice-versa.

   NB:
    1 pouce = 2.54 cm
    1 cm = 0.39 pouce
"""

class Convertisseur:
    def __init__(self):
        pass

    @staticmethod
    def convertir_p_cm(pouce):
        return pouce*2.54
    @staticmethod
    def convertir_cm_p(cm):
        return cm/2.54
    
if __name__ =="__main__":

    while True:
        print("----------------------  choix:  ------------------------ \n \
         1 - Convertir des cm en pouce \n \
         2 - Convertir des pouce en cm\n \
         3 - Quittez le programme")
        print("----------------------  choix:  ------------------------")
            
        choix = input("Entrez votre choix (1, 2, 3): ")
        

        if choix == "1":
            try:
                valeur = float(input("Quel valeur en cm convertir en pouce? "))
                resultat = Convertisseur.convertir_cm_p(valeur)
                unite = "pouce" if resultat < 2 else "pouces"
            except ValueError:
                print("Entrez une valeur valide.")
            print(f"Resultat: {resultat: .2f} {unite}")
        elif choix == "2":
            try:
                valeur = float(input("Quel valeur en pouce convertir cm? "))
                resultat = Convertisseur.convertir_p_cm(valeur)
            except ValueError:
                print("Entrez une valeur valide.")
            print(f"Resultat: {resultat: .2f} cm")
        elif choix =="3":
            print("Au revoir ....")
            break
        else:
            print("Entrez un choix valide (1, 2 ou 3).")
            
        

