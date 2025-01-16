# TP Web Scraping

## Justification des choix

### **Technologies utilisées**
1. **Scrapy** : 
   - Puissance et flexibilité pour extraire les données d'un site web.
   - Gestion intégrée des requêtes AJAX et des processus asynchrones.
   - Pipelines pratiques pour valider, transformer et exporter les données.

2. **HTML** :
   - Utilisé pour générer un fichier de visualisation facile à utiliser et accessible via un navigateur.
   - Stylisation avec CSS pour améliorer l'esthétique de la page.

3. **JSON et CSV** :
   - Formats de fichiers standard pour l'exportation des données.
   - JSON pour faciliter l'intégration avec d'autres outils ou applications.
   - CSV pour permettre l'analyse avec des outils tels qu'Excel ou Pandas.

---

### **Choix des données extraites**
1. **Nom, rôle, type** :
   - Ces informations sont fondamentales pour identifier et catégoriser chaque champion.

2. **Portée d'attaque (Attack Range)** :
   - Donnée essentielle pour comprendre le style de combat du champion.

3. **Vitesse de déplacement (Move Speed)** :
   - Permet de comparer la mobilité des champions dans le jeu.

---

### **Pagination dans HTML**
- Une interface paginée améliore la lisibilité lorsque le nombre de champions affichés devient important.
- La navigation fluide rend l'expérience utilisateur plus agréable.

---

### **Validation des données**
- L'utilisation de pipelines permet de garantir l'exactitude et la cohérence des données extraites.
- Traitement des valeurs manquantes pour éviter les incohérences dans les fichiers générés.

---

### **Design visuel**
- Couleurs de fond choisies pour refléter une ambiance moderne et immersive.
- Mise en page claire et cartes uniformes pour chaque champion, facilitant la comparaison des données.

---

## Instructions d'installation et d'exécution

### **Suivez ces étapes pour exécuter le projet :**

### **1. Cloner le projet**
Clonez le dépôt en local sur votre machine avec la commande suivante :
```bash
git clone https://github.com/jdjerroudstu/tpwebscraping.git

### **2. Accéder au dossier du projet**
Une fois le projet cloné, accédez au répertoire principal avec cette commande :
```bash
cd legendsscraper

### **3. Préparer le projet**
Avant de lancer le scraper, vous pouvez supprimer les fichiers générés lors d'une exécution précédente pour éviter les conflits :
- legends.json
- legends.csv
- legends.html
Supprimez-les manuellement ou utilisez la commande suivante dans votre terminal :
```bash
rm legends.json legends.csv legends.html

### **4. Exécuter le scraper**
Lancez le spider legends pour collecter les données et générer les fichiers nécessaires. Utilisez la commande suivante dans le terminal :
```bash
scrapy crawl legends

### **5. Visualiser les résultats**

Une fois l'exécution terminée, les fichiers suivants seront créés dans le répertoire principal du projet :

- legends.json : Contient les données extraites au format JSON.
- legends.csv : Contient les données extraites au format CSV.
- legends.html : Une page HTML stylisée avec pagination pour afficher les informations des champions.


### **6. Ouvrir le fichier HTML**
Ouvrez le fichier **legends.html** dans un navigateur pour visualiser les résultats :

- # macOS
open legends.html

- # Linux
xdg-open legends.html

- # Windows
start legends.html

Fonctionnalités du projet
- Scraping avec Scrapy
   - Extraction des informations des champions : nom, rôle, type, vitesse de déplacement, portée d'attaque.
   - Gestion des données manquantes avec des valeurs par défaut.
- Pipelines de validation
   - Vérification et traitement des données avant leur stockage.
- Exportation multi-format
   - Génération automatique de fichiers JSON, CSV et HTML.
- Pagination dans HTML
   -Affichage des champions par groupes de 12 avec navigation fluide.

- Exigences système
   - Python 3.8 ou plus récent
- Auteurs
   - Juda Djerroud
   - Said Mekaouar


