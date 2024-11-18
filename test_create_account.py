import unittest
import _json
from app.models import Account
from app import db


class TestCreateAccount(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_create_account(self):
        account = Account(name = 'test user', email = 'test@email.com', balance = 500)
        db.session.add(account)
        db.session.commit()
        self.assertIsNotNone('account.id')
        self.assertEqual(account.name, 'test user')
        self.assertEqual(account.email, 'test@email.com')

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            Account(name = 'test user', email = 'invalid_email', balance = 500)

    