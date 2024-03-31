import unittest
from utils import last_transactions
import os


class LastTransactions(unittest.TestCase):
    def test_check_data(self):
        self.assertEqual(last_transactions.check_data([]), False)
        self.assertEqual(last_transactions.check_data([{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
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
        }]), True)
        self.assertEqual(last_transactions.check_data([{
            "id": 441945886,
            "state": "EXECUTED",
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
        }]), False)
        self.assertEqual(last_transactions.check_data([{
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
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
        }]), False)
        self.assertEqual(last_transactions.check_data([{
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
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
        }]), False)
        self.assertEqual(last_transactions.check_data([{
            "id": 441945886,
            "date": "2019-08-26T10:50:58.294041",
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
        }]), False)
        self.assertEqual(last_transactions.check_data([{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }]), False)
        self.assertEqual(last_transactions.check_data([{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }]), False)
        self.assertEqual(last_transactions.check_data([{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
        }]), False)

    def test_prepare_data(self):
        self.assertEqual(last_transactions.prepare_data("../requirements.txt", 5), [])
        self.assertEqual(last_transactions.prepare_data(os.getcwd() + "/tests/broken_operations_test.json", 5), [])
        self.assertEqual(last_transactions.prepare_data(os.getcwd() + '/tests/operations_test.json', 5), [
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
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-11-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 64686473678894779589",
                "to": "Maestro 1596837868705199"
            },
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-10-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            },
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-09-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "to": "Счет 35383033474447895560"
            },
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-08-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "to": "MasterCard 7158300734726758"
            }
        ])

    def test_hide_data(self):
        self.assertEqual(last_transactions.hide_data(
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
            ]),
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
                    "from": "Maestro 1596 83** **** 5199",
                    "to": "Счет **9589"
                }])
        self.assertEqual(last_transactions.hide_data(
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-11-26T10:50:58.294041",
                    "operationAmount": {
                        "amount": "31957.58",
                        "currency": {
                            "name": "руб.",
                            "code": "RUB"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "Счет 64686473678894779589",
                    "to": "Maestro 1596837868705199"
                },
            ]),
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-11-26T10:50:58.294041",
                    "operationAmount": {
                        "amount": "31957.58",
                        "currency": {
                            "name": "руб.",
                            "code": "RUB"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "Счет **9589",
                    "to": "Maestro 1596 83** **** 5199"
                }
            ])
        self.assertEqual(last_transactions.hide_data([]), [])
        self.assertEqual(last_transactions.hide_data([{
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-09-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "to": "Счет 35383033474447895560"
        }]), [{
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-09-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "to": "Счет **5560"
        }])
        self.assertEqual(last_transactions.hide_data([{
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-08-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "to": "MasterCard 7158300734726758"
        }]), [{
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-08-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "to": "MasterCard 7158 30** **** 6758"
        }
        ])
