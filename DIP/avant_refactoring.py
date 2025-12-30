# DIP - Avant Refactoring
# Violation : Dépendance directe aux implémentations concrètes

# Classe de bas niveau : Base de données MySQL
class MySQLDatabase:
    def __init__(self):
        self.connexion = "MySQL"
    
    def connecter(self):
        print(f"Connexion à la base de données {self.connexion}")
        return True
    
    def sauvegarder_donnees(self, donnees):
        print(f"Sauvegarde dans MySQL: {donnees}")
        return True
    
    def recuperer_donnees(self, id):
        print(f"Récupération depuis MySQL de l'ID: {id}")
        return {"id": id, "nom": "Données de test"}


# Classe de haut niveau qui dépend directement de MySQLDatabase
class GestionnaireUtilisateurs:
    def __init__(self):
        # Dépendance directe à une implémentation concrète
        self.database = MySQLDatabase()
    
    def ajouter_utilisateur(self, utilisateur):
        self.database.connecter()
        self.database.sauvegarder_donnees(utilisateur)
        print(f"Utilisateur {utilisateur['nom']} ajouté")
    
    def obtenir_utilisateur(self, id):
        self.database.connecter()
        return self.database.recuperer_donnees(id)


# Utilisation
if __name__ == "__main__":
    gestionnaire = GestionnaireUtilisateurs()
    
    utilisateur = {"nom": "Jean Dupont", "email": "jean@email.com"}
    gestionnaire.ajouter_utilisateur(utilisateur)
    print()
    
    user_data = gestionnaire.obtenir_utilisateur(1)
    print(f"Données récupérées: {user_data}")
    
    # Problème : Pour changer de MySQL à MongoDB,
    # il faut MODIFIER la classe GestionnaireUtilisateurs
    # Le module de haut niveau dépend du module de bas niveau
    # Cela viole le principe DIP