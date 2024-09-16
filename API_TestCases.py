import unittest
import yaml
from resources.random_data import get_random_data
from resources.api_requests import get_api_request
from resources.api_requests import post_api_request
from resources.api_requests import put_api_request
from resources.api_requests import delete_api_request

config = yaml.safe_load(open("config.yaml"))
api_url = config['API base URL']


# GET, POST, PUT and DELETE TestCase Examples

class APITesting(unittest.TestCase):

    # Here are the API testcases for GET, POST, UPDATE, DELETE HTTP Requests
    def test_get_data(self):
        uri = '/get_data'
        all_data = get_api_request(api_url, uri).get('items')
        random_event_data = get_random_data(all_data)
        name = random_event_data.get('Item Name')
        price = random_event_data.get('price')
        self.assertIsNotNone(all_data)
        self.assertEqual(type(name), str)
        self.assertEqual(type(price), float)

    def test_POST_create_item(self):
        uri = "/post_data"
        new_item = {
            "Item Name": "Something",
            "price": 999.9
        }
        created_item = post_api_request(api_url, uri, payload=new_item)
        self.assertIsNotNone(created_item)
        self.assertEqual(type(created_item.get('price')), float)

    def test_PUT_update_item(self):
        uri = "/put_data"
        new_item = {
            "Item Name": "Something",
            "price": 999.9
        }
        updated_item = put_api_request(api_url, uri, payload=new_item)
        self.assertIsNotNone(updated_item)
        self.assertEqual(type(updated_item.get('price')), float)

    def test_DELETE_remove_item(self):
        uri = "/delete_data"
        deleted_item = delete_api_request(api_url, uri)
        self.assertIsNotNone(deleted_item)
