from django.test import TestCase


class ViewTests(TestCase):

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Holiday Homes</title>", response.content)
