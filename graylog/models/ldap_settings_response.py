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


class LdapSettingsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, enabled=None, system_username=None, system_password=None, ldap_uri=None, use_start_tls=None, trust_all_certificates=None, active_directory=None, search_base=None, search_pattern=None, default_group=None, group_mapping=None, group_search_base=None, group_id_attribute=None, additional_default_groups=None, group_search_pattern=None, display_name_attribute=None):
        """
        LdapSettingsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',
            'system_username': 'str',
            'system_password': 'str',
            'ldap_uri': 'str',
            'use_start_tls': 'bool',
            'trust_all_certificates': 'bool',
            'active_directory': 'bool',
            'search_base': 'str',
            'search_pattern': 'str',
            'default_group': 'str',
            'group_mapping': 'object',
            'group_search_base': 'str',
            'group_id_attribute': 'str',
            'additional_default_groups': 'list[str]',
            'group_search_pattern': 'str',
            'display_name_attribute': 'str'
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'system_username': 'system_username',
            'system_password': 'system_password',
            'ldap_uri': 'ldap_uri',
            'use_start_tls': 'use_start_tls',
            'trust_all_certificates': 'trust_all_certificates',
            'active_directory': 'active_directory',
            'search_base': 'search_base',
            'search_pattern': 'search_pattern',
            'default_group': 'default_group',
            'group_mapping': 'group_mapping',
            'group_search_base': 'group_search_base',
            'group_id_attribute': 'group_id_attribute',
            'additional_default_groups': 'additional_default_groups',
            'group_search_pattern': 'group_search_pattern',
            'display_name_attribute': 'display_name_attribute'
        }

        self._enabled = enabled
        self._system_username = system_username
        self._system_password = system_password
        self._ldap_uri = ldap_uri
        self._use_start_tls = use_start_tls
        self._trust_all_certificates = trust_all_certificates
        self._active_directory = active_directory
        self._search_base = search_base
        self._search_pattern = search_pattern
        self._default_group = default_group
        self._group_mapping = group_mapping
        self._group_search_base = group_search_base
        self._group_id_attribute = group_id_attribute
        self._additional_default_groups = additional_default_groups
        self._group_search_pattern = group_search_pattern
        self._display_name_attribute = display_name_attribute

    @property
    def enabled(self):
        """
        Gets the enabled of this LdapSettingsResponse.


        :return: The enabled of this LdapSettingsResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this LdapSettingsResponse.


        :param enabled: The enabled of this LdapSettingsResponse.
        :type: bool
        """

        self._enabled = enabled

    @property
    def system_username(self):
        """
        Gets the system_username of this LdapSettingsResponse.


        :return: The system_username of this LdapSettingsResponse.
        :rtype: str
        """
        return self._system_username

    @system_username.setter
    def system_username(self, system_username):
        """
        Sets the system_username of this LdapSettingsResponse.


        :param system_username: The system_username of this LdapSettingsResponse.
        :type: str
        """

        self._system_username = system_username

    @property
    def system_password(self):
        """
        Gets the system_password of this LdapSettingsResponse.


        :return: The system_password of this LdapSettingsResponse.
        :rtype: str
        """
        return self._system_password

    @system_password.setter
    def system_password(self, system_password):
        """
        Sets the system_password of this LdapSettingsResponse.


        :param system_password: The system_password of this LdapSettingsResponse.
        :type: str
        """

        self._system_password = system_password

    @property
    def ldap_uri(self):
        """
        Gets the ldap_uri of this LdapSettingsResponse.


        :return: The ldap_uri of this LdapSettingsResponse.
        :rtype: str
        """
        return self._ldap_uri

    @ldap_uri.setter
    def ldap_uri(self, ldap_uri):
        """
        Sets the ldap_uri of this LdapSettingsResponse.


        :param ldap_uri: The ldap_uri of this LdapSettingsResponse.
        :type: str
        """

        self._ldap_uri = ldap_uri

    @property
    def use_start_tls(self):
        """
        Gets the use_start_tls of this LdapSettingsResponse.


        :return: The use_start_tls of this LdapSettingsResponse.
        :rtype: bool
        """
        return self._use_start_tls

    @use_start_tls.setter
    def use_start_tls(self, use_start_tls):
        """
        Sets the use_start_tls of this LdapSettingsResponse.


        :param use_start_tls: The use_start_tls of this LdapSettingsResponse.
        :type: bool
        """

        self._use_start_tls = use_start_tls

    @property
    def trust_all_certificates(self):
        """
        Gets the trust_all_certificates of this LdapSettingsResponse.


        :return: The trust_all_certificates of this LdapSettingsResponse.
        :rtype: bool
        """
        return self._trust_all_certificates

    @trust_all_certificates.setter
    def trust_all_certificates(self, trust_all_certificates):
        """
        Sets the trust_all_certificates of this LdapSettingsResponse.


        :param trust_all_certificates: The trust_all_certificates of this LdapSettingsResponse.
        :type: bool
        """

        self._trust_all_certificates = trust_all_certificates

    @property
    def active_directory(self):
        """
        Gets the active_directory of this LdapSettingsResponse.


        :return: The active_directory of this LdapSettingsResponse.
        :rtype: bool
        """
        return self._active_directory

    @active_directory.setter
    def active_directory(self, active_directory):
        """
        Sets the active_directory of this LdapSettingsResponse.


        :param active_directory: The active_directory of this LdapSettingsResponse.
        :type: bool
        """

        self._active_directory = active_directory

    @property
    def search_base(self):
        """
        Gets the search_base of this LdapSettingsResponse.


        :return: The search_base of this LdapSettingsResponse.
        :rtype: str
        """
        return self._search_base

    @search_base.setter
    def search_base(self, search_base):
        """
        Sets the search_base of this LdapSettingsResponse.


        :param search_base: The search_base of this LdapSettingsResponse.
        :type: str
        """

        self._search_base = search_base

    @property
    def search_pattern(self):
        """
        Gets the search_pattern of this LdapSettingsResponse.


        :return: The search_pattern of this LdapSettingsResponse.
        :rtype: str
        """
        return self._search_pattern

    @search_pattern.setter
    def search_pattern(self, search_pattern):
        """
        Sets the search_pattern of this LdapSettingsResponse.


        :param search_pattern: The search_pattern of this LdapSettingsResponse.
        :type: str
        """

        self._search_pattern = search_pattern

    @property
    def default_group(self):
        """
        Gets the default_group of this LdapSettingsResponse.


        :return: The default_group of this LdapSettingsResponse.
        :rtype: str
        """
        return self._default_group

    @default_group.setter
    def default_group(self, default_group):
        """
        Sets the default_group of this LdapSettingsResponse.


        :param default_group: The default_group of this LdapSettingsResponse.
        :type: str
        """

        self._default_group = default_group

    @property
    def group_mapping(self):
        """
        Gets the group_mapping of this LdapSettingsResponse.


        :return: The group_mapping of this LdapSettingsResponse.
        :rtype: object
        """
        return self._group_mapping

    @group_mapping.setter
    def group_mapping(self, group_mapping):
        """
        Sets the group_mapping of this LdapSettingsResponse.


        :param group_mapping: The group_mapping of this LdapSettingsResponse.
        :type: object
        """

        self._group_mapping = group_mapping

    @property
    def group_search_base(self):
        """
        Gets the group_search_base of this LdapSettingsResponse.


        :return: The group_search_base of this LdapSettingsResponse.
        :rtype: str
        """
        return self._group_search_base

    @group_search_base.setter
    def group_search_base(self, group_search_base):
        """
        Sets the group_search_base of this LdapSettingsResponse.


        :param group_search_base: The group_search_base of this LdapSettingsResponse.
        :type: str
        """

        self._group_search_base = group_search_base

    @property
    def group_id_attribute(self):
        """
        Gets the group_id_attribute of this LdapSettingsResponse.


        :return: The group_id_attribute of this LdapSettingsResponse.
        :rtype: str
        """
        return self._group_id_attribute

    @group_id_attribute.setter
    def group_id_attribute(self, group_id_attribute):
        """
        Sets the group_id_attribute of this LdapSettingsResponse.


        :param group_id_attribute: The group_id_attribute of this LdapSettingsResponse.
        :type: str
        """

        self._group_id_attribute = group_id_attribute

    @property
    def additional_default_groups(self):
        """
        Gets the additional_default_groups of this LdapSettingsResponse.


        :return: The additional_default_groups of this LdapSettingsResponse.
        :rtype: list[str]
        """
        return self._additional_default_groups

    @additional_default_groups.setter
    def additional_default_groups(self, additional_default_groups):
        """
        Sets the additional_default_groups of this LdapSettingsResponse.


        :param additional_default_groups: The additional_default_groups of this LdapSettingsResponse.
        :type: list[str]
        """

        self._additional_default_groups = additional_default_groups

    @property
    def group_search_pattern(self):
        """
        Gets the group_search_pattern of this LdapSettingsResponse.


        :return: The group_search_pattern of this LdapSettingsResponse.
        :rtype: str
        """
        return self._group_search_pattern

    @group_search_pattern.setter
    def group_search_pattern(self, group_search_pattern):
        """
        Sets the group_search_pattern of this LdapSettingsResponse.


        :param group_search_pattern: The group_search_pattern of this LdapSettingsResponse.
        :type: str
        """

        self._group_search_pattern = group_search_pattern

    @property
    def display_name_attribute(self):
        """
        Gets the display_name_attribute of this LdapSettingsResponse.


        :return: The display_name_attribute of this LdapSettingsResponse.
        :rtype: str
        """
        return self._display_name_attribute

    @display_name_attribute.setter
    def display_name_attribute(self, display_name_attribute):
        """
        Sets the display_name_attribute of this LdapSettingsResponse.


        :param display_name_attribute: The display_name_attribute of this LdapSettingsResponse.
        :type: str
        """

        self._display_name_attribute = display_name_attribute

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
