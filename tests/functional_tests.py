#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_connexion_cas(self):
        # John a vu le site d'échange de meuble sur le facebook UTC
        # Il navigue jusque là
        self.browser.get('http://localhost:8000')

        # Le titre est marrant
        self.assertIn('Adopte un meuble', self.browser.title)

        self.fail('Finish the test !')

if __name__ == '__main__':
    unittest.main()
