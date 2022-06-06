from typing import List
from pydantic import BaseModel
from app.models import Article

class ListArticlesQuery(BaseModel):

    def execute(self) -> List[Article]:
        articles = Article.list()
        return articles