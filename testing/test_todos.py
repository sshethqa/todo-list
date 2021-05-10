from flask import url_for
from flask_testing import TestCase
from application.models import Todos
from application import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
                SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY="TEST_SECRET_KEY",
                DEBUG=True, 
                WTF_CSRF_ENABLED=False
            )
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Todos(task="Test the application", complete=False))
        db.session.add(Todos(task="Take out the trash", complete=False))
        db.session.add(Todos(task="Be a real cool dude", complete=False))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_index_get(self):
        response = self.client.get(url_for("index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test the application', response.data)
        self.assertIn(b'Take out the trash', response.data)
        self.assertIn(b'Be a real cool dude', response.data)

    def test_add_get(self):
        response = self.client.get(url_for("add"))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for("update", id=1))
        self.assertEqual(response.status_code, 200)

class TestOrder(TestBase):
    def test_index_order_by_id(self):
        response = self.client.post(
            url_for("index"),
            data=dict(order_with="id"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
    
    def test_index_order_by_complete(self):
        response = self.client.post(
            url_for("index"),
            data=dict(order_with="complete"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_index_order_by_incomplete(self):
        response = self.client.post(
            url_for("index"),
            data=dict(order_with="incomplete"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
    
    def test_index_order_by_other(self):
        response = self.client.post(
            url_for("index"),
            data=dict(order_with="other"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for("add"),
            data=dict(task="123456789"),
            follow_redirects=True
        )
        self.assertIn(b'123456789', response.data)
    
    def test_add_existing_post(self):
        response = self.client.post(
            url_for("add"),
            data=dict(task="Test the application"),
            follow_redirects=True
        )
        self.assertIn(b'You already added this Todo', response.data)

class TestComplete(TestBase):
    def test_complete(self):
        response = self.client.get(
            url_for("complete", id=1), 
            follow_redirects=True
        )
        self.assertEquals(Todos.query.filter_by(id=1).first().complete, True)

class TestIncomplete(TestBase):
    def test_incomplete(self):
        response = self.client.get(
            url_for("incomplete", id=1), 
            follow_redirects=True
        )
        self.assertEquals(Todos.query.filter_by(id=1).first().complete, False)

class TestUpdate(TestBase):
    def test_update(self):
        response = self.client.post(
            url_for("update", id=1), 
            data=dict(task="Updated task"),
            follow_redirects=True
        )
        self.assertIn(b'Updated task', response.data)

class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(
            url_for("delete", id=1),
            follow_redirects=True
        )
        self.assertNotIn(b'Test the application', response.data)