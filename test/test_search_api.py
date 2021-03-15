# coding: utf-8

"""
    universal search engine

    universal search engine api  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import universal_search_engine
from universal_search_engine.api.search_api import SearchApi  # noqa: E501
from universal_search_engine.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = universal_search_engine.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_index(self):
        """Test case for add_index

        Add Index By Api  # noqa: E501
        """
        pass

    def test_add_object(self):
        """Test case for add_object

        This will add an object to the given index.  # noqa: E501
        """
        pass

    def test_add_objects(self):
        """Test case for add_objects

        This will add an array of objects to the given index.  # noqa: E501
        """
        pass

    def test_copy_index_config(self):
        """Test case for copy_index_config

        Copy Index configuration from one index to another  # noqa: E501
        """
        pass

    def test_delete_index(self):
        """Test case for delete_index

        Delete Index  # noqa: E501
        """
        pass

    def test_delete_object(self):
        """Test case for delete_object

        This will delete the object with given object id  # noqa: E501
        """
        pass

    def test_generate_event(self):
        """Test case for generate_event

        This will generate an event.  # noqa: E501
        """
        pass

    def test_get_all_objects(self):
        """Test case for get_all_objects

        Get All objects stored in index  # noqa: E501
        """
        pass

    def test_search_query(self):
        """Test case for search_query

        """
        pass


if __name__ == '__main__':
    unittest.main()