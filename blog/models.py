import os
import sqlite3
import uuid
from typing import List

from pydantic import BaseModel, EmailStr, Field


class NotFound(Exception):
    pass

class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    author: EmailStr
    title: str
    content: str

    @classmethod
    def get_by_id(cls, article_id:str) -> "Article":
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM articles where id=?", (article_id,))

        record = cur.fetchone()
        if record is None:
            raise NotFound

        article = cls(**record)
        con.close()

        return article

    @classmethod
    def get_by_title(cls, title:str):
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM articles WHERE title = ?", (title, ))

        record = cur.fetchone()

        if record is None:
            raise NotFound

        article = cls(**record)
        con.close()

        return article

    @classmethod
    def list(cls) -> List["Article"]:
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM articles")

        records = cur.fetchall()

        articles = [cls(**record) for record in records]

        con.close()

        return articles

    def save(self) -> "Article":
        with sqlite3.connect(os.getenv("DATABASE_NAME", "database.db")) as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO articles (id, author, title, content) values (?, ?, ?, ?)",
                (self.id, self.author, self.title, self.content)
            )
            conn.commit()
        return self

    @classmethod
    def create_table(cls, database_name="database.db"):
        conn = sqlite3.connect(database_name)
        conn.execute(
            "CREATE TABLE IF NOT EXISTS articles (id TEXT, author TEXT, title TEXT, content TEXT)"
        )
        conn.close()

    @classmethod
    def _get_by_attribute(cls, sql_query:str, sql_query_values: tuple):
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute(sql_query, sql_query_values)

        record = cur.fetchone()

        if record is None:
            raise NotFound

        article = cls(**record)
        con.close()

        return article