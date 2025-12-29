

```

\# TP\_0\_ICT301 - Principes SOLID



Nom et Prénoms : NGANFANG MERVEILLE  

Matricule :\[22v2344]



&nbsp;   ce que j ai compris des principes solide:



Les principes SOLID constituent cinq piliers fondamentaux de la programmation orientée objet qui permettent de créer des logiciels maintenables, extensibles et robustes.



§§§§§§ 1. SRP (Single Responsibility Principle)



Le principe de responsabilité unique stipule qu'une classe ne doit avoir qu'une seule raison de changer. Chaque classe doit se concentrer sur une seule responsabilité ou fonctionnalité. Cela facilite la maintenance et réduit les effets secondaires lors des modifications.



NB         Une classe Utilisateur ne devrait pas gérer à la fois les données utilisateur et l'envoi d'emails. Il faut séparer ces responsabilités.



\### 2. OCP (Open/Closed Principle)





Le principe ouvert/fermé indique que les entités logicielles doivent être ouvertes à l'extension mais fermées à la modification. On peut ajouter de nouvelles fonctionnalités sans modifier le code existant, généralement via l'héritage ou les interfaces.



NOUS DEVONS  Utiliser des interfaces et le polymorphisme pour ajouter de nouveaux types de calculs sans modifier la classe de base.



§§§§§ 3. LSP (Liskov Substitution Principle)



Le principe de substitution de Liskov affirme que les objets d'une classe dérivée doivent pouvoir remplacer les objets de la classe de base sans altérer le bon fonctionnement du programme. Les sous-classes doivent respecter le contrat de leur classe parent.



NB //// Si une classe Oiseau a une méthode voler(), créer une sous-classe Pingouin qui hérite d'Oiseau violerait ce principe car les pingouins ne volent pas.



///§§§§§§§ 4. ISP (Interface Segregation Principle)



Le principe de ségrégation des interfaces recommande de créer des interfaces spécifiques plutôt qu'une seule interface générale. Les clients ne doivent pas être forcés d'implémenter des méthodes qu'ils n'utilisent pas.



NB/////// Au lieu d'une interface Animal avec toutes les méthodes possibles, créer des interfaces séparées comme IVolant, INageur, IMarcheur.



§§§§§§§§§§ 5. DIP (Dependency Inversion Principle)



Le principe d'inversion des dépendances stipule que les modules de haut niveau ne doivent pas dépendre des modules de bas niveau. Les deux doivent dépendre d'abstractions. De plus, les abstractions ne doivent pas dépendre des détails, mais les détails doivent dépendre des abstractions.



\*\*Exemple //////// Une classe Application ne doit pas dépendre directement d'une classe concrète BaseDeDonnéesMySQL, mais d'une interface IBaseDeDonnées.



\## Structure du projet

```

TP\_0\_ICT301\_NGANFANG\_MERVEILLE/

│   README.md

│   diagrammes\_solid.pdf

├── DIP/

│   ├── avant\_refactoring.py

│   └── apres\_refactoring.py

├── ISP/

│   ├── avant\_refactoring.py

│   └── apres\_refactoring.py

├── LSP/

│   ├── avant\_refactoring.py

│   └── apres\_refactoring.py

├── OCP/

│   ├── avant\_refactoring.py

│   └── apres\_refactoring.py

└── SRP/

&nbsp;   ├── avant\_refactoring.py

&nbsp;   └── apres\_refactoring.py

```



en guise de  Conclusion



L'application des principes SOLID permet de créer du code plus modulaire, testable et facile à maintenir. Ces principes favorisent la réutilisation du code et réduisent la complexité des systèmes logiciels.

