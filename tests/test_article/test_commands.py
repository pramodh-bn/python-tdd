import pytest

from app.models import Article
from app.commands import CreateArticleCommand, AlreadyExists

def test_create_article():
    """
    Given createArticleCommand with valid author, title and content properties
    WHEN the execute method is called
    THEN a new Article must exist in the database with the same attributes
    """
    cmd = CreateArticleCommand(
        author="john@doe.com",
        title="new article",
        content="this is some content"
    )
    article = cmd.execute()
    db_article = Article.get_by_id(article.id)

    assert db_article.id == article.id
    assert db_article.author == article.author
    assert db_article.title == article.title
    assert db_article.conten == article.content




