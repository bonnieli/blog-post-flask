import pytest

from db.shared import db
from app import create_app
import seed
from tests.utils import SYSTEM_TIME, patch_time


@pytest.fixture
def client():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["TESTING"] = True
    with patch_time(SYSTEM_TIME):
        with app.test_client() as client:
            with app.app_context():
                db.init_app(app)
                seed.reset(db)
                seed.seed(db)
            yield client
