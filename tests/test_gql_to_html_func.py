import json
import os
import unittest

from contentstack_utils.gql import GQL
from contentstack_utils.render.options import Options


def mock_entry():
    path_gql = 'mocks/graphqlmock'
    file = os.path.dirname(os.path.abspath(__file__))
    gql_entry = os.path.join(file, path_gql, 'content.json')
    with open(gql_entry) as file:
        return json.load(file)


class TestGQLToHtml(unittest.TestCase):

    def setUp(self):
        print("logger for convert style")

    def test_gql_to_html(self):
        entry = mock_entry()
        option = Options()
        path_keys = ['srte']
        GQL.json_to_html(entry, path_keys, option)
        self.assertEqual(entry['srte'][0],
                         '<p></p><div><p>Abcd Three</p><div><p>Content type: <span></span></p></div>')
