import unittest
import _json
from app.models import Account
from app import db


class TestDeleteAccount(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_deleting_accounr(self):
        account = Account(name = 'test user', email = 'test@email.com', balance = 500)
        db.session.add(account)
        db.session.commit()
        
        response = self.aap.delet(f'/accounts/{account.id}')
        self.assertEqual(response.status_code, 204)
        deleted_account = Account.query.get(account.id)
        self.assertIsNone(deleted_account)

    def test_delete_nonexistent_account(self):
        response = self.app.delete(f'/accounts/999')
        self.assertEqual(response.status_code, 404)   