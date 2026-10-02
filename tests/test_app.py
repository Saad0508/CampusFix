import unittest
from app import app


class CampusFixTestCase(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()