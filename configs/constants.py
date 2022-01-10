from environs import Env
from pathlib import Path
from os.path import join as join_path

BASE_URL = Path(__file__).parent.parent
env = Env()
env.read_env()
BOT_TOKEN = env.str('BOT_TOKEN')
BOT_NAME = env.str('BOT_NAME')
# PASSWORD = env.str("PASSWORD")
# SENDER_EMAIL = env.str("SENDER_EMAIL")
LOGO = "db/images.jpg"
MEDIA_FILE = join_path(BASE_URL, 'media')
STORAGE_PATH = join_path(BASE_URL, 'configs', 'mystates.json')
LOG_PATH = join_path(BASE_URL, 'configs', 'log.log')
DB_PATH = join_path(BASE_URL, 'db', 'db.sqlite')
