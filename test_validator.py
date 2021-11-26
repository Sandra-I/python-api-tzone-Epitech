import unittest
import json
from validator import translation_allowed, validate_json

class testClass(unittest.TestCase):
    def test_translation_allowed(self):
        jsonData = json.loads('{"lang": "ES", "r": 25, "marks": 72}')
        result = translation_allowed(jsonData)
        self.assertEqual(result, True)
    def test_validate_json(self):
        jsonData = json.loads('{"lang": "ES", "img": "gggg"}')
        result = validate_json(jsonData)
        self.assertEqual(result, True)
