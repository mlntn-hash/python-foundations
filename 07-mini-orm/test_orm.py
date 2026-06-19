import pytest
from orm import User
import orm

@pytest.fixture
def test_db(tmp_path, monkeypatch):
    db_file = tmp_path / "test_users.db"
    monkeypatch.setattr(orm, "DB_NAME", str(db_file))
    User._create_table()
    yield

def test_save_creates_new_user(test_db):
        user = User(name="Bob", email="bob@example.com", age=25)
        user.save()

        assert user.id is not None

def test_get_returns_saved_user(test_db):
        user = User(name="Carol", email="carol@example.com", age=40)
        user.save()

        found = User.get(user.id)

        assert found is not None
        assert found.name == "Carol"
        assert found.age == 40

def test_get_returns_none_for_missing_id(test_db):
        found = User.get(999)
        assert found is None

def test_save_updates_existing_user(test_db):
        user = User(name="Dave", email="dave@example.com", age=30)
        user.save()

        user.age = 31
        user.save()

        updated = User.get(user.id)
        assert updated.age == 31

def test_delete_removes_user(test_db):
        user = User(name="Eve", email="eve@example.com", age=22)
        user.save()

        user.delete()

        assert User.get(user.id) is None