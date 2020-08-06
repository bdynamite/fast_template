from peewee import PostgresqlDatabase

from config import settings

db = PostgresqlDatabase(
    settings.db_name,
    host=settings.db_host,
    port=settings.db_port,
    user=settings.db_user,
    password=settings.db_password,
)
