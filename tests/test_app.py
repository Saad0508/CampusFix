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
    
    def test_valid_login(self):
        response = self.client.post(
            "/login",
            data={
                "email": "student@campusfix.com",
                "password": "123456"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn("/dashboard", response.location)

    def test_invalid_login(self):
        response = self.client.post(
            "/login",
            data={
                "email": "wrong@example.com",
                "password": "wrongpassword"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Invalid email or password", response.data)

    def test_add_complaint(self):
        with self.client.session_transaction() as session:
            session["logged_in"] = True

        response = self.client.post(
            "/complaint",
            data={
                "title": "Projector not working",
                "location": "Lecture Hall 2",
                "priority": "High"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn("/dashboard", response.location)

    def test_invalid_complaint(self):
        with self.client.session_transaction() as session:
            session["logged_in"] = True

        response = self.client.post(
            "/complaint",
            data={
                "title": "",
                "location": "",
                "priority": "High"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn("/dashboard", response.location)


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()