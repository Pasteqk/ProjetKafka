# Projet de Tracking GPS

Ce projet implémente un système de tracking GPS en temps réel utilisant Apache Kafka pour la collecte de données, PostgreSQL pour le stockage des données, FastAPI pour l'API backend, et Leaflet pour l'affichage des données sur une carte.

## Description
Projet d'Architecture et Microservices d'ING3 à CYTech.
Ce système se compose de plusieurs composants :
- **Producteurs Kafka** : Simulent l'envoi de données GPS. Il y en a 2.
- **Topic Kafka 'coordinates'** : Pour la gestion des messages GPS.
- **Consommateur Kafka** : Lit les messages du topic et les stocke dans PostgreSQL.
- **Base de Données PostgreSQL** : Stocke les données GPS.
- **API FastAPI** : Fournit un accès aux données GPS.
- **Frontend Leaflet** : Affiche les positions GPS sur une carte.

## Requirement

- docker 25 ou version plus récente
- au moins 4Go de mémoire disponible

## Installation 
```bash
git clone https://github.com/Pasteqk/ProjetKafka
```

## Lancement
```bash
cd ProjetKafka
docker compose up
```
Attendez de recevoir un message du type 
```
api_1           | INFO:     172.61.0.1:37798 - "GET /gps/IP1 HTTP/1.1" 200 OK
```
Puis aller sur votre navigateur internet au lien "http://localhost:8080/"

##Exposition des ports
Pour ce projet j'ai exposé les ports suivants :
- 8080 : pour le frontend
- 8000 : pour l'api
- 9093 : pour le kafka
Si vous utilisez déjà un de ces ports, le container docker serait incapable de l'exposé et va donc créer des erreurs.

# Authors

- **Antoine Vacossin**
- Biscorray Alexandre
- Nolan Clerc
- Louis Oger
