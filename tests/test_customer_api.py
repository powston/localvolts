import unittest
from unittest import mock
from localvolts_api import CustomerAPI, CustomerIntervalData

class TestCustomerAPI(unittest.TestCase):
    @mock.patch('localvolts_api.customer_api.requests')
    def test_get_interval_data(self, mock_requests):
        # Create a mock response
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            'key1': 'value1',
            'key2': 'value2'
        }
        mock_requests.get.return_value = mock_response

        # Create an instance of CustomerAPI with a mock auth object
        mock_auth = mock.Mock()
        customer_api = CustomerAPI(mock_auth)

        # Call the method under test
        result = customer_api.get_interval_data(nmi='123', from_time='2022-01-01T00:00:00Z', to_time='2022-01-02T00:00:00Z')

        # Assert that the requests.get method was called with the correct URL, headers, and params
        mock_requests.get.assert_called_once_with(
            'https://api.localvolts.com/v1/customer/interval',
            headers=mock_auth.get_headers(),
            params={'NMI': '123', 'from': '2022-01-01T00:00:00Z', 'to': '2022-01-02T00:00:00Z'}
        )

        # Assert that the result is an instance of CustomerIntervalData
        self.assertIsInstance(result, CustomerIntervalData)

        # Assert that the result contains the expected data
        self.assertEqual(result.data, {
            'key1': 'value1',
            'key2': 'value2'
        })

if __name__ == '__main__':
    unittest.main()
