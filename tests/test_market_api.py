import unittest
from unittest import mock
import json
from localvolts_api import MarketAPI, MarketData


class TestMarketAPI(unittest.TestCase):
    @mock.patch('localvolts_api.market_api.requests')
    def test_get_market_stats(self, mock_requests):
        # Create a mock response
        mock_response = mock.Mock()
        mock_content = {}
        with open('tests/market_stats.json') as f:
            mock_content = json.load(f)
        mock_response.json.return_value = mock_content
        mock_requests.get.return_value = mock_response

        # Create an instance of MarketAPI with a mock auth object
        mock_auth = mock.Mock()
        market_api = MarketAPI(mock_auth)

        # Call the method under test
        result = market_api.get_market_stats()

        # Assert that the requests.get method was called with the correct URL and headers
        mock_requests.get.assert_called_once_with(
            'https://api.localvolts.com/v1/market/stats',
            headers=mock_auth.get_headers()
        )

        # Assert that the result is an instance of MarketData
        self.assertIsInstance(result, MarketData)

        # Assert that the result contains the expected data
        active_generators = mock_content['objResult']['active_generators']
        self.assertEqual(result.active_generators, active_generators)

if __name__ == '__main__':
    unittest.main()
