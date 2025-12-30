# OCP - Après Refactoring
# Respect du principe : Ouvert à l'extension, fermé à la modification

from abc import ABC, abstractmethod

# Interface abstraite
class StrategieRemise(ABC):
    @abstractmethod
    def calculer_remise(self, montant):
        pass


# Implémentations concrètes - Extension sans modification
class RemiseClientRegulier(StrategieRemise):
    def calculer_remise(self, montant):
        return montant * 0.0  # Pas de remise


class RemiseClientPremium(StrategieRemise):
    def calculer_remise(self, montant):
        return montant * 0.10  # 10% de remise


class RemiseClientVIP(StrategieRemise):
    def calculer_remise(self, montant):
        return montant * 0.20  # 20% de remise


# Nouvelle classe ajoutée SANS modifier le code existant
class RemiseClientGold(StrategieRemise):
    def calculer_remise(self, montant):
        return montant * 0.15  # 15% de remise


# Nouvelle classe pour remise de fidélité
class RemiseClientFidele(StrategieRemise):
    def calculer_remise(self, montant):
        return montant * 0.25  # 25% de remise


class CalculateurPrix:
    def __init__(self, strategie_remise: StrategieRemise):
        self.strategie_remise = strategie_remise
    
    def changer_strategie(self, strategie_remise: StrategieRemise):
        self.strategie_remise = strategie_remise
    
    def calculer_prix_final(self, montant):
        remise = self.strategie_remise.calculer_remise(montant)
        prix_final = montant - remise
        
        print(f"Stratégie: {self.strategie_remise.__class__.__name__}")
        print(f"Montant initial: {montant} FCFA")
        print(f"Remise: {remise} FCFA")
        print(f"Prix final: {prix_final} FCFA")
        
        return prix_final


# Utilisation
if __name__ == "__main__":
    montant = 10000
    
    # Client régulier
    calculateur = CalculateurPrix(RemiseClientRegulier())
    calculateur.calculer_prix_final(montant)
    print()
    
    # Client premium
    calculateur.changer_strategie(RemiseClientPremium())
    calculateur.calculer_prix_final(montant)
    print()
    
    # Client VIP
    calculateur.changer_strategie(RemiseClientVIP())
    calculateur.calculer_prix_final(montant)
    print()
    
    # Nouveau client GOLD - Ajouté sans modifier le code existant
    calculateur.changer_strategie(RemiseClientGold())
    calculateur.calculer_prix_final(montant)
    print()
    
    # Client fidèle - Encore une extension
    calculateur.changer_strategie(RemiseClientFidele())
    calculateur.calculer_prix_final(montant)
    
    # Avantages :
    # - On peut ajouter de nouveaux types de remise sans modifier le code existant
    # - Le code est extensible
    # - Respect du principe Open/Closed