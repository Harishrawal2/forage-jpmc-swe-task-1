import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint(self):
        quotes = [
            {'stock': 'ABC', 'top_bid': {'price': 100}, 'top_ask': {'price': 105}},
            {'stock': 'DEF', 'top_bid': {'price': 200}, 'top_ask': {'price': 210}},
        ]
        expected_results = [
            ('ABC', 100.0, 105.0, 102.5),
            ('DEF', 200.0, 210.0, 205.0)
        ]

        for quote, expected in zip(quotes, expected_results):
            self.assertEqual(getDataPoint(quote), expected)

    def test_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'stock': 'ABC', 'top_bid': {'price': 105}, 'top_ask': {'price': 100}},
            {'stock': 'DEF', 'top_bid': {'price': 210}, 'top_ask': {'price': 200}},
        ]
        expected_results = [
            ('ABC', 105.0, 100.0, 102.5),
            ('DEF', 210.0, 200.0, 205.0)
        ]

        for quote, expected in zip(quotes, expected_results):
            self.assertEqual(getDataPoint(quote), expected)

    def test_getRatio(self):
        # Test normal cases
        self.assertEqual(getRatio(100, 200), 0.5)
        self.assertEqual(getRatio(200, 100), 2.0)

        # Test edge cases
        self.assertIsNone(getRatio(100, 0))  # Avoid division by zero
        self.assertEqual(getRatio(0, 100), 0.0)

if __name__ == '__main__':
    unittest.main()
