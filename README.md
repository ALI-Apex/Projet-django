# Django Web App - Merchex

Application Django pour [description].

## Installation

### Prérequis
- Python 3.11+
- Conda (Anaconda ou Miniconda)

### Setup avec Conda
```bash
# Créer l'environnement virtuel
conda create -n env_django python=3.11 -y

# Activer l'environnement
conda activate env_django

# Installer les dépendances
pip install -r requirements.txt
```

## Configuration de la base de données
```bash
cd merchex
python manage.py migrate
```

## Lancement du serveur
```bash
python manage.py runserver
```

Ouvrez votre navigateur sur : http://127.0.0.1:8000/

## Technologies

- Python 3.11
- Django 5.2+
- SQLite (dev)