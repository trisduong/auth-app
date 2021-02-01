import unittest


class ProjectTests(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEquals(app.debug, False)

    def tearDown(self) -> None:
        pass

    def test_health_page(self):
        response = self.app.get('/health', follow_redirects=True)
        self.assertIn(b'ok', response.data)

    def test_crawl_page(self):
        response = self.app.get('/top', follow_redirects=True)
        self.assertIn(b'', response.data)

    def test_logout_page(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'', response.data)


if __name__ == "__main__":
    unittest.main()
