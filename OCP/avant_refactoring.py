# OCP - Avant Refactoring
# Violation : Il faut modifier la classe pour ajouter de nouveaux types

class CalculateurRemise:
    def calculer_remise(self, client_type, montant):
        if client_type == "REGULAR":
            return montant * 0.0  # Pas de remise
        elif client_type == "PREMIUM":
            return montant * 0.10  # 10% de remise
        elif client_type == "VIP":
            return montant * 0.20  # 20% de remise
        else:
            return 0


class CalculateurPrix:
    def __init__(self):
        self.calculateur_remise = CalculateurRemise()
    
    def calculer_prix_final(self, client_type, montant):
        remise = self.calculateur_remise.calculer_remise(client_type, montant)
        prix_final = montant - remise
        
        print(f"Client type: {client_type}")
        print(f"Montant initial: {montant} FCFA")
        print(f"Remise: {remise} FCFA")
        print(f"Prix final: {prix_final} FCFA")
        
        return prix_final


# Utilisation
if __name__ == "__main__":
    calculateur = CalculateurPrix()
    
    calculateur.calculer_prix_final("REGULAR", 10000)
    print()
    calculateur.calculer_prix_final("PREMIUM", 10000)
    print()
    calculateur.calculer_prix_final("VIP", 10000)
    
    # Problème : Pour ajouter un nouveau type de client (ex: GOLD),
    # il faut MODIFIER la classe CalculateurRemise
    # Cela viole le principe Open/Closed
    # La classe devrait être fermée à la modification