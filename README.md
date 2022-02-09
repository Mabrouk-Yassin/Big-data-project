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

![1](https://user-images.githubusercontent.com/81876011/153227645-b89c063f-05fe-4ce1-a77a-2f0651d74dbf.png)
![2](https://user-images.githubusercontent.com/81876011/153227649-1a32c3d9-bd1e-461f-86e3-c21e58c5f1a4.png)
![3](https://user-images.githubusercontent.com/81876011/153227652-0fa89ab3-34f3-4d2f-a0b4-33da9fa6ef74.png)
![4](https://user-images.githubusercontent.com/81876011/153227654-96921626-4b9f-4af0-927e-d0d78617ac10.png)


Nous avons utilisé openstreetmap pour recadrer le réseau berrechid et pouvoir extraire la carte avec laquelle nous allons faire la simulation, et puisque le simulateur SUMO prend des fichiers xml en entrée, il est nécessaire de convertir le fichier osm à l'aide de la commande netConvert en fichiers xml qui sera exécuté sur le logiciel de simulation de suivi de voiture SUMO.

![5](https://user-images.githubusercontent.com/81876011/153227875-f0a482ce-3e17-48fb-a423-a174fc8cc394.png)
![6](https://user-images.githubusercontent.com/81876011/153227856-00c2a639-a3f0-43c0-ae55-a9e0ec5dc0d0.png)
![7](https://user-images.githubusercontent.com/81876011/153227864-17e976e9-2c92-4b95-9741-21d58aba32a5.png)
![8](https://user-images.githubusercontent.com/81876011/153227868-08e326d6-528e-4c95-bdb4-bf9c2f3cbb15.png)
![9](https://user-images.githubusercontent.com/81876011/153227869-34f29189-4a8a-4de1-937e-910c3e6971d6.png)
![10](https://user-images.githubusercontent.com/81876011/153227871-8a5c6fc9-19d9-4980-8000-8a0ad68b9494.png)

## 2.Connectez Sumo à Kafka et produisez des données :
Afin de recevoir le flux de données du sumo, kafka est la meilleure solution alors que nous avons plusieurs suivis de voitures. Donc, pour connecter sumo à kafka, nous avons implémenté le script python suivant qui nous permet d'obtenir automatiquement le flux de données de sumo pour le produire avec kafka.

![11](https://user-images.githubusercontent.com/81876011/153228630-a489025f-7c40-4c46-8760-13bb9ac694ba.png)
![12](https://user-images.githubusercontent.com/81876011/153228637-9faac544-eea0-4859-9abb-a0e1a7c874f5.png)

Créer un objet producteur et produire des données.

![13](https://user-images.githubusercontent.com/81876011/153229185-c3d22d6f-7e32-479a-ab38-7cdf8203ba6e.png)

## 3. Charger les données dans la base de données NoSQL Neo4J :

Comme nous recevons plusieurs données de voiture, la meilleure solution est de représenter nos données de flux dans un tableau graphique, donc Neo4J est la meilleure solution pour notre cas.

Dans cette étape, nous allons connecter Kafka avec kafka avec la base de données Neo4J Nosql pour stocker notre flux provenant du système de messagerie kafka.

Dans ce cas, nous consommerons des données, donc un objet Kafka consumer sera nécessaire.

![15](https://user-images.githubusercontent.com/81876011/153232068-1a81cd6f-bad6-4cad-a7a5-6f2ad645c609.png)

## 4. Appliquer l'algorithme PageRank :

Le PageRank est l'algorithme le plus puissant pour classer les nœuds dans un schéma de graphe, dans notre cas les rues.

Ainsi, pour classer les rues les plus importantes dans notre schéma graphique, nous appliquerons l'algorithme neo4J sur les données stockées dans notre base de données NoSQL Neo4j.

Nous avons donc implémenté le script suivant.

![16](https://user-images.githubusercontent.com/81876011/153232930-d3984c53-ddde-46a2-a62a-6311b8e18476.png)

![17](https://user-images.githubusercontent.com/81876011/153233106-0a9a767e-f760-471f-bb6d-f804be3737df.png)
![18](https://user-images.githubusercontent.com/81876011/153233119-4870c478-626a-49d2-b51d-7e3e47b74723.png)

**Flux de données dans Neo4J**

![19](https://user-images.githubusercontent.com/81876011/153233126-e98a1a4c-87b8-4ea3-81af-54a68718d972.png)

## 5. Détecter les actions fraud des taxis :

Jusqu'à présent, nous avons implémenté notre flux de données avec succès et l'algorithme de classement des pages fonctionne bien.

Dans cette étape, nous appliquerons des filtres pour extraire les connaissances du résultat du classement de la page, donc pour chaque rue, nous avons un score d'action frauduleuse comme suit :

![20](https://user-images.githubusercontent.com/81876011/153233851-c1e80d5b-a524-4372-a14b-2806122275f7.png)

Score de fraude de rue

Selon ce score, nous détecterons si un trajet en taxi est frau ou non, nous avons donc fixé un score de 0,6.

Si le score > 0,6 alors ce voyage est sans danger.

Sinon, ce voyage en taxi est une fraude.

![21](https://user-images.githubusercontent.com/81876011/153234460-f71caafe-754b-4e02-95ef-cd18fc407018.png)

Merci!
