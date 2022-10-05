from yoyo import read_migrations
from yoyo import get_backend
from os import getenv


def set():
    MYSQL_USER = getenv('MYSQL_USER')
    MYSQL_PASSWORD = getenv('MYSQL_PASSWORD')
    MYSQL_HOST = getenv('MYSQL_HOST')
    MYSQL_DATABASE = getenv('MYSQL_DATABASE')
    backend = get_backend(
        f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}')
    migrations = read_migrations('./migrations')
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
    return
