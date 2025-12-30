# ISP - Après Refactoring
# Respect du principe : Interfaces ségrégées et spécifiques

from abc import ABC, abstractmethod

# Interfaces séparées et spécifiques
class Imprimante(ABC):
    @abstractmethod
    def imprimer(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scanner(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def faxer(self, document):
        pass


class Photocopieur(ABC):
    @abstractmethod
    def photocopier(self, document):
        pass


# Imprimante simple : implémente seulement ce dont elle a besoin
class ImprimanteSimple(Imprimante):
    def imprimer(self, document):
        print(f"Impression de {document}")
        return True


# Scanner simple : implémente seulement ce dont il a besoin
class ScannerSimple(Scanner):
    def scanner(self, document):
        print(f"Scan de {document}")
        return True


# Imprimante moderne : implémente toutes les interfaces nécessaires
class ImprimanteModerne(Imprimante, Scanner, Fax, Photocopieur):
    def imprimer(self, document):
        print(f"Impression de {document}")
        return True
    
    def scanner(self, document):
        print(f"Scan de {document}")
        return True
    
    def faxer(self, document):
        print(f"Envoi du fax de {document}")
        return True
    
    def photocopier(self, document):
        print(f"Photocopie de {document}")
        return True


# Utilisation
if __name__ == "__main__":
    documents = ["document1.pdf", "document2.pdf"]
    
    print("=== Imprimante simple ===")
    imprimante_simple = ImprimanteSimple()
    for doc in documents:
        imprimante_simple.imprimer(doc)
    print()
    
    print("=== Scanner simple ===")
    scanner_simple = ScannerSimple()
    for doc in documents:
        scanner_simple.scanner(doc)
    print()
    
    print("=== Imprimante moderne (toutes fonctionnalités) ===")
    imprimante_moderne = ImprimanteModerne()
    imprimante_moderne.imprimer("document.pdf")
    imprimante_moderne.scanner("photo.jpg")
    imprimante_moderne.faxer("contrat.pdf")
    
    # Avantages :
    # - Chaque classe implémente seulement ce dont elle a besoin
    # - Respect du principe de ségrégation des interfaces