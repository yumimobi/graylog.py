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


class PipelineConnections(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, stream_id=None, pipeline_ids=None):
        """
        PipelineConnections - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'stream_id': 'str',
            'pipeline_ids': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'stream_id': 'stream_id',
            'pipeline_ids': 'pipeline_ids'
        }

        self._id = id
        self._stream_id = stream_id
        self._pipeline_ids = pipeline_ids

    @property
    def id(self):
        """
        Gets the id of this PipelineConnections.


        :return: The id of this PipelineConnections.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PipelineConnections.


        :param id: The id of this PipelineConnections.
        :type: str
        """

        self._id = id

    @property
    def stream_id(self):
        """
        Gets the stream_id of this PipelineConnections.


        :return: The stream_id of this PipelineConnections.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """
        Sets the stream_id of this PipelineConnections.


        :param stream_id: The stream_id of this PipelineConnections.
        :type: str
        """

        self._stream_id = stream_id

    @property
    def pipeline_ids(self):
        """
        Gets the pipeline_ids of this PipelineConnections.


        :return: The pipeline_ids of this PipelineConnections.
        :rtype: list[str]
        """
        return self._pipeline_ids

    @pipeline_ids.setter
    def pipeline_ids(self, pipeline_ids):
        """
        Sets the pipeline_ids of this PipelineConnections.


        :param pipeline_ids: The pipeline_ids of this PipelineConnections.
        :type: list[str]
        """

        self._pipeline_ids = pipeline_ids

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
