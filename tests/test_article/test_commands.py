import pytest
import random

from blog.models import Article
from blog.commands import CreateArticleCommand, AlreadyExists

@pytest.fixture
def random_name():
    names = ["John", "Jane", "Marry"]
    return random.choice(names)

def test_fixture_usage(random_name):
    assert random_name

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
    assert db_article.content == article.content

def test_create_article1(monkeypatch):
    """
    Given createArticleCommand with valid author, title and content properties
    WHEN the execute method is called
    THEN a new Article must exist in the database with the same attributes
    """
    article = Article(
        author="john@doe.com",
        title="new article",
        content="this is some content"
    )
    monkeypatch.setattr(
        Article,
        "save",
        lambda self: article
    )
    cmd = CreateArticleCommand(
        author="john@doe.com",
        title="new article",
        content="this is some content"
    )
    db_article = cmd.execute()

    assert db_article.id == article.id
    assert db_article.author == article.author
    assert db_article.title == article.title
    assert db_article.content == article.content

def test_create_article_already_exists():
    """
    Given CreateArticleCommand with a title of some article in database
    WHEN the execute method is called
    THEN the AlreadyExists exception must be raised
    """
    Article(
        author="jane@doe.com",
        title="New Article",
        content="Super extra awesome article"
    ).save()

    cmd = CreateArticleCommand(
        author="john@doe.com",
        title="New Article",
        content="Super awesome article"
    )

    with pytest.raises(AlreadyExists):
        cmd.execute()



