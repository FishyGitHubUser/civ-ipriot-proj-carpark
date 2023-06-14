import unittest

import json  # you can use toml, json,yaml, or ryo for your config file


class TestConfigParsing(unittest.TestCase):
    def test_parse_config_has_correct_location_and_spaces(self):
        config_string = '''
        {
          "name": "carpark",
          "total-spaces": 130,
          "total-cars": 0,
          "location": "L306",
          "topic-root": "lot",
          "broker": "localhost",
          "port": 1883,
          "topic-qualifier": "entry",
          "is_stuff": false
        }
        '''
        config = json.loads(config_string)
        parking_lot = pc.parse_config(config)
        self.assertEqual(parking_lot['location'], "Moondalup City Square Parking")
        self.assertEqual(parking_lot['total_spaces'], 192)