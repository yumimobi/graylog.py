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
from graylog.apis.systemstats_api import SystemstatsApi


class TestSystemstatsApi(unittest.TestCase):
    """ SystemstatsApi unit test stubs """

    def setUp(self):
        self.api = graylog.apis.systemstats_api.SystemstatsApi()

    def tearDown(self):
        pass

    def test_fs_stats(self):
        """
        Test case for fs_stats

        Filesystem information about this node.
        """
        pass

    def test_jvm_stats(self):
        """
        Test case for jvm_stats

        JVM information about this node.
        """
        pass

    def test_network_stats(self):
        """
        Test case for network_stats

        Networking information about this node.
        """
        pass

    def test_os_stats(self):
        """
        Test case for os_stats

        OS information about this node.
        """
        pass

    def test_process_stats(self):
        """
        Test case for process_stats

        Process information about this node.
        """
        pass

    def test_system_stats(self):
        """
        Test case for system_stats

        System information about this node.
        """
        pass


if __name__ == '__main__':
    unittest.main()
