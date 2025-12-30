# SRP - Après Refactoring
# Respect du principe : Chaque classe a une seule responsabilité

# Responsabilité 1 : Gérer les données utilisateur
class Utilisateur:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
    
    def get_nom(self):
        return self.nom
    
    def get_email(self):
        return self.email


# Responsabilité 2 : Gérer la persistance en base de données
class UtilisateurRepository:
    def sauvegarder(self, utilisateur):
        print(f"Connexion à la base de données...")
        print(f"Sauvegarde de {utilisateur.get_nom()} dans la base de données")
        return True
    
    def charger(self, id_utilisateur):
        print(f"Chargement de l'utilisateur {id_utilisateur}")
        return None


# Responsabilité 3 : Gérer l'envoi d'emails
class EmailService:
    def envoyer_email_bienvenue(self, utilisateur):
        print(f"Envoi d'un email de bienvenue à {utilisateur.get_email()}")
        print(f"Cher {utilisateur.get_nom()}, bienvenue sur notre plateforme!")
        return True
    
    def envoyer_email(self, destinataire, sujet, message):
        print(f"Envoi email à {destinataire}: {sujet}")
        return True


# Responsabilité 4 : Valider les données
class ValidateurEmail:
    @staticmethod
    def valider(email):
        if "@" in email and "." in email:
            print("Email valide")
            return True
        else:
            print("Email invalide")
            return False


# Responsabilité 5 : Générer des rapports
class RapportUtilisateur:
    def generer(self, utilisateur):
        rapport = f"""
        ===== Rapport Utilisateur =====
        Nom: {utilisateur.get_nom()}
        Email: {utilisateur.get_email()}
        ==============================
        """
        print(rapport)
        return rapport


# Utilisation
if __name__ == "__main__":
    # Création de l'utilisateur
    user = Utilisateur("Jean Dupont", "jean.dupont@email.com")
    
    # Chaque service gère sa propre responsabilité
    validateur = ValidateurEmail()
    repository = UtilisateurRepository()
    email_service = EmailService()
    rapport_service = RapportUtilisateur()
    
    # Utilisation séparée
    if validateur.valider(user.get_email()):
        repository.sauvegarder(user)
        email_service.envoyer_email_bienvenue(user)
        rapport_service.generer(user)
    
    # Avantages :
    # - Chaque classe a une seule raison de changer
    # - Plus facile à tester individuellement
    # - Plus facile à réutiliser
    # - Code mieux organisé