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

from pprint import pformat
from six import iteritems
import re


class SourcesList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, total=None, sources=None, took_ms=None, range=None):
        """
        SourcesList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total': 'int',
            'sources': 'object',
            'took_ms': 'int',
            'range': 'int'
        }

        self.attribute_map = {
            'total': 'total',
            'sources': 'sources',
            'took_ms': 'took_ms',
            'range': 'range'
        }

        self._total = total
        self._sources = sources
        self._took_ms = took_ms
        self._range = range

    @property
    def total(self):
        """
        Gets the total of this SourcesList.


        :return: The total of this SourcesList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this SourcesList.


        :param total: The total of this SourcesList.
        :type: int
        """

        self._total = total

    @property
    def sources(self):
        """
        Gets the sources of this SourcesList.


        :return: The sources of this SourcesList.
        :rtype: object
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this SourcesList.


        :param sources: The sources of this SourcesList.
        :type: object
        """

        self._sources = sources

    @property
    def took_ms(self):
        """
        Gets the took_ms of this SourcesList.


        :return: The took_ms of this SourcesList.
        :rtype: int
        """
        return self._took_ms

    @took_ms.setter
    def took_ms(self, took_ms):
        """
        Sets the took_ms of this SourcesList.


        :param took_ms: The took_ms of this SourcesList.
        :type: int
        """

        self._took_ms = took_ms

    @property
    def range(self):
        """
        Gets the range of this SourcesList.


        :return: The range of this SourcesList.
        :rtype: int
        """
        return self._range

    @range.setter
    def range(self, range):
        """
        Sets the range of this SourcesList.


        :param range: The range of this SourcesList.
        :type: int
        """

        self._range = range

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
