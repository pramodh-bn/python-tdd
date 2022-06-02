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
    def get_by_id(cls, article_id:str):
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM articles where id=?", (article_id,))

        record = cur.fetchone()
        if record is None:
            raise NotFound

        article = cls(**record)
        con.close()

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
