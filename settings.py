# t-zone/settings.py
from pathlib import Path
# import de la librairie permettant de lire le fichier .env
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# objet
env = environ.Env()
# env_file ne prend que les strings
environ.Env.read_env(env_file=str(BASE_DIR / "t-zone" / ".env"))

# on récupère les valeurs
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG")
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'