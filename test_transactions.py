import unittest
import _json
from app.models import Account
from app import app, db


class TestWithdrawal(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_deposit(self):
        account = Account(name = 'Test User', email = 'test@email.com', balance= 500)
        db.session.add(account)
        db.session.commit()

        response = self.app.post('/transavtions/deposit', json={'account_id': account.id, 'amount': 500})
        self.assertEqual(response.status_code, 201)

        updated_account = Account.query.get(account.id)
        self.assertEqual(updated_account.balance, 1000)

        transactions = transaction.query.filter_by(account_id = account.id).all()


    def test_withdrawal(self):
        account = Account(name='Test User', email='test@example.com', balance=100)
        db.session.add(account)
        db.session.commit()