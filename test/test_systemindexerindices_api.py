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
from graylog.apis.systemindexerindices_api import SystemindexerindicesApi


class TestSystemindexerindicesApi(unittest.TestCase):
    """ SystemindexerindicesApi unit test stubs """

    def setUp(self):
        self.api = graylog.apis.systemindexerindices_api.SystemindexerindicesApi()

    def tearDown(self):
        pass

    def test_all(self):
        """
        Test case for all

        List all open, closed and reopened indices.
        """
        pass

    def test_close(self):
        """
        Test case for close

        Close an index. This will also trigger an index ranges rebuild job.
        """
        pass

    def test_closed(self):
        """
        Test case for closed

        Get a list of closed indices that can be reopened.
        """
        pass

    def test_delete(self):
        """
        Test case for delete

        Delete an index. This will also trigger an index ranges rebuild job.
        """
        pass

    def test_multiple(self):
        """
        Test case for multiple

        Get information of all specified indices and their shards.
        """
        pass

    def test_open(self):
        """
        Test case for open

        Get information of all open indices managed by Graylog and their shards.
        """
        pass

    def test_reopen(self):
        """
        Test case for reopen

        Reopen a closed index. This will also trigger an index ranges rebuild job.
        """
        pass

    def test_reopened(self):
        """
        Test case for reopened

        Get a list of reopened indices, which will not be cleaned by retention cleaning
        """
        pass

    def test_single(self):
        """
        Test case for single

        Get information of an index and its shards.
        """
        pass


if __name__ == '__main__':
    unittest.main()