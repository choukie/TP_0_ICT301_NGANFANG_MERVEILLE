# DIP - Après Refactoring
# Respect du principe : Dépendance aux abstractions

from abc import ABC, abstractmethod

# Abstraction (interface) - Ni haut ni bas niveau ne dépendent l'un de l'autre
class BaseDeDonnees(ABC):
    @abstractmethod
    def connecter(self):
        pass
    
    @abstractmethod
    def sauvegarder(self, donnees):
        pass
    
    @abstractmethod
    def recuperer(self, id):
        pass


# Implémentation concrète 1 : MySQL
class MySQLDatabase(BaseDeDonnees):
    def __init__(self):
        self.connexion = "MySQL"
    
    def connecter(self):
        print(f"Connexion à la base de données {self.connexion}")
        return True
    
    def sauvegarder(self, donnees):
        print(f"Sauvegarde dans MySQL: {donnees}")
        return True
    
    def recuperer(self, id):
        print(f"Récupération depuis MySQL de l'ID: {id}")
        return {"id": id, "nom": "Données MySQL", "source": "MySQL"}


# Implémentation concrète 2 : MongoDB
class MongoDB(BaseDeDonnees):
    def __init__(self):
        self.connexion = "MongoDB"
    
    def connecter(self):
        print(f"Connexion à la base de données {self.connexion}")
        return True
    
    def sauvegarder(self, donnees):
        print(f"Insertion dans MongoDB: {donnees}")
        return True
    
    def recuperer(self, id):
        print(f"Recherche dans MongoDB de l'ID: {id}")
        return {"id": id, "nom": "Données MongoDB", "source": "MongoDB"}


# Classe de haut niveau qui dépend de l'abstraction
class GestionnaireUtilisateurs:
    def __init__(self, database: BaseDeDonnees):
        # Dépend de l'abstraction, pas de l'implémentation
        self.database = database
    
    def changer_base_de_donnees(self, database: BaseDeDonnees):
        """Permet de changer de base de données dynamiquement"""
        self.database = database
    
    def ajouter_utilisateur(self, utilisateur):
        self.database.connecter()
        self.database.sauvegarder(utilisateur)
        print(f"Utilisateur {utilisateur['nom']} ajouté avec succès")
    
    def obtenir_utilisateur(self, id):
        self.database.connecter()
        return self.database.recuperer(id)


# Utilisation
if __name__ == "__main__":
    utilisateur = {"nom": "Jean Dupont", "email": "jean@email.com"}
    
    # Utilisation avec MySQL
    print("=== Avec MySQL ===")
    mysql_db = MySQLDatabase()
    gestionnaire = GestionnaireUtilisateurs(mysql_db)
    gestionnaire.ajouter_utilisateur(utilisateur)
    user_data = gestionnaire.obtenir_utilisateur(1)
    print(f"Données: {user_data}")
    print()
    
    # Changement vers MongoDB - Pas besoin de modifier GestionnaireUtilisateurs
    print("=== Changement vers MongoDB ===")
    mongo_db = MongoDB()
    gestionnaire.changer_base_de_donnees(mongo_db)
    gestionnaire.ajouter_utilisateur(utilisateur)
    user_data = gestionnaire.obtenir_utilisateur(2)
    print(f"Données: {user_data}")
    
    # Avantages :
    # - Le module de haut niveau ne dépend pas du module de bas niveau
    # - Facile de changer d'implémentation
    # - Respect du principe d'inversion des dépendances