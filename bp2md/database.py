from __future__ import annotations

import sqlite3

from bp2md.config import OUTPUT_DIR


class BenchmarkDatabase:

    def __init__(self):

        self.db = OUTPUT_DIR / "benchmark.db"

        self.conn = sqlite3.connect(self.db)

        self.create_tables()

    def create_tables(self):

        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS benchmark (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                pdf TEXT,

                extractor TEXT,

                score INTEGER,

                pages INTEGER,

                words INTEGER,

                characters INTEGER
            )
            """
        )

        self.conn.commit()

    def insert(
        self,
        pdf,
        extractor,
        score,
        pages,
        words,
        characters,
    ):

        self.conn.execute(
            """
            INSERT INTO benchmark (

                pdf,
                extractor,
                score,
                pages,
                words,
                characters

            )

            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                pdf.name,
                extractor,
                score,
                pages,
                words,
                characters,
            ),
        )

        self.conn.commit()

    def close(self):
        self.conn.close()