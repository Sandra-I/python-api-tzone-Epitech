import unittest
import json
from validator import translation_allowed, validateJson

class testClass(unittest.TestCase):
    def test_translation_allowed(self):
        jsonData = json.loads('{"lang": "ES", "r": 25, "marks": 72}')
        result = translation_allowed(jsonData)
        self.assertEqual(result, True)
    def test_validateJson(self):
        jsonData = json.loads('{"lang": "ES", "img": "gggg"}')
        result = validateJson(jsonData)
        self.assertEqual(result, True)