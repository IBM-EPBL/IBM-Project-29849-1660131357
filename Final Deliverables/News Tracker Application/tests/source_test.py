import unittest
from ..models import Sources

class SourceTest(unittest.TestCase):
    def setUp(self):
        self.source = Sources(
            "ABC News", 
            "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", 
            "https://abcnews.go.com/"
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.source, Sources))

if __name__ == "__main__":
    unittest.main()
