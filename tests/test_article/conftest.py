import os
import tempfile

import pytest

from app.models import Article

@pytest.fixture(autouse=True)
def database():
    handle, file_name = tempfile.mkstemp()
    os.environ["DATABASE_NAME"] = file_name
    Article.create_table(database_name=file_name)
    yield
    os.close(handle)
    os.unlink(file_name)