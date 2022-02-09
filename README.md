# Big-data-project
TAXI FRAUD DETECTION

# Introduction générale :
Le réseau routier en tant qu'ensemble de routes interconnectées et sécantes permettant le passage des personnes et des marchandises constitue un secteur important dans une économie de la ville de Berrechid, c'est pourquoi notre projet consiste à suivre en temps réel les taxis circulant sur le réseau routier de la ville de Berrechid, ainsi que l'analyse et la détection des fraudes probables.

Notre projet est intégré au module applications big data et vise la détection des fraudes taxi de la ville de BERRECHID, nous l'avons appelé "TRUSTY RIDE". C'est dans le but de clarifier l'idée que nous avons préparé ce rapport qui couvre la description de l'entreprise, la conception et la partie technique.
# I. Description du projet :
## 1. Problématique :
Notre problématique est de développer une application permettant de suivre l'état d'un réseau routier en temps réel en analysant l'itinéraire du taxi pour éviter les fraudes.
## 2. Objectifs :
• Surveillance en temps réel de l'état des itinéraires de taxi

• Analyse de la trajectoire des taxis

• Détection de fraude au taxi.

Logo

![2](https://user-images.githubusercontent.com/81876011/153175234-69168448-3321-4999-aad8-c8c8cf8bc922.png)

Nous avons choisi yack tracking comme nom de notre société car notre objectif est de maintenir une relation de confiance entre le chauffeur de taxi et ses clients. Nous avons également fait apparaître un taxi dans notre logo qui fait référence à ce que nous ciblons.

## 3. Technologies utilisées :
• SUMO

SUMO est l'un des outils gratuits de simulation de trafic open source pour la construction et l'exécution d'exemples de systèmes de modèles de trafic pour les sections en T et les intersections. Il fournit également des fonctionnalités pour appliquer différents types d'entités comme des véhicules de différentes tailles (voitures, bus) et des piétons dans le modèle.

• Kafka

  Kafka est un système de messagerie distribué, de publication-abonnement et persistant pour les données qu'il reçoit, conçu pour évoluer facilement et prendre en charge des débits de données très élevés.
  
• Néo4j

Une base de données de graphes stocke des nœuds et des relations au lieu de tables ou de documents. Les données sont stockées comme vous pourriez esquisser des idées sur un tableau blanc. Vos données sont stockées sans les restreindre à un modèle prédéfini, ce qui permet une manière très flexible de les penser et de les utiliser.

•	PageRank

L'algorithme PageRank mesure l'importance de chaque nœud dans le graphique, en fonction du nombre de relations entrantes et de l'importance des nœuds source correspondants.

# II. Conception :
## 1. introduction : 
La phase de conception définit les structures et les modèles à suivre lors de la phase de mise en œuvre de l'application. C'est la phase où l'on prépare l'architecture du projet et où l'on définit la structure de l'application et la répartition des tâches que l'on va mettre en place.
L'objectif de ce projet est de mettre en place une application dans un contexte Big-data permettant la détection des fraudes en temps réel des taxis circulant sur le réseau routier de la ville de Berrechid.

## 2. Architecture globale :
Comme le montre l'image ci-dessous, l'architecture globale de notre projet commence par la génération de données par le simulateur de sumo. Ensuite, nous connectons Kafka à sumo pour collecter ces données et les stocker dans une base de données orientée graphe neo4j afin que les nœuds du graphe représentent les rues et arrêtent le passage d'un taxi entre deux nœuds. Enfin, l'algorithme PageRank est appliqué pour détecter la fraude des taxis à travers les nœuds qui composent leurs itinéraires.

![image](https://user-images.githubusercontent.com/81876011/153178110-672182d0-978f-4dfc-a445-d31deaa1f502.png)

## 3. Analyse comparative :
• Pourquoi neo4j ?
* Manipuler des données fortement connectées ;
* Pour supporter un modèle complexe et flexible ;
* Pour obtenir des performances exceptionnelles pour la recherche de chemin : chemin le plus court, identification de sous-graphes ou plus spécifiquement : calculs d'itinéraire, mais aussi détection de fraude, recommandation, réseaux sociaux.

• Pourquoi Kafka ?
* Faible latence
* Tolérance aux pannes
* Traitement en temps réel

• Pourquoi PageRank ?
* Puisqu'il pré calcule le score de classement, cela prend moins de temps et donc c'est rapide.
* Il renvoie les pages importantes car le classement est calculé sur la base de la popularité d'une page.

## 4. Étapes du projet :
•	Étape 1:
La première étape consiste à connecter Kafka au simulateur de sumo à l'aide d'un script python.

•	Étape 2:
La deuxième étape consiste à stocker les données sumo dans la base de données neo4j.

•	Étape 3:
La troisième étape consiste à appliquer l'algorithme PageRank à notre graphique pour détecter les nœuds frauduleux en utilisant les scores que nous donnons.

# III. Partie technique :
## 1. Obtenir des données de SUMO :
En urbanisme, les réseaux routiers quadrillés sont assez courants. Dans SUMO, nous mettons en place une grille 5x5 avec chaque route d'une longueur de 200m, et 3 voies, comme ci-dessous :

![image](https://user-images.githubusercontent.com/81876011/153180584-a89552e6-c5ae-4b15-944a-68ea6a98f4c7.png)

Ensuite, nous utilisons randomTrips.py situé dans le dossier outils du répertoire d'accueil de SUMO (sumo -> outils), pour générer des trajets aléatoires pour un certain nombre de véhicules (200 véhicules dans cet exemple). Les heures de début et de fin indiquent les heures pendant lesquelles les véhicules entrent dans la simulation. J'ai choisi 0 et 1, ce qui signifie que tous les véhicules entrent dans la simulation dans la première seconde de la simulation. La période désigne le taux d'arrivée des véhicules.

![image](https://user-images.githubusercontent.com/81876011/153180682-29d7feb9-e575-4e78-b8cc-504dfc97f2b9.png)

Ensuite, nous générons les itinéraires empruntés par les véhicules individuels à l'aide du jtrrouter de SUMO, entre les temps 0 et 10000.

![image](https://user-images.githubusercontent.com/81876011/153180743-4533bbc3-756e-4419-9ecb-9d524d57e56b.png)

Enfin, par souci de simplicité, nous voulons maintenir une densité constante. La façon la plus évidente de le faire est de conduire des véhicules au hasard et de ne pas quitter la simulation.

![image](https://user-images.githubusercontent.com/81876011/153180844-72352536-b972-4136-81a8-282f0b6b250a.png)

Ensuite, nous créons un fichier de configuration sumo, afin d'exécuter la simulation dans SUMO, qui est essentiellement un fichier .xml avec certains attributs, contenant les noms du fichier réseau, du fichier d'itinéraire et du fichier de reroutage supplémentaire pour que les véhicules restent dans le simulation jusqu'à ce que la simulation soit terminée. Nous définissons un fichier de sortie, pour stocker les informations détaillées du véhicule lors de la simulation de trafic.

![image](https://user-images.githubusercontent.com/81876011/153181115-486c5fd1-0d8d-47ba-b74d-24600602add5.png)

En utilisant l'interface graphique SUMO, pour générer le fichier xml, nous pouvons procéder comme suit

![image](https://user-images.githubusercontent.com/81876011/153181709-009bd81d-96e1-4e29-b27f-0f0504172078.png)
![image](https://user-images.githubusercontent.com/81876011/153181727-f42763a6-6a5a-44e1-a411-3497ceaa1ea0.png)
![image](https://user-images.githubusercontent.com/81876011/153181743-e04a86ac-c717-4db5-9df5-98ecfedbadc9.png)
![image](https://user-images.githubusercontent.com/81876011/153181757-c0b1173d-48fb-467b-bcf4-86de5f8109bb.png)

Nous avons utilisé openstreetmap pour recadrer le réseau berrechid et pouvoir extraire la carte avec laquelle nous allons faire la simulation, et puisque le simulateur SUMO prend des fichiers xml en entrée, il est nécessaire de convertir le fichier osm à l'aide de la commande netConvert en fichiers xml qui sera exécuté sur le logiciel de simulation de suivi de voiture SUMO.

![image](https://user-images.githubusercontent.com/81876011/153182004-02d3149d-9c1f-47b2-a8d4-8ebc11db4135.png)
![image](https://user-images.githubusercontent.com/81876011/153182027-5b7d9945-4a3b-431f-a2d5-e20a93ec17f2.png)
![image](https://user-images.githubusercontent.com/81876011/153182048-c3277ed5-d3e0-449f-a514-00992ad59ddf.png)
![image](https://user-images.githubusercontent.com/81876011/153182075-12341e37-d618-4353-8118-274624085fb3.png)
![image](https://user-images.githubusercontent.com/81876011/153182095-5bcd00bf-c7a1-43ed-861d-24babd266fba.png)
![image](https://user-images.githubusercontent.com/81876011/153182116-c8ea66a3-c420-4b63-a2d1-ec34d16e56ae.png)




