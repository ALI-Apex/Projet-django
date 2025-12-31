# Merchex - Application Django de Marketplace Musicale

Merchex est une application web Django permettant de gérer une marketplace pour les groupes musicaux et leurs annonces. Les utilisateurs peuvent découvrir des groupes, consulter leurs biographies, et parcourir des annonces de produits musicaux (disques, vêtements, posters, etc.).

## Fonctionnalités

### Gestion des Groupes Musicaux
- **Liste des groupes** : Affichage de tous les groupes avec liens vers leurs détails
- **Détails d'un groupe** : Biographie, genre musical, année de formation, statut actif, site officiel
- **Création de groupes** : Formulaire pour ajouter de nouveaux groupes via l'interface web
- **Genres musicaux** : Hip-Hop, Synth-Pop, Alternative Rock, R&B, Rap Français

### Gestion des Annonces
- **Liste des annonces** : Affichage de toutes les annonces disponibles
- **Détails d'une annonce** : Titre, description, année, type, statut de vente, groupe associé
- **Création d'annonces** : Formulaire pour ajouter de nouvelles annonces
- **Types d'annonces** : Records, Clothing, Posters, Miscellaneous

### Autres Fonctionnalités
- **Page À propos** : Informations sur l'application
- **Contact** : Formulaire de contact avec envoi d'email
- **Administration Django** : Interface d'administration pour gérer les données
- **Templates responsives** : Interface utilisateur avec CSS personnalisé

## Technologies Utilisées

- **Backend** : Python 3.11+, Django 6.0
- **Base de données** : SQLite (développement)
- **Frontend** : HTML5, CSS3, Django Templates
- **Outils de qualité** :
  - Ruff (linter et formateur)
  - Pre-commit hooks
  - Commitizen (messages de commit conventionnels)
- **Email** : Configuration SMTP pour les formulaires de contact

## Installation

### Prérequis
- Python 3.11 ou supérieur
- Git
- (Optionnel) Conda pour la gestion d'environnement virtuel

### Étapes d'Installation

1. **Cloner le dépôt** :
   ```bash
   git clone <url-du-depot>
   cd django-web-app
   ```

2. **Créer un environnement virtuel** :
   ```bash
   # Avec venv
   python -m venv env
   source env/bin/activate  # Sur Windows: env\Scripts\activate

   # Ou avec conda
   conda create -n merchex python=3.11 -y
   conda activate merchex
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données** :
   ```bash
   cd merchex
   python manage.py migrate
   ```

5. **Créer un superutilisateur (optionnel)** :
   ```bash
   python manage.py createsuperuser
   ```

## Utilisation

### Lancement du serveur de développement
```bash
cd merchex
python manage.py runserver
```

Ouvrez votre navigateur à l'adresse : http://127.0.0.1:8000/

### URLs principales
- **Page d'accueil** : `/` (redirige vers les groupes)
- **Groupes** : `/bands/` (liste), `/bands/<id>/` (détail), `/bands/add/` (création)
- **Annonces** : `/listings/` (liste), `/listings/<id>/` (détail), `/listings/add/` (création)
- **À propos** : `/about-us/`
- **Contact** : `/contact-us/`
- **Administration** : `/admin/` (nécessite superutilisateur)

### Interface d'administration
Accédez à `/admin/` pour gérer les groupes et annonces via l'interface Django admin.

## Structure du Projet

```
django-web-app/
├── README.md
├── requirements.txt
├── .pre-commit-config.yaml  # Configuration pre-commit
├── cz.yaml                  # Configuration Commitizen
├── .gitignore
├── merchex/                 # Projet Django principal
│   ├── manage.py
│   ├── merchex/            # Configuration du projet
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── listings/           # Application principale
│       ├── models.py       # Modèles Band et Listing
│       ├── views.py        # Vues pour les pages
│       ├── forms.py        # Formulaires Django
│       ├── admin.py        # Configuration admin
│       ├── urls.py         # URLs de l'app
│       ├── apps.py
│       ├── tests.py
│       ├── migrations/     # Migrations de base de données
│       ├── static/         # Fichiers statiques (CSS)
│       └── templates/      # Templates HTML
│           └── listings/
└── .ruff_cache/            # Cache Ruff
```

## Développement

### Outils de Qualité du Code
Le projet utilise plusieurs outils pour maintenir la qualité du code :

- **Ruff** : Linter et formateur ultra-rapide
- **Pre-commit** : Hooks automatiques avant chaque commit
- **Commitizen** : Validation des messages de commit

### Installation des hooks pre-commit
```bash
pip install pre-commit
pre-commit install
```

### Messages de Commit
Utilisez Commitizen pour des messages de commit standardisés :
```bash
cz commit
```

Ou commitez manuellement en suivant la convention :
- `feat:` pour les nouvelles fonctionnalités
- `fix:` pour les corrections
- `docs:` pour la documentation
- `style:` pour le formatage

### Tests
```bash
python manage.py test
```

### Formatage du Code
```bash
# Avec Ruff
ruff check . --fix
ruff format .
```

## Configuration Email
Pour que le formulaire de contact fonctionne, configurez les paramètres email dans `merchex/settings.py` :

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-server.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

## Déploiement
Pour un déploiement en production :
1. Utilisez un serveur WSGI comme Gunicorn
2. Configurez une base de données PostgreSQL ou MySQL
3. Servez les fichiers statiques avec un serveur web (Nginx/Apache)
4. Configurez les variables d'environnement pour la sécurité

## Contribution
1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nouvelle-fonction`)
3. Commitez vos changements (`cz commit`)
4. Poussez vers la branche (`git push origin feature/nouvelle-fonction`)
5. Ouvrez une Pull Request


## Auteur
Développé par [ALI - openClassroom]
