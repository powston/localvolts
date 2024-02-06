import unittest
from unittest import mock
from localvolts_api import MarketAPI, MarketData
from localvolts_api import LocalvoltsAuth

class TestMarketAPI(unittest.TestCase):
    @mock.patch('localvolts_api.market_api.requests')
    def test_get_market_stats(self, mock_requests):
        # Create a mock response
        mock_response = mock.Mock()
        mock_result = {
            "objResult": {
                'key1': 'value1',
                'key2': 'value2'
            }
        }
        mock_response.json.return_value = mock_result
        mock_requests.get.return_value = mock_response

        # Create an instance of LocalvoltsAuth with mock API key and Partner ID
        mock_auth = LocalvoltsAuth('mock_api_key', 'mock_partner_id')

        # Create an instance of MarketAPI with the mock auth object
        market_api = MarketAPI(mock_auth)

        # Call the method under test
        result = market_api.get_market_stats()

        # Assert that the requests.get method was called with the correct URL and headers
        mock_requests.get.assert_called_once_with(
            'https://api.localvolts.com/v1/market/stats',
            headers={
                'authorization': 'apikey mock_api_key',
                'partner': 'mock_partner_id'
            }
        )

        # Assert that the result is an instance of dict
        self.assertIsInstance(result, MarketData)

        # Assert that the result contains the expected data
        for key, value in mock_result["objResult"].items():
            self.assertEqual(getattr(result, key), value)

if __name__ == '__main__':
    unittest.main()

