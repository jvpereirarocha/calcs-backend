from os import environ
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


class BaseRepo:
    def __init__(self):
        self._url = environ.get('DATABASE_URI')
        self._engine = create_engine(self._url)
        self.session = None
        self._session = sessionmaker(
            bind=self._engine,
            autocommit=False,
            expire_on_commit=True
        )

    def __enter__(self):
        self.session = self._session()
        return self

    def __exit__(self, type_, value, traceback):
        self.session.expunge_all()
        self.session.close()