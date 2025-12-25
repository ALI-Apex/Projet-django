# Django Web App - Merchex

Application Django pour [description de votre projet].

## Installation

### Avec Conda
```bash
conda env create -f environment.yml
conda activate env_django
```

### Avec pip
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
# ou
env\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Lancement
```bash
cd merchex
python manage.py migrate
python manage.py runserver
```

## Structure du projet
```
merchex/
├── manage.py           # Script de gestion Django
└── merchex/            # Configuration principale
    ├── settings.py     # Configuration
    ├── urls.py         # Routes URL
    └── wsgi.py         # Déploiement
```

## Technologies

- Python 3.x
- Django
