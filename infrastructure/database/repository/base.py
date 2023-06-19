from infrastructure.database.sql_session import DEFAULT_SQL_SESSION


class SqlBaseRepo:
    def __init__(self, session=DEFAULT_SQL_SESSION):
        self.session = None
        self._session_factory = session

    def __enter__(self):
        self.session = self._session_factory()
        return self

    def __exit__(self, type_, value, traceback):
        self.session.expunge_all()
        self.session.close()
