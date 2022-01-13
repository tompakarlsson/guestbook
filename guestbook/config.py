from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings for serving the guestbook app"""

    db_uri: str = "sqlite:///database.db"
    db_name: str = "database.db"
    host: str = "localhost"
    port: int = 8000


settings = Settings()
