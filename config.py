from pydantic import BaseSettings


class Settings(BaseSettings):
    db_name = "db_2009_2018"
    db_host = '0.0.0.0'
    db_port = 5432
    db_user = 'postgres'
    db_password = 'postgres'


settings = Settings()
