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
from graylog.apis.systemloggers_api import SystemloggersApi


class TestSystemloggersApi(unittest.TestCase):
    """ SystemloggersApi unit test stubs """

    def setUp(self):
        self.api = graylog.apis.systemloggers_api.SystemloggersApi()

    def tearDown(self):
        pass

    def test_loggers(self):
        """
        Test case for loggers

        List all loggers and their current levels
        """
        pass

    def test_messages(self):
        """
        Test case for messages

        Get recent internal log messages
        """
        pass

    def test_set_single_logger_level(self):
        """
        Test case for set_single_logger_level

        Set the loglevel of a single logger
        """
        pass

    def test_set_subsystem_logger_level(self):
        """
        Test case for set_subsystem_logger_level

        Set the loglevel of a whole subsystem
        """
        pass

    def test_subsystems(self):
        """
        Test case for subsystems

        List all logger subsystems and their current levels
        """
        pass


if __name__ == '__main__':
    unittest.main()
