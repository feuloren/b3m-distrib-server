#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from tornado import testing
from tornado.httpclient import AsyncHTTPClient

class MyTestCase(testing.AsyncTestCase):
    def test_http_fetch(self):
        client = AsyncHTTPClient(self.io_loop)
        client.fetch("http://localhost:8000/", self.stop)
        response = self.wait()
        # Test contents of response
        self.assertTrue(re.match('^<!DOCTYPE html>\n<html.*?>.*</html>$', response.body, re.DOTALL))
        self.assertIn("Bienvenue", response.body)

        self.fail('Finish the test !')

all = MyTestCase

if __name__ == '__main__':
    testing.main()
