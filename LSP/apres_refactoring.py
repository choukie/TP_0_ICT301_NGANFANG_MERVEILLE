# LSP - Après Refactoring
# Respect du principe : Bonne hiérarchie avec substitution possible

from abc import ABC, abstractmethod

# Classe de base
class Oiseau(ABC):
    def __init__(self, nom):
        self.nom = nom
    
    @abstractmethod
    def se_deplacer(self):
        pass
    
    def manger(self):
        print(f"{self.nom} mange")
        return True


# Interface pour les oiseaux qui volent
class OiseauVolant(Oiseau):
    def se_deplacer(self):
        self.voler()
    
    def voler(self):
        print(f"{self.nom} vole dans le ciel")
        return True


# Interface pour les oiseaux qui ne volent pas
class OiseauNonVolant(Oiseau):
    def se_deplacer(self):
        self.marcher()
    
    @abstractmethod
    def marcher(self):
        pass


# Implémentations des oiseaux volants
class Aigle(OiseauVolant):
    def voler(self):
        print(f"{self.nom} vole très haut et très vite")
        return True


class Moineau(OiseauVolant):
    def voler(self):
        print(f"{self.nom} vole de branche en branche")
        return True


# Implémentations des oiseaux non volants
class Pingouin(OiseauNonVolant):
    def marcher(self):
        print(f"{self.nom} marche et nage, mais ne vole pas")
        return True
    
    def nager(self):
        print(f"{self.nom} nage très bien")
        return True


class Autruche(OiseauNonVolant):
    def marcher(self):
        print(f"{self.nom} court très rapidement")
        return True


# Fonctions qui respectent le LSP
def faire_deplacer_oiseaux(oiseaux):
    """Tous les oiseaux peuvent se déplacer"""
    for oiseau in oiseaux:
        oiseau.se_deplacer()


# Utilisation
if __name__ == "__main__":
    # Tous les oiseaux
    tous_oiseaux = [
        Aigle("Aigle royal"),
        Moineau("Petit moineau"),
        Pingouin("Pingouin empereur"),
        Autruche("Grande autruche")
    ]
    
    print("=== Tous les oiseaux se déplacent ===")
    faire_deplacer_oiseaux(tous_oiseaux)
    
    # Avantages :
    # - Chaque sous-classe peut remplacer sa classe parent sans problème
    # - Pas d'exceptions ou de comportements inattendus
    # - Respect du principe de substitution de Liskov