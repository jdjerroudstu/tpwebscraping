# tpwebscraping

Instructions d'installation et d'exécution
Suivez ces étapes pour exécuter le projet :

1. Cloner le projet
Clonez le dépôt en local sur votre machine avec la commande suivante :

git clone <URL_DU_REPO>


2. Accéder au dossier du projet
Une fois le projet cloné, accédez au répertoire principal avec cette commande :
cd legendsscraper
3. Préparer le projet
4. 
Avant de lancer le scraper, vous pouvez supprimer les fichiers générés lors d'une exécution précédente pour éviter les conflits :

legends.json
legends.csv
legends.html
Supprimez-les manuellement ou utilisez la commande suivante dans votre terminal :
rm legends.json legends.csv legends.html

4. Exécuter le scraper
Lancez le spider legends pour collecter les données et générer les fichiers nécessaires. Utilisez la commande suivante dans le terminal :

scrapy crawl legends

6. Visualiser les résultats
Une fois l'exécution terminée, les fichiers suivants seront créés dans le répertoire principal du projet :

legends.json : Contient les données extraites au format JSON.
legends.csv : Contient les données extraites au format CSV.
legends.html : Une page HTML stylisée avec pagination pour afficher les informations des champions.


Ouvrez le fichier legends.html dans un navigateur pour visualiser les résultats :

open legends.html  # macOS
xdg-open legends.html  # Linux
start legends.html  # Windows

Fonctionnalités du projet

Scraping avec Scrapy :

Extraction des informations des champions : nom, rôle, type, vitesse de déplacement, portée d'attaque.
Gestion des données manquantes avec des valeurs par défaut.

Pipelines de validation :
Vérification et traitement des données avant leur stockage.

Exportation multi-format :
Génération automatique de fichiers JSON, CSV et HTML.

Pagination dans HTML :
Affichage des champions par groupes de 12 avec navigation fluide.

Exigences système
Python 3.8 ou plus récent

Auteurs
Juda Djerroud | Said Mekaouar
