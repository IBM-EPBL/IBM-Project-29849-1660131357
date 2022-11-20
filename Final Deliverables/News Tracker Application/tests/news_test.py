import unittest
from ..models import Articles

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.articles = Articles(
            "Techcrunch", 
            "Steve Njuguna", 
            "Nike acquires NFT collectibles studio RTFKT", 
            "Nike is taking a plunge deeper into the world of crypto collectibles, announcing that they’re acquiring the NFT studio RTFKT (pronounced “artifact”). The acquisition announcement ...", 
            "https://techcrunch.com/2021/12/13/nike-acquires-nft-collectibles-studio-rtfkt/", 
            "https://techcrunch.com/wp-content/uploads/2021/12/FC3_itGXEAA6z5g.jpg?w=1390&crop=1", 
            "2021-12-13T20:19:00Z"
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.articles, Articles))

if __name__ == "__main__":
    unittest.main()
