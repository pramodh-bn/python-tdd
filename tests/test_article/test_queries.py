from blog.models import Article
from blog.queries import ListArticlesQuery
from blog.queries import GetArticleByIDQuery

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



def test_get_articles_by_id():
    """
    Given ID of articles stored in the database
    WHEN the execute method is called on GetArticlesByIDQuery with an ID
    THEN it should return the article with the same ID
    """
    article = Article(
        author="jane@doe.com",
        title="new article",
        content="super extra awesome article"
    ).save()

    query = GetArticleByIDQuery(
        id = article.id
    )

    assert query.execute().id == article.id
