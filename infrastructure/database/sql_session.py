from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = environ.get("DATABASE_URI")

ENGINE = create_engine(
    url=DATABASE_URL
)


DEFAULT_SQL_SESSION = sessionmaker(
    bind=ENGINE,
    autocommit=False,
    expire_on_commit=True
)