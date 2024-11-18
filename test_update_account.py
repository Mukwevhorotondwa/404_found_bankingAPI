import unittest
import _json
from app.models import Account
from app import db


class TestUpdateAccount(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_successful_update(self):
        account = Account(name = 'Test User', email = 'test@email.com', balance = 500)
        db.session.add(account)
        db.session.commit()

        response = self.app.put(f'/accounts/{account.id}', json={'name': 'Updated Name', 'email': 'updated@example.com'})
        self.assertEqual(response.status_code, 200)

        #for FICA purposes

        updated_account = account.query.get(account.id)
        self.assertEqual(updated_account.name, 'Updated Name')
        self.assertEqual(updated_account.email, 'updated@example.com')


    def test_invalid_update(self):
        with self.assertRaises(ValueError):
            Account(name = 'test user', email = 'invalid_email', balance = 500)
        response = self.app.put(f'/accounts/{Account.id}', json={'email': 'invalid_email'})
        self.assertEqual(response.status_code, 400)
