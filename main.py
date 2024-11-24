from flask import Flask, request, jsonify

app = Flask(__name__)

transactions = []
beneficiaries = []


@app.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify({"data": {"transactions": transactions}, "meta": {"totalPages": 1}})

@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    transaction_id = len(transactions) + 1
    new_transaction = {
        "id": transaction_id,
        "accountId": data["accountId"],
        "type": data["type"],
        "status": data["status"],
        "description": data["description"],
        "transactionDate": data["transactionDate"],
        "amount": data["amount"]
    }
    transactions.append(new_transaction)
    return jsonify({"message": "Transaction added successfully"}), 201

@app.route('/beneficiaries', methods=['GET'])
def get_beneficiaries():
    return jsonify({"data": beneficiaries, "meta": {"totalPages": 1}})

@app.route('/beneficiaries', methods=['POST'])
def add_beneficiary():
    data = request.json
    
    beneficiary_id = len(beneficiaries) + 1
    new_beneficiary = {
        "beneficiaryId": beneficiary_id,
        "name": data["name"],
        "accountNumber": data["accountNumber"],
        "lastPaymentAmount": data["lastPaymentAmount"],
        "lastPaymentDate": data["lastPaymentDate"],
    }
    beneficiaries.append(new_beneficiary)
    return jsonify({"message": "Beneficiary added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)