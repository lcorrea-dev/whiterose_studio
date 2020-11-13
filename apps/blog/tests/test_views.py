from django.test import TestCase, Client


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)

    def test_search_url(self):
        client = Client()
        response = client.get('http://localhost:8000/post/search/')
        self.assertEqual(response.status_code, 200)
