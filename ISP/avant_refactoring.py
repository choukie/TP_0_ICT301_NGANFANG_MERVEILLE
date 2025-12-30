# ISP - Avant Refactoring
# Violation : Interface trop large, les clients doivent implémenter des méthodes inutiles

from abc import ABC, abstractmethod

# Interface trop large avec toutes les fonctionnalités possibles
class AppareilMultifonction(ABC):
    @abstractmethod
    def imprimer(self, document):
        pass
    
    @abstractmethod
    def scanner(self, document):
        pass
    
    @abstractmethod
    def faxer(self, document):
        pass
    
    @abstractmethod
    def photocopier(self, document):
        pass


# Imprimante moderne avec toutes les fonctionnalités
class ImprimanteModerne(AppareilMultifonction):
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


# Problème : Une imprimante simple doit implémenter toutes les méthodes
class ImprimanteSimple(AppareilMultifonction):
    def imprimer(self, document):
        print(f"Impression de {document}")
        return True
    
    # Forcée d'implémenter des méthodes qu'elle ne supporte pas
    def scanner(self, document):
        raise NotImplementedError("Cette imprimante ne peut pas scanner")
    
    def faxer(self, document):
        raise NotImplementedError("Cette imprimante ne peut pas faxer")
    
    def photocopier(self, document):
        raise NotImplementedError("Cette imprimante ne peut pas photocopier")


# Utilisation
if __name__ == "__main__":
    print("=== Imprimante moderne ===")
    imprimante_moderne = ImprimanteModerne()
    imprimante_moderne.imprimer("document.pdf")
    imprimante_moderne.scanner("photo.jpg")
    print()
    
    print("=== Imprimante simple ===")
    imprimante_simple = ImprimanteSimple()
    imprimante_simple.imprimer("document.pdf")
    try:
        imprimante_simple.scanner("photo.jpg")  # Erreur !
    except NotImplementedError as e:
        print(f"Erreur: {e}")
    
    # Problème : Les classes sont forcées d'implémenter des méthodes
    # qu'elles n'utilisent pas. Cela viole le principe ISP