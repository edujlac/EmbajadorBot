import logging
import sqlite3
import random
from sqlite3 import Cursor, Connection
from typing import Tuple

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class BotDb:

    _connection: Connection = None
    _cursor: Cursor = None

    _table_rows: int = 0

    def __init__(self):
        if self._connection is None:
            self._connection = sqlite3.connect('phrases.db')

    def _get_cursor(self) -> Cursor:
        return self._connection.cursor()

    def get_phrase(self) -> Tuple[str, str]:
        if self._table_rows == 0:
            self._table_rows = self._get_cursor().execute("SELECT COUNT(id) FROM phrases").fetchone()[0]

        return self._get_cursor().execute(
            "SELECT phrase, author FROM phrases WHERE id=?",
            [random.randint(1, self._table_rows)]
        ).fetchone()
