# SRP - Avant Refactoring
# Violation du principe : La classe Utilisateur a trop de responsabilités

class Utilisateur:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
    
    # Responsabilité 1 : Gérer les données utilisateur
    def get_nom(self):
        return self.nom
    
    def get_email(self):
        return self.email
    
    # Responsabilité 2 : Sauvegarder dans la base de données
    def sauvegarder_en_base(self):
        # Connexion à la base de données
        print(f"Connexion à la base de données...")
        print(f"Sauvegarde de {self.nom} dans la base de données")
        # Code de sauvegarde
        return True
    
    # Responsabilité 3 : Envoyer des emails
    def envoyer_email_bienvenue(self):
        print(f"Envoi d'un email de bienvenue à {self.email}")
        print(f"Cher {self.nom}, bienvenue sur notre plateforme!")
        return True
    
    # Responsabilité 4 : Valider les données
    def valider_email(self):
        if "@" in self.email and "." in self.email:
            print("Email valide")
            return True
        else:
            print("Email invalide")
            return False
    
    # Responsabilité 5 : Générer des rapports
    def generer_rapport(self):
        rapport = f"""
        ===== Rapport Utilisateur =====
        Nom: {self.nom}
        Email: {self.email}
        ==============================
        """
        print(rapport)
        return rapport


# Utilisation
if __name__ == "__main__":
    user = Utilisateur("Jean Dupont", "jean.dupont@email.com")
    
    # La classe fait trop de choses différentes
    user.valider_email()
    user.sauvegarder_en_base()
    user.envoyer_email_bienvenue()
    user.generer_rapport()
    
    # Problème : Si on veut changer la façon d'envoyer des emails,
    # on doit modifier la classe Utilisateur
    # Si on veut changer le format du rapport, même problème
    # Trop de raisons de modifier cette classe !