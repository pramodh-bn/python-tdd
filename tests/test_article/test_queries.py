from app.models import Article
from app.queries import ListArticlesQuery

def test_list_articles():
    """
    Given 2 articles stored in the database
    WHEN the execute method is called
    THEN it should return 2 articles
    """
    Article(
        author="jane@doe.com",
        title="New Article",
        content="Super Extra Awesome Article"
    ).save()
    Article(
        author="jane@doe.com",
        title="Another Title",
        content="Super Awesome Article"
    ).save()

    query = ListArticlesQuery()

    assert len(query.execute()) == 2

