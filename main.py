from utils import last_transactions

last_transactions.last_transactions("operations.json")

print(last_transactions.hide_data(
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-12-26T10:50:58.294041",
                    "operationAmount": {
                        "amount": "31957.58",
                        "currency": {
                            "name": "руб.",
                            "code": "RUB"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589"
                },
            ]))