from unittest.mock import patch
from assignment.source.currency_exchanger import CurrencyExchanger
from assignment.test.utils import get_mock_exchange_api_response

import unittest
import requests

class TestCurrency(unittest.TestCase):
    def setUp(self):
        self.currency = CurrencyExchanger()
        self.mock_api_response = get_mock_exchange_api_response()

    @patch("assignment.source.currency_exchanger.requests")
    def test_get_exchange_rate(self,mock_request):
        mock_request.get.return_value = self.mock_api_response

        #self.currency.get_exchange_rate()
        self.currency.get_currency_rate()

        mock_request.get.assert_called_once()
        mock_request.get.assert_called_with('https://coc-kku-bank.com/foreign-exchange', params={'from': 'THB', 'to': 'USD'})
        self.assertIsNotNone(self.currency.api_response)
        self.assertEqual(self.currency.api_response, self.mock_api_response.json())

        print("\nAPI Response: ", self.currency.api_response)
if __name__ == '__main__':
    unittest.main(verbosity=2)