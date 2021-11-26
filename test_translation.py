import unittest
from translation import translation_text

class testClass(unittest.TestCase):
    def test_translation_text(self):
        result = translation_text("name","ES")
        target='nombre'
        self.assertEqual(result.text, target)