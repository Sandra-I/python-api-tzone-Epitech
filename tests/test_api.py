import sys
sys.path.append("..")

import unittest
import requests
from test_vars import get_var, get_var_translation

class testApi(unittest.TestCase):
    param= get_var()
    param_translation= get_var_translation()
    URL = 'http://sandrai.pythonanywhere.com'
    URLupload='https://tzone.yamikamisama.fr/dev/upload'
    URLtranslation='https://tzone.yamikamisama.fr/dev/upload-with-translation'
    
    
    def test_connect_get(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)

    def test_connect_post(self):
        resp = requests.post(self.URL)
        self.assertEqual(resp.status_code, 405)

    def test_connect_upload(self):
        response = requests.post(self.URLupload,json=self.param)
        print(response.text)
        self.assertEqual(response.status_code, 200)

    def test_connect_upload_transactional(self):
        response = requests.post(self.URLtranslation,json=self.param_translation)
        print(response.text)
        self.assertEqual(response.status_code, 200)
    

    