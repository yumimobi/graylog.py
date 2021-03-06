# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.1.1+01d50e5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import graylog
from graylog.rest import ApiException
from graylog.apis.searchuniversalkeyword_api import SearchuniversalkeywordApi


class TestSearchuniversalkeywordApi(unittest.TestCase):
    """ SearchuniversalkeywordApi unit test stubs """

    def setUp(self):
        self.api = graylog.apis.searchuniversalkeyword_api.SearchuniversalkeywordApi()

    def tearDown(self):
        pass

    def test_export_search_keyword_chunked(self):
        """
        Test case for export_search_keyword_chunked

        Export message search with keyword as timerange.
        """
        pass

    def test_field_histogram_keyword(self):
        """
        Test case for field_histogram_keyword

        Datetime histogram of a query using keyword timerange.
        """
        pass

    def test_histogram_keyword(self):
        """
        Test case for histogram_keyword

        Datetime histogram of a query using keyword timerange.
        """
        pass

    def test_search_keyword(self):
        """
        Test case for search_keyword

        Message search with keyword as timerange.
        """
        pass

    def test_stats_keyword(self):
        """
        Test case for stats_keyword

        Field statistics for a query using a keyword timerange.
        """
        pass

    def test_terms_keyword(self):
        """
        Test case for terms_keyword

        Most common field terms of a query using a keyword timerange.
        """
        pass

    def test_terms_stats_relative(self):
        """
        Test case for terms_stats_relative

        Ordered field terms of a query computed on another field using a keyword timerange.
        """
        pass


if __name__ == '__main__':
    unittest.main()
