# LSP - Avant Refactoring
# Violation : Les sous-classes ne peuvent pas remplacer la classe de base

class Oiseau:
    def __init__(self, nom):
        self.nom = nom
    
    def voler(self):
        print(f"{self.nom} vole dans le ciel")
        return True
    
    def manger(self):
        print(f"{self.nom} mange")
        return True


class Aigle(Oiseau):
    def voler(self):
        print(f"{self.nom} vole très haut et très vite")
        return True


class Moineau(Oiseau):
    def voler(self):
        print(f"{self.nom} vole de branche en branche")
        return True


# Problème : Les pingouins ne peuvent pas voler !
class Pingouin(Oiseau):
    def voler(self):
        # Violation du LSP : On doit lever une exception ou retourner False
        # Le comportement n'est pas cohérent avec la classe parent
        raise Exception(f"{self.nom} ne peut pas voler !")


class Autruche(Oiseau):
    def voler(self):
        # Même problème : les autruches ne volent pas
        print(f"{self.nom} ne peut pas voler, elle court rapidement")
        return False


# Fonction qui utilise des oiseaux
def faire_voler_oiseaux(oiseaux):
    for oiseau in oiseaux:
        try:
            oiseau.voler()
        except Exception as e:
            print(f"Erreur: {e}")


# Utilisation
if __name__ == "__main__":
    oiseaux = [
        Aigle("Aigle royal"),
        Moineau("Petit moineau"),
        Pingouin("Pingouin empereur"),  # Problème ici !
        Autruche("Grande autruche")     # Problème ici aussi !
    ]
    
    faire_voler_oiseaux(oiseaux)
    
    # Problème : On ne peut pas substituer Pingouin ou Autruche
    # à la place d'Oiseau sans casser le programme
    # Cela viole le principe de substitution de Liskov